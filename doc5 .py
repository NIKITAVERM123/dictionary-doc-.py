# Write a Python program to sort (ascending and descending) a dictionary by value.
# Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order 
a={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
b=[]
for i in a:
    b.append(a[i])
    for i in range(len(b)):
        for j in range(len(b)):
            if b[i]<b[j]:
                tm=b[i]
                b[i]=tm
                tm=b[i]
print(b)