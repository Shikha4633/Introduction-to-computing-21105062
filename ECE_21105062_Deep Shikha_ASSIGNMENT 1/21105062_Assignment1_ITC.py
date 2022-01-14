# Assignment 1


# 1st program

print()
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))
total = num1+num2+num3
avg = total/3
print("avg of numbers= ",avg)


# 2nd program

print()
tax_rate = 0.2                                              #20%
sd = 10000                                                  #Standard Deduction
dd = 3000                                                   #Dependent Deduction
gi = int(input("enter Gross Income: "))                     #Gross Income
no_of_dependent = int(input("enter No.Of Dependent: "))
taxable_income = gi-sd-(dd*no_of_dependent)
print("Taxable Income: ",taxable_income)
tax = taxable_income * tax_rate
print("Tax: ",tax)


# 3rd program

print()
student = ["SID","Name","Gender","Department Name", "CGPA"]
print("Student: ",student)
student = [21105062,"Deep Shikha","F","ECE",9.8]
print("student: ",student)


# 4th program

print()
Marks = [76,95,84,67,55]
print("Marks Before Sorting: ",Marks)
Marks.sort()
print("Marks After Sorting: ",Marks)


# 5th program

print()
Color = ["Red","Green","White","Black","Pink","Yellow"]
print("Color",Color)
Color.pop(3)
print("(a) Color",Color)

Color = ["Red","Green","White","Black","Pink","Yellow"]
Color[3:5] = ["Purple"]
print("(b) Color",Color)
