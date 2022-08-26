# Q18.Write a Python program to get the maximum and minimum value in a dictionary
a={"a":1,"b":4,"j":6}
max=0
max1=0
for i in a:
    if a[i]>max:
        max=a[i]
min=0
for i in a:
    if  a[i]<max:
        if a[i]>min  and a[i]!=max and a[i]!=max1:
            min=a[i]
# print(min)
print(max)
print(min)