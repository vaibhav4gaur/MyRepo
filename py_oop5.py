#Types of Inheritance
#Single Level of Inheritance
#Multi Level of Inheritance
#Multiple

# Single Inheritance

class A:
    def state_1(self):
        print("State_1 present")
    def state_2(self):
        print("State_2 present")
    def state_3(self):
        print("State_3 present")

class B:
    def state_4(self):
        print("State_4 present")
    def state_5(self):
        print("State_5 present")


# Multi-Level of Inheritance

class C(A,B):                                # class C(A,B)  ---> Multple Inheritant value formation
    def state_6(self):
        print("State_6 present")
    def state_7(self):
        print("State_7 present")

# Single Inheritance
a = A()
a.state_3()
a.state_1()

b = B()
b.state_5()
b.state_4()

# Multi-level-Inheritance
c = C()
c.state_7()
c.state_1()
c.state_4()


# Multiple - Inheritance
c = C()
c.state_3()
c.state_1()