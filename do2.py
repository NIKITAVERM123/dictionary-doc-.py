# Q2. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c'
a='w3resource'
b={}
for i in a:
    c=0
    for j in a:
        if i==j:
            c=c+1
            b[i]=c
print(b)