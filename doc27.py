# # Q27.Write a Python program to count the values associated with key in a dictionary.
student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
name=input("enter the number:")
c=0
for i in student:
    for j in i :
        if j == name:
         c+=i[j]
print(c)



