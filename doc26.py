# # Write a Python program to print a dictionary in table format.
# # my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}

# # Sample Output:

# C1 C2 C3                                                                                                      
# 1 5 9                                                                                                         
# 2 6 10                                                                                                        
# 3 7 11
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
s=[]
for i in my_dict:
    print(i,end=" ")
    s.append(my_dict[i])
print()
for i in range(len(s)):
    for j in range(len(s[i])):
        print(s[j][i],end=" ")
    print()






 

  




