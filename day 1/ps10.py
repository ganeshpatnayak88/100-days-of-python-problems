# 10.	 From ["cat", "dog", "parrot", "cow"], create a tuple of words with more than 3 letters
h=["cat", "dog", "parrot", "cow"]
new=[]
for i in h:
    if len(i)>3:
        new.append(i)
print(new)