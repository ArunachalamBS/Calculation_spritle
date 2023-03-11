# functions defined for operators +,-,*,//
def plus(x):
    return str(x)+'+'
def minus(x):
    return str(x)+'-'
def times(x):
    return str(x)+'*'
def divided_by(x):
    return str(x)+'//'
# functions defined for numbers from 0 to 9:

def zero(x=0):
    if x==0:
        return x
    else:
        if x[1]=='+':
            return 0+int(x[0])
        elif x[1]=='-':
            return 0-int(x[0])
        elif x[1]=='*':
            return 0*int(x[0])
        else:
            return 0//int(x[0])

def one(x=1):
    if x==1:
        return x
    else:
        if x[1]=='+':
            return 1+int(x[0])
        elif x[1]=='-':
            return 1-int(x[0])
        elif x[1]=='*':
            return 1*int(x[0])
        else:
            return 1//int(x[0])

def two(x=2):
    if x==2:
        return x
    else:
        if x[1]=='+':
            return 2+int(x[0])
        elif x[1]=='-':
            return 2-int(x[0])
        elif x[1]=='*':
            return 2*int(x[0])
        else:
            return 2//int(x[0])


def three(x=3):
    if x==3:
        return x
    else:
        if x[1]=='+':
            return 3+int(x[0])
        elif x[1]=='-':
            return 3-int(x[0])
        elif x[1]=='*':
            return 3*int(x[0])
        else:
            return 3//int(x[0])

def four(x=4):
    if x==4:
        return x
    else:
        if x[1]=='+':
            return 4+int(x[0])
        elif x[1]=='-':
            return 4-int(x[0])
        elif x[1]=='*':
            return 4*int(x[0])
        else:
            return (4)//(int(x[0]))

def five(x=5):
    if x==5:
        return x
    else:
        if x[1]=='+':
            return 5+int(x[0])
        elif x[1]=='-':
            return 5-int(x[0])
        elif x[1]=='*':
            return 5*int(x[0])
        else:
            return 5//int(x[0])

def six(x=6):
    if x==6:
        return x
    else:
        if x[1]=='+':
            return 6+int(x[0])
        elif x[1]=='-':
            return 6-int(x[0])
        elif x[1]=='*':
            return 6*int(x[0])
        else:
            return 6//int(x[0])

        
def seven(x=7):
    if x==7:
        return x
    else:
        if x[1]=='+':
            return 7+int(x[0])
        elif x[1]=='-':
            return 7-int(x[0])
        elif x[1]=='*':
            return 7*int(x[0])
        else:
            return 7//int(x[0])

def eight(x=8):
    if x==8:
        return x
    else:
        if x[1]=='+':
            return 8+int(x[0])
        elif x[1]=='-':
            return 8-int(x[0])
        elif x[1]=='*':
            return 8*int(x[0])
        else:
            return 8//int(x[0])

def nine(x=9):
    if x==9:
        return x
    else:
        if x[1]=='+':
            return 9+int(x[0])
        elif x[1]=='-':
            return 9-int(x[0])
        elif x[1]=='*':
            return 9*int(x[0])
        else:
            return 9//int(x[0])

           
            
# sample program output:       
print(seven(minus(three())))# output 4
print(six(times(seven())))  # output 42
print(nine(divided_by(three()))) # output 3
print(three(plus(seven())))  # output 10
