#!/usr/bin/python
# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("ChineseChatBot")
chatbot.set_trainer(ChatterBotCorpusTrainer)

# 使用中文语料库训练它
chatbot.train("chatterbot.corpus.chinese")

# 开始对话
while True:
    print(chatbot.get_response(input(">")))