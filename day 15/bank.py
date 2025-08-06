class Bank:  
    def create_A(self,name,acc_no):
        self.name=name
        self.acc_no=acc_no
        self.balance=0
    def deposite(self,Acc_no,dp_amount):
        if self.acc_no==Acc_no:
            self.balance+=dp_amount
            print(self.balance)
    def withdraw(self,acc_no,wd_amount):
        if self.acc_no==acc_no:
            self.balance-=wd_amount
            print('withdraw:',self.balance)


obj=Bank()
obj.create_A("ganesh",1234)
obj.deposite(1234,132)
obj.withdraw(1234,20)
