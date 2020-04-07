from nltk import *
import random

# 打招呼
greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']
# 回复打招呼
random_greeting = random.choice(greetings)
# 对于“假期”的话题关键词
question = ['break','holiday','vacation','weekend']
# 回复假期话题
responses = ['It was nice! I went to Paris',"Sadly, I just stayed at home"]
# 随机选一个回
random_response = random.choice(responses)

# 机器人跑起来
while True:
    userInput = input(">>> ")
    # 清理一下输入，看看都有哪些词
    cleaned_input = word_tokenize(userInput)
    # 这里，我们比较一下关键词，确定他属于哪个问题
    if  not set(cleaned_input).isdisjoint(greetings):
        print(random_greeting)
    elif not set(cleaned_input).isdisjoint(question):
        print(random_response)
    # 除非你说“拜拜”
    elif userInput == 'bye':
        break
    else:
        print("I did not understand what you said")