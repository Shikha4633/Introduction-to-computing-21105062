#ASSIGNMENT 2


#1st Program

print("Ques.1}\n\n")
a=input("Type Your String: ")        #a=String
#a is the string enter by user

#part (a)
length=len(a)
print("\na. Length of the entered string is: ",length, "\n" )

#part (b)
rev=(a[::-1])                        #Reversed
print("b. Reversed Order of String: ",rev, "\n")

#part (c)
new_str=a[10:26]
print("c. New String is: ", new_str, "\n")

#part (d)
X= a.replace(new_str, "object oriented")
print("d. Repaced String is : ",X, "\n")

#part (e)
sub_index=a.index("a")               #Substring
print("e. Index of Substring 'a' is : ",sub_index, "\n")

#part (f)
no_space=a.replace(" ","")
print("Your String with no spaces",no_space)



#2nd Program

print("\n\n\n\n\nQues.2}\n\n")

#Data Entry By User

Name=input("Enter Your Name: ")
SID=int(input("Enter YOur SID: "))
Dept=input("Enter Your Department: ")
CG=float(input("Enter Your CGPA: "))

print("Hey, %s Here!\n"
      "My SID is %d\n"
      "I am from %s Departmentand My CGPA is %f" %(Name,SID,Dept,CG))



#3rd Program

print("\n\n\n\n\nQues.3}\n\n")
a=56
b=10

print("a= ",a,"\n"
      "b= ",b)

#part (a)
print("a. a&b= ",a & b,"\n")

#part (b)
print("b. a|b= ",a|b,"\n")

#part (c)
print("c. a^b= ",a^b,"\n")

#part (d)
print("d. Left Shift of 'a' by 2 bits= ",a<<2, "\n"
      "Left Shift od 'b' by 2 bits= ",b<<2)

#part (e)
print("e. Right Shift of 'a' by 2 bits= ",a>>2, "\n"
      "Right Shift od 'b' by 4 bits= ",b>>4)



#4th Program

print("\n\n\n\n\nQues.4}\n\n")

print("Enter three numbers to find the greatest number:- ")

#Number to be enter by the user
a=float(input("First Number= "))
b=float(input("Second Number= "))
c=float(input("Third Number= "))

if a>=b and a>=c:
    greatest=a
elif b>=c:
    greatest=b
else:
    greatest=c

print("\nGreatest Number is: ",greatest)



#5th Program

print("\n\n\n\n\nQues.5}\n\n")

print("Enter a sentence to know wheteher it contains 'name' or not:-\n")

Sen= input("Enter your sentence: ")    #Sentence
Remark="Does this sentence contain word 'name' : "

if "name" in Sen:
    print("\n",Remark,"Yes")
else:
    print("\n",Remark,"No")



#6th Program

print("\n\n\n\n\nQues.6}\n\n")

print("Enter three lengths to see whether a triangle can be formed from these lengths or not:-\n")
x=float(input("Length of Frist Side of Triangle= "))
y=float(input("Length of Second Side of Triangle= "))
z=float(input("Length of Third Side of Triangle= "))

if x>= y+z or y>= x+z or z>= x+y:
    print("\nNo,Triangle can't be formed.")
else:
    print("\nYes,Triangle can be formed.")
    




























    
    





































