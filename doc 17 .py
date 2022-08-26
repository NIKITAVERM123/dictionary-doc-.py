# # Q17.Write a Python program to sort a dictionary by 
a={"a":7,"b":8,"e":6,"d":9}
e=[]
for i in a:
    e.append(a[i])
    for i  in range (len(e)):
        for j in range (len(e)):
            if e[i]<e[j]:
                tm=e[i]
                e[i]=e[j]
                e[j]=tm
print(e)
e=[]
for i in a:  
 e.append(a[i])
 for i in range(len(e)):
    for j in range(len(e)):
        if e[i]<e[j]:
            tm=e[i]
            e[i]=e[j]
            e[j]=tm
print(e)            