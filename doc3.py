# 3.Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample input ( n = 5) :
# Output :
# 
b={}
for i in range (5):
    a=int(input("enter the number :"))
    c=a*a
    b.update({a:c})
print(b)
