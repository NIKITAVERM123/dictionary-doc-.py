# Write a Python program to sum all the items in a dic
# a={1:20,"d":45,"l":45}
# s=0
# for i in a:
#     s=s+a[i]
# print(s)

# nasted sum 
a={"o":7,"g":4,"h":{"p":3},"u":4}
s=0
for i in a:
    if type(a[i])==dict:
        for j in a[i]:
            s=s+a[i][j]
    else:
        s=s+a[i]
print(s)