import requests
from bs4 import BeautifulSoup
import urllib.request

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
}

def download_code(s):
    url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
    r = s.get(url=url,headers=headers)
    soup = BeautifulSoup(r.text,'lxml')
    #得到图片链接
    image_src = 'https://so.gushiwen.org' + soup.find('img',id="imgCode")['src']
    #下载图片
    r_image = s.get(image_src,headers=headers)
    with open('code.png','wb') as fp:
        fp.write(r_image.content)
    #查找表单所需要的两个参数
    __VIEWSTATE = soup.find('input',id="__VIEWSTATE")['value']
    __VIEWSTATEGENERATOR = soup.find('input',id="__VIEWSTATEGENERATOR")['value']
    return __VIEWSTATE,__VIEWSTATEGENERATOR

def login(view,viewg,s):
    post_url = 'https://so.gushiwen.org/user/login.aspx?from='
    #提示用户输入验证码
    code = input('请输入验证码:')
    formdata = {
        '__VIEWSTATE' : view,
        '__VIEWSTATEGENERATOR' : viewg,
        'from' : '',
        'email' : '17642181300',
        'pwd' : 'mimanibuzhidao741',
        'code' : code,
        'denglu' : '登录',
    }
    #发送响应
    r = s.post(url=post_url,headers=headers,data=formdata)
    with open('gushi.html','w',encoding='utf8') as fp:
        fp.write(r.text)

def main():
    #创建会话
    s = requests.Session()
    #下载验证码到本地
    view,viewg = download_code(s)
    #向post地址发送请求
    login(view,viewg,s)

if __name__ == '__main__':
    main()