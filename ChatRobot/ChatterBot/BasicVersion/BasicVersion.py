# -*- coding: utf-8 -*-
from chatterbot import ChatBot


# 构建ChatBot并指定Adapter
bot = ChatBot(
    'Default Response Example Bot',
    storage_adapter='chatterbot.storage.JsonFileStorageAdapter',#存储的Adapter
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'#回话逻辑
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',#回话逻辑
            'threshold': 0.65,#低于置信度，则默认回答
            'default_response': 'I am sorry, but I do not understand.'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer'#给定的语料是个列表
)

# 手动给定一点语料用于训练
bot.train([
    'How can I help you?',
    'I want to create a chat bot',
    'Have you read the documentation?',
    'No, I have not',
    'This should help get you started: http://chatterbot.rtfd.org/en/latest/quickstart.html'
])

# 给定问题并取回结果
question = 'How do I make an omelette?'
print(question)
response = bot.get_response(question)
print(response)

print("\n")
question = 'how to make a chat bot?'
print(question)
response = bot.get_response(question)
print(response)