'''
Python Syntax
--------------------------------
This Project demonstrates basic Python syntax rules and features.
It Collects a student's name, age, and favorite subject, then display it by
the use of string formatting and conditional logic.
'''
import time

#Greet the user and collect their name, age, and favorite subject
#Display the collected information using formatted strings
name = input("\n\nEnter your Name: ")
print(f"Hello, {name}! Hope you're having a great day!")

age = int(input("\nPlease Enter your Age: "))
print(f"You are {age} years old and You are {'an minor' if age < 18 else 'an adult'}.")

subject = input("\nWhat is your favorite subject in school? ")
print(f"{subject} is a great subject! Keep up the good work, {name}!")

#Display fun fact with string lenth calculation

print(f"\nDid you know that the length of your name is {len(name)} characters?")

time.sleep(2)

#Using multiple format string

print("\nThis is the Summary of your inputs:")
print("\nProcessing........")
time.sleep(2)

print("\nUsing f-string: " )
print(f"Name: {name}, Age: {age}, Favorite Subject: {subject}")

print("\nUsing format() method: ")
print("Name: {}, Age: {}, Favorite Subjects: {}".format(name, age, subject))

print("\nUsing % operator: ")
print("Name: %s, Age: %d, Favorite Subject: %s" % (name, age, subject))

#Computations and \ for line continuation

total_letter = len(name) + \
               len(subject) 
total_number = len(str(age))

print(f"\nTotal number of letter you input is: {total_letter}")
print(f"Total number of digit you input is: {total_number}")
print(f"Total number of character you input is: {total_letter + total_number}")

#Final Message
time.sleep(2)
print(f"\nThank you for using the Python Syntax Demonstration Program, {name}! Goodbye!\n\n")