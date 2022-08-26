# Q28.Write a Python program to convert a list into a nested dictionary of keys.
# num_list = [1, 2, 3, 4]
# Sample output:
# {1: {2: {3: {4: {}}}}}
num_list = [1, 2, 3, 4]
v={}
for i in num_list:
    v={num_list[-i]:v}
print(v)

