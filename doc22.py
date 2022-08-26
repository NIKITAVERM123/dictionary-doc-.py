# Q22. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Go to the editor
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd
a={'1':['a','b'], '2':['c','d']}
b=a["1"]
k=a["2"]
for i in b:
    for j in k:
        print(i+j)



    # b.append(a[i])
    # print(a[i]*a[i])
