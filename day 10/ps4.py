# From ["cat", "dog", "parrot", "cow"], create a tuple of words with more than 3 letters.
f=["cat", "dog", "parrot", "cow"]
for i in f:
    if len(i)>3:
        print(tuple(i))