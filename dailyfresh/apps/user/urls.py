from django.conf.urls import url
from django.urls import path,re_path
from user.views import RegisterView,ActiveView,LoginView,UserInfoView,UserInfoOrder,AddressView,LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # url(r'^register$',views.register,name='register'), # 注册
    # path('register/',views.register,name='register'), # 注册
    # path('register_handle/',views.register_handle,name='register_handle'), # 注册处理
    path('register/',RegisterView.as_view(),name='register'), # 注册
    re_path('^active/(?P<token>.*)/$',ActiveView.as_view(),name='active'), # 用户激活
    path('login',LoginView.as_view(),name='login'), # 登录
    # re_path('^$',login_required(UserInfoView.as_view()),name='user'), # 用户中心-信息页
    # path('order',login_required(UserInfoOrder.as_view()),name='order'), # 用户中心-订单页
    # path('address',login_required(AddressView.as_view()),name='address'), # 用户中心-地址页
    re_path('^$',UserInfoView.as_view(),name='user'), # 用户中心-信息页
    re_path('^order/(?P<page>\d+)$', UserInfoOrder.as_view(), name='order'), # 用户中心-订单页
    path('address',AddressView.as_view(),name='address'), # 用户中心-地址页
    path('logout',LoginView.as_view(),name='logout') # 注销登录
]
