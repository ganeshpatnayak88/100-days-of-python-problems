# Generate a tuple of prime numbers between 10 to 50 using comprehension.
d=tuple(i for i in range(10,51) for j in range(i+1,51) if i%j==0 )
print(d)