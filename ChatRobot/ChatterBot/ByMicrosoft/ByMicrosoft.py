# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from settings import Microsoft

'''
关于获取微软的user access token请参考以下的文档
https://docs.botframework.com/en-us/restapi/directline/
'''

chatbot = ChatBot(
    'MicrosoftBot',
    directline_host = Microsoft['directline_host'],
    direct_line_token_or_secret = Microsoft['direct_line_token_or_secret'],
    conversation_id = Microsoft['conversation_id'],
    input_adapter='chatterbot.input.Microsoft',
    output_adapter='chatterbot.output.Microsoft',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

chatbot.train('chatterbot.corpus.english')

# 是的，会一直聊下去
while True:
    try:
        response = chatbot.get_response(None)

    # 直到按ctrl-c 或者 ctrl-d 才会退出
    except (KeyboardInterrupt, EOFError, SystemExit):
        break