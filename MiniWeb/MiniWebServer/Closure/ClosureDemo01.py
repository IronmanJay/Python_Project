
def line_(k,b):
    def create_y(x):
        print(k*x+b)
    return create_y

line = line_(1,2)
line(0)
line(1)
line(2)
print("*"*50)
line = line_(11,22)
line(0)
line(1)
line(2)
