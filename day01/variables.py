"""
    Java variables:
    String varName = data;

    Python variables:
    varName = data;
"""

name_of_student = "Efe"
print(type(name_of_student))
print(name_of_student)

name_of_student = 3.5
print(type(name_of_student))
print(name_of_student)

name_of_student = True
print(type(name_of_student))
print(name_of_student)


print("---")

s = "35"

num = int(s)

print(num)
print(type(num))

#concatenation
age = 20
print("I am {} years old".format(age))
print(f"I am {age} years old")
#f stands for format function

print("--Operators---------------------------------")

str1 = "python programming"

print("python" in str1)

print(True and True)  #&&
print(False or True)  #||

s1 = "Java"
s2 = "Java"

print(s1 is s2) #used for checking if two reference variables are referencing to the same objects (== in java)

"""
in Java;

String s1 = "Java";
String s2 = "Java";

String s3 = new String("Java");

s1 == s2 ---> true
s1 == s3 ---> false
"""



