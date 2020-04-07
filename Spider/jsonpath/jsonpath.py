import json
lt = [
    {'name': '王宝强','age' : '30'},
    {'name': '周杰伦', 'age': '36'},
    {'name': '张学友', 'age': '45'},
    {'name': '郭富城', 'age': '50'},
]
string = json.dumps(lt)
obj = json.loads(string)
json.dump(lt,open('json.txt','w',encoding='utf8'))
newobj = json.load(open('json.txt','r',encoding='utf8'))