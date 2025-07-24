# Create a list from user input of 5 numbers.
# method 1:
a=int(input('enter numbers '))
b=str(a)
x=[]
for i in b:
    x.append(i)
print(x)

# method 2:
x=[]
for i in range(1,6):
    a=(int(input('enter a num:-')))
    x.append(a)
print(x)