from chatterbot import ChatBot
import logging


'''
这是一个使用Ubuntu语料构建聊天机器人的例子
'''

# 允许打日志
logging.basicConfig(level=logging.INFO)

chatbot = ChatBot(
    'Example Bot',
    trainer='chatterbot.trainers.UbuntuCorpusTrainer'
)

# 使用Ubuntu数据集开始训练
chatbot.train()

# 我们来看看训练后的机器人的应答
response = chatbot.get_response('How are you doing today?')
print(response)