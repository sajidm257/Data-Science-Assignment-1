# DATA SCIENCE ASSIGNMENT 1 SAJID ALI

# 1.Write a Python program to print the following string in a specific format (see the output).
#     Twinkle, twinkle little star,
#         how i wonder what you are!
#             Up above the world so high,
#             Like a diamond in the sky.
#         Twinkle, twinkle little star,
#         how i wonder what you are!
x = ("Twinkle, twinkle little star,\n"
"\t how i wonder what you are!\n"
"\t\tUp above the world so high,\n"
"\t\tLike a diamond in the sky. \n"
"Twinkle, twinkle little star, \n"
"\thow i wonder what you are! \n")
print(x)

# 2. Write a Python program to get the Python version you are using 
import sys
print("Python version")
print (sys.version)

# 3. Write a Python program to display the current date and time.
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

# 4. Write a Python program which accepts the radius of a circle from the user and compute the area.
from math import pi
r = float(input ("Enter radius of circle : "))
print ("Area of the circle is: " + str(pi * r**2))

# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them. 
firstName = input("Enter First Name : ")
lastName = input("Enter Last Name : ")
print (lastName + " " + firstName)

# 6. Write a Python program which takes two inputs from user and print them addition
a = int(input("enter first number: "))
b = int(input("enter second number: "))
sum = a + b
print("sum:", sum)