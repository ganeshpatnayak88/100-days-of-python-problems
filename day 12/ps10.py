# Create a list of words with length > 3 from a sentence.
h="pablo is good boy"
l=h.split()
j=[i for i in l if len(i)>3]
print(j)