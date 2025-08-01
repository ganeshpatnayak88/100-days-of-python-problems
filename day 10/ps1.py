# Tuple of cube of odd numbers from 1 to 15.
a=tuple(i**3 for i in range(1,16) if i%2!=0 )
print(a)