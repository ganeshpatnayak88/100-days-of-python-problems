import mysql.connector


data=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ganesh#5522@",
    database="banking"
)

f=data.cursor()

def signup():
    name=input("enter your name:")
    password=input("enter your password:")
    f.execute("insert into bank(user_name,user_password) values(%s,%s)",(name,password))
    data.commit()
    f.execute("select * from bank where user_name=%s",(name,))
    o=f.fetchone()
    user_id,username,password=o
    print(o)
    acc_type=input("enter your type(savings/current):")
    if acc_type=="savings":
        acc_bal=10000
        f.execute("insert into accounts(user_id,acc_bal,acc_type) values(%s,%s,%s)",(user_id,acc_bal,acc_type))
        data.commit()
    if acc_type=="current":
        acc_bal=1000
        f.execute("insert into accounts(user_id,acc_bal,acc_type) values(%s,%s,%s)",(user_id,acc_bal,acc_type))
        data.commit()
    print("---sign up sucessfully---")



def login():
    username=input("enter user_name:")
    password=input("enter your pass:")
    f.execute("select * from bank where user_name=%s",(username,))
    o=f.fetchone()
    user_id,username,password=o
    f.execute("select * from accounts where user_id=%s",(user_id,))
    i=f.fetchone()
    acc_no,user_id,acc_bal,acc_type=i
    

    print("welcome to sbi bank of india")
    
    print("1.check balance")
    print("2.withdraw")
    print("3.deposite")

    choose=input("enter your option:")
    if choose=="1":
        print(acc_bal)
    if choose=="2":
        money=int(input("enter your money:"))
        if money<=acc_bal:
            f.execute("update accounts set acc_bal=acc_bal-%s where acc_no=%s",(money,acc_no))
            data.commit()
            print("debited sucessfully")
            f.execute("select * from accounts where user_id=%s",(user_id,))
            q=f.fetchone()
            acc_no,user_id,acc_bal,acc_type=q
            print(acc_bal)

        if money>acc_bal:
            print("insufficent balance")
    if choose=="3":
        money=int(input("enter your money:"))
        f.execute("update accounts set acc_bal=acc_bal+%s where acc_no=%s",(money,acc_no))
        data.commit()
        print("deposited sucessfully")
        check=input("if you check your bal(yes/no):")
        if check=="yes":
            f.execute("select * from accounts where user_id=%s",(user_id,))
            q=f.fetchone()
            acc_no,user_id,acc_bal,acc_type=q
            print(acc_bal)
        if check=="no":
            print("thankyou")

print("***sbi ki swagatham***")
print("1.sign up")
print("2.login")
print("3.exits")

choose=input("choose your option:")
if choose=="1":
    signup()
if choose=="2":
    login()
if choose=="3":
    print("thankyou for comming vist again.....")




