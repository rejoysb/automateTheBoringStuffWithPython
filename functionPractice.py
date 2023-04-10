import random

def hello():
     print("hello world")

hello()
hello()

#def statement with input parameter

def helloWorld(name):

    print("hello world " + name)


helloWorld("rejoy")

def randomNum(num):

    if(num==1):
        return "number One"
    elif(num==2):
        return "number two"
    elif(num==3):
        return "number three"


r=random.randint(1,3)
print(randomNum(r))

#so if there is a function without return value
#python adds a return null

#try and except in python.

def tryCatch(num):
    try:
        return 42/num
    except ZeroDivisionError:
        print("error: invalid Argument")

tryCatch(0)