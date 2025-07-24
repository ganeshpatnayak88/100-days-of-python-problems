
# Replace the middle element in a list with the number 100.
# method 1:
list=[10,20,30,40,50,60,70,80,90]
list[4]=100
print(list)
# mrthod 2:
if len(list)%2!=0:
    list[len(list)//2]=100
else:
    list[len(list)//2-1]=100
print(list)