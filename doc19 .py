from binascii import a2b_base64


student_data = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}
# l=[]
# a={}
# for i,j in student_data.items():
#     if j not in l:
#         l.append(j)
# print(l)
a=[]
for i in student_data:
  a.append(student_data[i])
  for j in range (len(a)):
        if j not in a:
              a.append(j)
print(a)