# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import logging

"""
反馈式的聊天机器人，会根据你的反馈进行学习
"""

# 把下面这行前的注释去掉，可以把一些信息写入日志中
# logging.basicConfig(level=logging.INFO)

# 创建一个聊天机器人
bot = ChatBot(
    'Feedback Learning Bot',
    storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter'
)

DEFAULT_SESSION_ID = bot.default_session.id


def get_feedback():
    from chatterbot.utils import input_function

    text = input_function()

    if 'Yes' in text:
        return True
    elif 'No' in text:
        return False
    else:
        print('Please type either "Yes" or "No"')
        return get_feedback()


print('Type something to begin...')

# 每次用户有输入内容，这个循环就会开始执行
while True:
    try:
        input_statement = bot.input.process_input_statement()
        statement, response = bot.generate_response(input_statement, DEFAULT_SESSION_ID)

        print('\n Is "{}" this a coherent response to "{}"? \n'.format(response, input_statement))

        if get_feedback():
            bot.learn_response(response,input_statement)

        bot.output.process_response(response)

        # 更新chatbot的历史聊天数据
        bot.conversation_sessions.update(
            bot.default_session.id_string,
            (statement, response, )
        )

    # 直到按ctrl-c 或者 ctrl-d 才会退出
    except (KeyboardInterrupt, EOFError, SystemExit):
        break