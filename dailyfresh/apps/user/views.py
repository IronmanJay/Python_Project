from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import View
import re
from user.models import User,Address
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from utils.mixin import LoginRequiredMixin
from django_redis import get_redis_connection
from goods.models import GoodsSKU
from order.models import OrderInfo,OrderGoods
from django.core.paginator import Paginator

# Create your views here.

class RegisterView(View):
    '''注册'''
    def get(self,request):
        '''显示注册页面'''
        return render(request,'register.html')

    def post(self,request):
        '''进行注册处理'''
        # 接收数据
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')

        # 进行数据校验
        if not all([username, password, email]):
            # 数据不完整
            return render(request, 'register.html', {'errmsg': '数据不完整'})
        # 校验邮箱
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})
        if allow != 'on':
            return render(request, 'register.html', {'errmsg': '请同意协议'})

        # 校验用户名是否重复
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # 用户名不存在
            user = None
        if user:
            # 用户名已存在
            return render(request, 'register.html', {'errmsg': '用户名已存在'})

        # 进行业务处理:进行用户注册
        user = User.objects.create_user(username, email, password)
        user.is_active = 0
        user.save()

        # 发送激活邮件，包含激活链接:http://127.0.0.1:8000/user/active/id
        # 激活链接中需要包含用户的身份信息，并且要把身份信息进行加密
        # 1、加密用户的身份信息，生成激活token
        serializer = Serializer(settings.SECRET_KEY,3600)
        info = {'confirm':user.id}
        token = serializer.dumps(info) # bytes
        token = token.decode()

        # 2、发邮件
        subject = '天天生鲜欢迎信息'
        message = ''
        sender = settings.EMAIL_FROM
        receiver = [email, sender]
        html_message = '<h1>%s，欢迎你成为天天生鲜注册会员。</h1><br/>请点击下面链接激活您的账户<a href="http://127.0.0.1:8000/user/active/%s">http://127.0.0.1:8000/user/active/%s</a>'%(username, token, token)
        send_mail(subject, message, sender, receiver, html_message=html_message)

        # 返回应答，跳转到首页
        return redirect(reverse('goods:index'))

class ActiveView(View):
    '''用户激活'''
    def get(self,request,token):
        '''进行用户激活'''
        # 进行解密，获取要激活的用户信息
        serializer = Serializer(settings.SECRET_KEY, 3600)
        try:
            info = serializer.loads(token)
            # 获取待激活用户的id
            user_id = info['confirm']
            # 根据id获取用户信息
            user = User.objects.get(id=user_id)
            user.is_active = 1
            user.save()
            # 跳转到登录页面
            return redirect(reverse('user:login'))
        except SignatureExpired as e:
            # 激活链接已过期
            return HttpResponse('激活链接已过期')

class LoginView(View):
    '''登录'''
    def get(self,request):
        '''显示登陆页面'''
        # 判断是否记住用户名
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('username')
            checked = 'checked'
        else:
            username = ''
            checked = ''
        # 使用模板
        return render(request,'login.html',{'username':username,'checked':checked})

    def post(self,request):
        '''登录校验'''
        # 接收数据
        username = request.POST.get('username')
        password = request.POST.get('pwd')

        # 校验数据
        if not all([username,password]):
            return render(request,'login.html',{'errmsg':'数据不完整'})

        # 业务处理:登录校验
        user = authenticate(username=username,password=password)
        if user is not None:
            # 用户名密码正确
            if user.is_active:
                # 用户已激活
                # 记录用户的登陆状态
                login(request,user)
                # 获取登陆后所要跳转到的地址
                # 默认跳转到首页
                next_url = request.GET.get('next',reverse('goods:index'))
                # 跳转到next_url
                response =  redirect(next_url)
                # 判断是否需要记住用户名
                remember = request.POST.get('remember')
                if remember == 'on':
                    # 记住用户名
                    response.set_cookie('username',username,max_age=7*24*3600)
                else:
                    response.delete_cookie('username')
                # 返回response
                return response
            else:
                # 用户未激活
                return render(request, 'login.html', {'errmsg': '请激活您的账户'})
        else:
            # 用户名或密码错误
            return render(request,'login.html',{'errmsg':'用户名或密码错误'})

class LogoutView(View):
    '''退出登录'''
    def get(self,request):
        '''退出登录'''
        # 清除用户的session信息
        logout(request)
        # 跳转到登陆界面
        return redirect(reverse('goods:login'))

class UserInfoView(LoginRequiredMixin,View):
    '''用户中心-信息页'''
    def get(self,request):
        '''显示'''
        # page='user'
        # 如果用户未登录->AnonymousUser的一个实例
        # 如果用户登录->User类的一个实例
        # 获取用户的个人信息
        user = request.user
        address = Address.objects.get_default_address(user)
        # 获取用户的历史浏览记录
        # from redis import StrictRedis
        # sr = StrictRedis(host='127.0.0.1',port=6379,db=9)
        con = get_redis_connection('default')
        history_key= 'history_%d'%user.id
        # 获取用户最新浏览的5个商品的id
        sku_ids = con.lrange(history_key,0,4)

        # 从数据库中查询用户浏览的商品的具体信息
        # goods_li = GoodsSKU.objects.filter(id__in=sku_ids)
        # goods_res = []
        # for a_id in sku_ids:
        #     for goods in goods_li:
        #         if a_id == goods.id:
        #             goods_res.append(goods)

        # 遍历获取用户浏览的商品信息
        goods_li = []
        for id in sku_ids:
            goods = GoodsSKU.objects.get(id=id)
            goods_li.append(goods)
        # 组织上下文
        context = {'page':'user','address':address,'goods_li':goods_li}
        # 除了你给模板文件传递的模板变量之外，django框架会把request.user也传给模板文件
        return render(request,'user_center_info.html',context)

class UserInfoOrder(LoginRequiredMixin,View):
    '''用户中心-订单页'''
    def get(self,request,page):
        '''显示'''
        # 获取用户的订单信息
        user = request.user
        orders = OrderInfo.objects.filter(user=user).order_by('-create_time')

        # 遍历获取订单商品的信息
        for order in orders:
            # 根据order_id查询订单商品的信息
            order_skus = OrderGoods.objects.filter(order_id=order.order_id)
            # 遍历order_skus计算商品的小计
            for order_sku in order_skus:
                # 计算小计1
                amount = order_sku.count*order_sku.price
                # 动态给order_sku增加属性amount保存订单商品的小计
                order_sku.amount = amount
            # 动态给order增加属性，保存订单商品的信息
            order.order_skus = order_skus
            order.status_name = OrderInfo.ORDER_STATUS[str(order.order_status)]

        # 分页
        paginator = Paginator(orders,1)

        # 处理页码
        # 获取第page页的内容
        try:
            page = int(page)
        except Exception as e:
            page = 1
        if page > paginator.num_pages:
            page = 1
        # 获取第page页的Page实例对象
        order_page = paginator.page(page)
        # todo：进行页码的控制，页面上最多显示5个页码，总页数如果小于5页，页面上显示所有页码，如果当前页是前3页，显示1-5页，如果当前页是后3页，显示后5页，如果是其他情况，显示当前页的前2页，当前页，当前页的后2页
        num_pages = paginator.num_pages
        if num_pages < 5:
            pages = range(1,num_pages+1)
        elif page <= 3:
            pages = range(1,6)
        elif num_pages - page <= 2:
            pages = range(num_pages-4,num_pages+1)
        else:
            pages = range(page-2,page+3)

        # 组织上下文
        context = {
            'order_page': order_page,
            'pages': pages,
            'page': 'order',
        }

        # 使用模板
        return render(request,'user_center_order.html',context)

class AddressView(LoginRequiredMixin,View):
    '''用户中心-地址页'''
    def get(self,request):
        '''显示'''

        # 获取登录用户的对应User对象
        user = request.user
        # # 获取用户的默认收货地址
        # try:
        #     address = Address.objects.get(user=user,is_default=True)
        # except Address.DoesNotExist:
        #     # 不存在默认收货地址
        #     address = None
        address = Address.objects.get_default_address(user)
        # 使用模板
        # page='address
        return render(request,'user_center_site.html',{'page':'address','address':address})

    def post(self,request):
        '''地址的添加'''
        # 接收数据
        receiver = request.POST.get('receiver')
        addr = request.POST.get('addr')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')

        # 校验数据
        if not all([receiver,addr,phone]):
            return render(request,'user_center_site.html',{'errmsg':'数据不完整'})
        # 校验手机号
        if not re.match(r'^1[3|4|5|7|8][0-9]{9}$',phone):
            return render(request,'user_center_site.html',{'errmsg':'手机格式不正确'})

        # 业务处理:地址添加
        # 如果用户已存在默认收货地址，添加的地址不作为默认收货地址
        # 获取登录用户对应的User对象
        user = request.user
        # try:
        #     address = Address.objects.get(user=user,is_default=True)
        # except Address.DoesNotExist:
        #     # 不存在默认收货地址
        #     address = None
        address = Address.objects.get_default_address(user)
        if address:
            is_default = False
        else:
            is_default = True
        # 添加地址
        Address.objects.create(user=user,receiver=receiver,addr=addr,zip_code=zip_code,phone=phone,is_default=is_default)

        # 返回应答，刷新地址页面
        return redirect(reverse('user:address'))