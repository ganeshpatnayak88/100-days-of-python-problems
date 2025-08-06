class b:
    def method(self,*s):  #not give tupple because tupple haS NO range
        T=0
        for i in s:
            T+=i
        print(T)
obj=b()
obj.method(10,20,30)