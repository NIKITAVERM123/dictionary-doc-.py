
# Q30.Write a Python program to remove spaces from dictionary keys.
# Original dictionary:  {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# New dictionary:  {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']} 
a={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
g={}
for i in a:
    v=" "
    for j in i:
        if j==" ":
            pass
        else:
            v=v+j
    g[v]=a[i]
print(g)
