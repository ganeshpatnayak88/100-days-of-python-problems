# 10. Find if a number is Armstrong or not.
h=int(input('enter a num:-- '))
a=0
for i in str(h):
    a+=int(i)**3
if h==a:
    print('it is arm')
else:
    print('it is arm prime')