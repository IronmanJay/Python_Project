import re
# string = '<p><div><span>猪八戒</span></div></p>'
# pattern = re.compile(r'<(\w+)><(\w+)>\w+</w+></w+>')
# string = '<div>赵越</div></div></div>'
# pattern = re.compile(r'<div>.*?</div>')
string = '''hate is a beautiful feel
love you very much
love she
love her'''
pattern = re.compile(r'^love',re.M)
ret = pattern.search(string)
print(ret)