# Q31.. Write a Python program to get the top three items in a shop. Go to the editor
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# # item3 41.3
a= {"item1": 45.50, "item2":35, "item3": 41.30, "item4":55, "item5": 24}
max=0
for i in a:
    if a[i]>max:
        max=a[i]
print(max)
max1=0
for i in a:
    if a[i]>max1:
        if a[i]!=max:
            max1=a[i]
print(max1)
max2=0
for i in a:
    if a[i]>max2:
        if a[i]!=max and a[i]!=max1:
            max2=a[i]
print(max2)
