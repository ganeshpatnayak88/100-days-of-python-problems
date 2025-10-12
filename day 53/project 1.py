class BankAccount():
    
    def __init__(self,name,balance=0):
        self._name=name
        self.__balace=balance
        self.is_active=True
        self.check_book_req=False
    
    # Check Balance    
    def check_balance(self):
        if self.is_active:
            print(f"\nYour Balance : {self.__balace}")
        else:
            print("\nYour Account is Freeze or Inactive")
    
    # Withdraw_Balance
    def Withdraw_Balance(self,with_amt):
        if self.__balace > with_amt and self.is_active:
            self.__balace -= with_amt
            print(f"\n{with_amt} debited successfully , your current balance : {self.__balace}")
        elif self.__balace<with_amt:
            print("\nInsufficient Balance")
        elif not self.is_active:
            print("\nYour Account is Freeze or Inactive")
    
    # Deposite_Amount
    def Deposite_Amount(self,Dep_Amt):
        
        if self.is_active and Dep_Amt>0:
            self.__balace+=Dep_Amt
            print(f"\n{Dep_Amt} Deposited Successfully , Your current balance : {self.__balace} ")
        elif Dep_Amt<=0:
            print("\nDeposited Amount Should be Greaater than Zero !!!!")
        else:
            print("\nYour Account is Freeze or Inactive")
    
    # Cheque_Book_Request
    def Cheque_Book_Request(self):
        if not self.check_book_req:
            self.check_book_req=True
            print("Approve request")
        else:
            print("already requested")
    
    # Freeze_Account
    def Freeze_Account(self):
        if self.is_active:
            self.is_active=False
            print("Account Frozen Successfully")
        else:
            print("account already frozen")
    
    # Unfreeze_Account
    def Unfreeze_Account(self):
        if not self.is_active:
            print("Account Unfrozen Successsfully")
        else:
            print("account already active")

    # Request_Loan
    def Request_Loan(self,Loan_amt):
        if (self.is_active) and (Loan_amt < 500000) and (self.__balace <= Loan_amt):
            self.__balace+=Loan_amt
            print("Approve loan")
        elif not self.is_active:
            print("Your Account is Freeze or Inactive")
        else:
            print("Loan Declined Due to Amount Issues")

            
# Savings Account
class SavingsAccount(BankAccount):
    
    # initializer
    def __init__(self, name, balance,pin,daily_limit=100000):
        super().__init__(name, balance)
        self.__pin=pin
        self.limit=daily_limit
        self.atm_request=False
    
    # Check Balance
    def check_balance(self,pin):
        if self.__pin==pin:
            return super().check_balance()
        elif self.__pin != pin:
            print("\nIncorrect Pin Entered")
            return
    
    # Withdraw Funds
    def Withdraw_Balance(self,pin,With_amt):
        
        if self.limit < With_amt:
            print("\nDaily transaction limit reached")
            return
        elif self.__pin==pin :
            return super().Withdraw_Balance(With_amt)
        else:
            print("\nIncorrect Pin Entered")
            return
    
    # Deposit Funds      
    def Deposite_Amount(self,pin,Dep_Amt):
        
        if self.__pin==pin:
            return super().Deposite_Amount(Dep_Amt)
        else:
            print("\nIncorrect Pin Entered")
    
    # ATM Card Request     
    def ATM_Card_Request(self):
        if not self.ATM_Card_Request:
            self.atm_request=True
            print("Approve Atm for this Holder")
            return
        else:
            print("already requested")
            return
    
    # Cheque_Book_Request
    def Cheque_Book_Request(self):
        return super().Cheque_Book_Request()
    
    # Freeze_Account 
    def Freeze_Account(self):
        return super().Freeze_Account()
    
    #Unfreeze_Account
    def Unfreeze_Account(self):
        return super().Unfreeze_Account()

 
# Bussiness Account   
class BusinessAccount(BankAccount):
    def __init__(self, name, balance=0):
        # self.__bal=balance
        # print(self.__bal)
        super().__init__(name, balance)
    
    # Withdraw Funds   
    def check_balance(self):
        return super().check_balance()
    
    # Withdraw_Balance
    def Withdraw_Balance(self,With_amt):
        return super().Withdraw_Balance(With_amt)
    
    # Deposite_Amount
    def Deposite_Amount(self,Dep_amt):
        return super().Deposite_Amount(Dep_amt)
    
    # Request_Loan
    def Request_Loan(self,Loan_amt):
        return super().Request_Loan(Loan_amt)
    
    # Cheque_Book_Request    
    def Cheque_Book_Request(self):
        return super().Cheque_Book_Request()
        
    

# ---------------------- Savings Account ----------------------
obj=SavingsAccount("Teja",5000,1234)
print(obj._name)
# print(obj.check_balance(1234))
# obj.Withdraw_Balance(1234,With_amt=10000)
# obj.Deposite_Amount(1234,123)
# obj.ATM_Card_Request()
# obj.Cheque_Book_Request()
# obj.Freeze_Account()
# obj.Unfreeze_Account()


#  ---------------------- Bussiness Account ----------------------

# obj2=BusinessAccount("10000 coders",8000)
# obj2.check_balance()
# obj2.Withdraw_Balance(With_amt=10000)
# obj2.Deposite_Amount(15000)
# obj2.Request_Loan(400000)
# obj2.Cheque_Book_Request()



print(f"\nThanks for using..................!\n")

