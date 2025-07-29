import random as r
import time

class qnpaper_generator:
    def __init__(self):
        self.num1 = r.randint(1,20)
        self.num2 = r.randint(1,20)
        self.op=r.choice(["+","-","*","/","//","%","**","==","!=",">","<",">=","<="])
    # i can use a decorator here to print out every qns     
    def qn_generator(self):
        expressions = {
            "+" : f"{self.num1}+{self.num2}",
            "-" : f"{self.num1}-{self.num2}",
            "*" : f"{self.num1}*{self.num2}",
            "/" : f"{self.num1}/{self.num2}",
            "//" : f"{self.num1}//{self.num2}",
            "%" : f"{self.num1}%{self.num2}",
            "**" : f"{self.num1}**{self.num2}",
            "==" : f"{self.num1}=={self.num2}",
            "!=" : f"{self.num1}!={self.num2}",
            ">" : f"{self.num1}>{self.num2}",
            "<" : f"{self.num1}<{self.num2}",
            ">=" : f"{self.num1}>={self.num2}",
            "<=" : f"{self.num1}<={self.num2}"
            }
        return expressions.get(self.op)

    
def timmer(func):
    def warpper():
        print(" cleanning window ")
        func()
        print("Your time is up")
    return warpper()
def qn_display(func):
    def warpper():
        print("I have generate a new question for you")
        func()
        for i in range(1,4):
            time.sleep(1)
            print(f"{i}          ",end="\r")
        print("Your times starts now")
        @timmer
        def time_d():
            for i in range(10,0,-1):
                time.sleep(1)
                print(f"{i}          ",end="\r")
    return warpper()

def asking_qqn():
    qn1= qnpaper_generator()
    @qn_display
    def qns():
        
# qnpaper decorator display vanera auta function banauxu tesma yo call bhayeci warper call huncha ok 
# proper visual pleasing huncha vanam na 
        print(qn1.qn_generator()) # i can keep this in display function
    return qn1.qn_generator()   
        
        
    


def take_input_check(a):
    if isinstance(a,int):  
        print("valid input")
        a=int(a)
    elif isinstance(float(a),float):        
        print("valid input")
        a=float(a)
    else:
        raise ValueError
    return a
def take_input():
    a = input("Type your ans (if comparion is done give type either 1 for true and 0 for  false ) = ")
    try:
        a= take_input_check(a)
    except ValueError:
        print("plz enter valid input")
    return a

def result_compare(expression, inp):
    d = eval(expression)
    if  d == inp:        
        print("correct")
    else:
        print("Incorrect ans")
