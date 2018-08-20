#Ques1
List=[1,2,3,4]
List.reverse()
print("Reverse List:",List)

#Ques2
String="My Name Is Arsh Verma"
upper=""
for letter in String:
    if letter.isupper():
        upper=upper+letter+','
print(upper)

#Ques3
value=input("Enter value:")
x=value.split(',')
y=[]
for i in x:
    y.append(int(i))
print(y)


#Ques4
String="naman"
rev=String[::-1]
if String==rev:
    print('It is a palindrome')
else:
    print('It is not a palindrome')

#Ques5
import copy as c
x=[1,2,[3,4],5]
y=c.deepcopy(x)
x[2][1]='one'
x[1]='two'
print(x)
print(y)

"""
The difference between shallow copy and deep copy:
SHALLOW COPY
1:Shallow copy creates a new object and then copy the non static fields of the current object to the new object.
2:A shallow copy of an object is a new object whose instance variables are identical to the old object.

DEEP COPY
1:Deep copy creates a new object and then copy the non-static fields of the current object to the new object.
2: A deep copy of an object is a new object with entirely new instance variables, it does not share objects with the old.

"""












