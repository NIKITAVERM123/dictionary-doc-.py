# Q29.Write a Python program to sort a list alphabetically in a dictionary.
# a={"e":12,"v":13,"r":11,"o":4}
# e=[]
# for  i in a:
#     e.append(a[i])
#     for i in range(len(e)):
#         for j in range(len(e)):
#             if e[i]<e[j]:
#                 tm=e[i]
#                 e[i]=e[j]
#                 e[j]=tm
# print(e)

a={"e":12,"v":13,"r":11,"o":4}
e=[]
for  i in a:
    e.append(a[i])
    for i in range(len(e)):
        for j in range(len(e)):
            if e[i]<e[j]:
                tm=e[i]
                e[i]=e[j]
                e[j]=tm
print(e)
