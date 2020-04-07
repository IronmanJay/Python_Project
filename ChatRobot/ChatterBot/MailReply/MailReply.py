
# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from settings import MAILGUN

'''
这个功能需要你新建一个文件settings.py，并在里面写入如下的配置:
MAILGUN = {
    "CONSUMER_KEY": "my-mailgun-api-key",
    "API_ENDPOINT": "https://api.mailgun.net/v3/my-domain.com/messages"
}
'''

# 下面这个部分可以改成你自己的邮箱
FROM_EMAIL = "mailgun@salvius.org"
RECIPIENTS = ["gunthercx@gmail.com"]

bot = ChatBot(
    "Mailgun Example Bot",
    mailgun_from_address=FROM_EMAIL,
    mailgun_api_key=MAILGUN["CONSUMER_KEY"],
    mailgun_api_endpoint=MAILGUN["API_ENDPOINT"],
    mailgun_recipients=RECIPIENTS,
    input_adapter="chatterbot.input.Mailgun",
    output_adapter="chatterbot.output.Mailgun",
    storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
    database="../database.db"
)

# 简单的邮件回复
response = bot.get_response("How are you?")
print("Check your inbox at ", RECIPIENTS)