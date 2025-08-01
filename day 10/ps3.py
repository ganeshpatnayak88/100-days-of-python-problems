# Extract vowels from the string "comprehension" into a tuple.
d=tuple(i for i in "comprehension" if i in "AEIOUaeiou")
print(d)