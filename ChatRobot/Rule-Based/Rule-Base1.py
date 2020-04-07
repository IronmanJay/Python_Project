import random

# 打招呼
greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']
# 回复打招呼
random_greeting = random.choice(greetings)
# 对于“你怎么样？”这个问题的回复
question = ['How are you?','How are you doing?']
# “我很好”
responses = ['Okay',"I'm fine"]
# 随机选一个回
random_response = random.choice(responses)

# 机器人跑起来
while True:
    userInput = input(">>> ")
    if userInput in greetings:
        print(random_greeting)
    elif userInput in question:
        print(random_response)
    # 除非你说“拜拜”
    elif userInput == 'bye':
        break
    else:
        print("I did not understand what you said")