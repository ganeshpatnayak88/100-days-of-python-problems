class default:
    def __init__(self,a=None,b=None,c=None,d=None):
        if a!=None and b!=None and c!=None and d!=None:
            print(a+b+c+d)
        elif a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print("enter two numbers")
obj=default(10,20)