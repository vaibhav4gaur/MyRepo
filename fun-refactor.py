def str_concatenate():
    str1 = "Fill"
    str2 = " up Complaint"
    print(str1 + str2)

str_concatenate()

def mul(a,b):
    print(a*b)
mul(9,6)

def mul1(a,b):
    c = a * b
    return c
mul(7,6)


ans = mul1(5,7)
print(ans)


def mult(a,b):
   c = a * b
   return c

result = mult(2,'Vaib ')
print(result)


# Function is Addition of Number
def add(a):
    print(a+1)
    print(a-1)
    print(a*3)
add(3)
add(14)
add(6)

def add(a,b):
    return (a+b)
def square(c):
    return (c*c)

result = square(add(4,5))
print(result)

# Modules
import math
print(math.pi)

from math import *
print(pi)



# Recursion

import sys
sys.setrecursionlimit(2000)

n = 0

def python():
    global n
    n = n + 1
    print('python',n)
    python()

python()




#Factorial
# 0! = 1
# 1! = 1
# 2! = 2
# 3! = 3*2*1
# 4! = 4*3*2*1
# 5! = 5*4*3*2*1

def factorial(n):
    if n<2: # for 0 ,1 is always less than 2 and return's the number is 1
        return 1
    else:
        return n * factorial(n-1) # 1,2,3, , , , (n-1)....

result = factorial(7)
print(result)
n=1 # global variable

def fun():
    global n # local variable convert to global variable
    n = 2 # local variable
    print('in',n) # input number in local variable

fun()

print('out',n) # output number in global variable
n = int(input("Enter a number: "))

def fact(n):
    if n == 0:
        return 1
    else :
        output = 1
        for i in range(1,n+1):
          output *= i
        return output
fact_num = fact(n)
print(f"Factorial  of {n} is : {fact_num}")
