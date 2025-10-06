name = input ("\nEnter Your Name: ")
project_name = input ("Enter Your Project Name: " )
date = input ("Enter Date: m-d-y: " )

print ("\n\nProject Name: {project_name}".format(project_name=project_name))
print ("Date: {date}" .format(date=date))

print ("\n ---Calculator----\n ")

num1 = float (input ("Enter first number: "))
num2 = float (input ("Enter second number: "))
              
print ("\n Select Operations: ")
print ("1. Addition")
print ("2. Subtraction")
print ("3. Multiplication")
print ("4. Division\n")    

operation = input ("Enter Operation: ")

if operation == '1':
    result = num1 + num2
    print ("\nResult: {result}".format(result=result))

elif operation == '2':
    result = num1 - num2
    print ("\nResult: {result}".format(result=result))

elif operation == '3':
    result = num1 * num2
    print ("\nResult: {result}".format(result=result))

elif operation == '4':
    if num2 != 0:
        result = num1 / num2
        print ("\nResult: {result}".format(result=result))
    else:
        print("\n Error: Division by zero is not allowed.")
else:
    print ("\n Invalid Operation")

print ("\n\nThank You {name} for using the calculator.\n\n".format(name=name))