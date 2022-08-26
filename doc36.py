# Q36.Write a Python program to match key values in two dictionaries. 
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y
a={'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
for i in a:
    for j in a:
        if i==j:
           print("yes key1:1 is present in both dic")
       