class vegetable:

    def __init__(self,carrots,beans):
        self.carrots = carrots
        self.beans = beans

    def __add__(self,others):
        carrots = self.carrots + others.carrots
        beans = self.beans + others.beans
        return vegetable(carrots,beans)

v1 = vegetable(5,8)
v2 = vegetable(8,9)
v3 = v1 + v2
print(v3.carrots)
