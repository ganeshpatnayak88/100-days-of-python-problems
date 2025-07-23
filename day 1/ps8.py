# 8.	words = ["level", "python", "madam", "world", "racecar"] print palindrome words  


words = ["level", "python", "madam", "world", "racecar"]
l=[i for i in words if i[::-1]==i]
print(l)