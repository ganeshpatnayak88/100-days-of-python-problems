# Find factors of 10 number using tuple comprehension? 
s=tuple((i,j) for i in range(1,11) for j in range(1,i) if i%j==0 )
print(s)