# Q16.Write a Python program to map two lists into a dictiona
# students = ['Smith', 'John', 'Priska', 'Abhi']
# marks = [89, 53, 92, 86]
# b={}
# for i in range(len (students)):
#     b.update({students[i]:marks[i]})
# print(b)

# students_dict = dict(zip(students, marks))
# print(students_dict)
a=['sumit','ha','ras','q']
b=[1,2,3,4]
c={}
for i in range(len(a)) :
    c.update({a[i]:b[i]})
print(c)
