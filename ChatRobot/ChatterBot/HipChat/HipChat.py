# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from settings import HIPCHAT

'''
炫酷一点，你可以接到一个HipChat聊天室，你需要一个user token，下面文档会告诉你怎么做
https://developer.atlassian.com/hipchat/guide/hipchat-rest-api/api-access-tokens
'''

chatbot = ChatBot(
    'HipChatBot',
    hipchat_host=HIPCHAT['HOST'],
    hipchat_room=HIPCHAT['ROOM'],
    hipchat_access_token=HIPCHAT['ACCESS_TOKEN'],
    input_adapter='chatterbot.input.HipChat',
    output_adapter='chatterbot.output.HipChat',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

chatbot.train('chatterbot.corpus.english')

# 没错，while True，会一直聊下去！
while True:
    try:
        response = chatbot.get_response(None)

    # 直到按ctrl-c 或者 ctrl-d 才会退出
    except (KeyboardInterrupt, EOFError, SystemExit):
        break