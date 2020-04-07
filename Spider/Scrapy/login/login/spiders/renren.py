# -*- coding: utf-8 -*-
import scrapy
import re

class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/971697873/profile']

    def start_requests(self):
        cookies = "anonymid=k1yr4manyg6tj2; depovince=GW; jebecookies=053f9043-a81c-4290-8855-81fe93d64ae0|||||; _r01_=1; JSESSIONID=abc8BJwKOjghQ5g1rxO3w; ick_login=51dfd374-2a1f-4fb7-8035-b830790b699b; _de=83FEE685AFDB1B83D580CD9BA8AE7B84; p=3765ea15b72c37b607c3d508f81447c13; first_login_flag=1; ln_uact=17642181300; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=40bfe897d358e982aa77915b938f0dc83; societyguester=40bfe897d358e982aa77915b938f0dc83; id=971697873; xnsid=17a29139; loginfrom=syshome; jebe_key=d0ff8e82-e506-4ad7-9add-d82f85f5cb79%7C6e0aab37382a274eb54a921a5e63d8e0%7C1571561501178%7C1%7C1571561505419; wp_fold=0"
        cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response):
        print(re.findall("李想",response.body.decode()))
        yield scrapy.Request(
            "http://www.renren.com/971697873/profile?v=info_timeline",
            callback=self.parse_detial
        )

    def parse_detial(self,response):
        print(re.findall("李想", response.body.decode()))
