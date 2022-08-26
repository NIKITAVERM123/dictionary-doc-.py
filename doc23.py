# Q23.Write a Python program to find the highest 3 values of corresponding keys in a dictionary.6:8
# a={1:3,4:7,6:8,7:4,10:12}
# max=0
# for i in a:
#     if a[i]>max:
#         max=a[i]
# print(max)
# max1=0
# for i in a:
#     if a[i]>max1:
#         if a[i]!=max:
#             max1=a[i]
# print(max1)
# max2=0
# for i in a:
#     if a[i]>max2:
#         if a[i]!=max and a[i]!=max1:
#             max2=a[i]
# # print(max2)
# a=["a","b"]
# b=[1,2]
# c={}
# for i in a:
#     for j in i:
#         for k in b:
#          c.update({i:{j:k}})
# print(c)

a={"a":1,"b":4}
a.pop("a")
print(a)
a.copy()
print(a)
s=a.values()
print(s)