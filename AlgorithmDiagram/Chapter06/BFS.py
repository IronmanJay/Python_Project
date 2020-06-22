from collections import deque

# 生成图关系，用芒果经销商来举例
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


# 判断这个人是不是芒果经销商
def person_is_seller(name):
    return name[-1] == 'm'


# 广度优先搜索
def BFS(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []  # 这个数组用于记录检查过的人
    while search_queue:  # 只要队列不为空
        person = search_queue.popleft()  # 就取出其中的第一个人
        if not person in searched:  # 仅当这个人没检查过时才检查
            if person_is_seller(person):  # 检查这个是否是芒果经销商
                print(person + " is a mango seller!")  # 是芒果经销商
                return True
            else:
                search_queue += graph[person]  # 不是芒果经销商。将这个人的朋友都加入搜索队列
                searched.append(person)  # 将这个人标记为检查过
    return False  # 如果到达了这里，就说明队列中没人是芒果经销商


# 测试
BFS("you")
