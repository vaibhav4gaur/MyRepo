'''class const_dest:
    x=0

    def __init__(self,color,type):
        self.color = color
        self.type = type
        print("Constructor")

    def __del__(self):
        print("Destructor")

count = const_dest("black","Ferrari")
print(count.color)
print(count.type)

count_1 = const_dest("red","Volkswagon")
print(count_1.color)
print(count_1.type)'''

def name(name):
    print("Hi",name)

n = name("Sam")
n = name("Jim")

class name:
    x=0
    name = ""

    def __init__(self,z):
        self.name = z
        print("Hi",z)
        
n = name("Jim")
n = name("Sam")
