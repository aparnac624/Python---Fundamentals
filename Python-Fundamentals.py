# Python code that prints your name, student number and email address. An example runs of the program: Bob ST1001 bob@gmail.com 
print("Aparna ST1003 aparnac624@gmail.com")

#Python code that prints your name, student number and email address using escape sequences. An example runs of the program: Bob ST1001 bob@gmail.com
print("Aparna\tST1003\taparnac624@gmail.com")

# Python code that add, subtract, multiply and divide the two numbers. You can use the two numbers 14 and 7. An example run of the program: 14 + 7 = 21 14 * 7 = 98 14 – 7 = 7 14 / 7 = 2 
n1=14
n2=7
print(f"{n1}+{n2}={n1+n2}")
print(f"{n1}-{n2}={n1-n2}")
print(f"{n1}*{n2}={n1*n2}")
print(f"{n1}/{n2}={n1/n2}")


# Python code that displays the numbers from 1 to 5 as steps. An example runs of the program: 1 2 3 4 5 
n=1
print(n,n+1,n+2,n+3,n+4)

# Python code that outputs the following sentence (including the quotation marks and line break) to the screen: An example runs of the program: "SDK" stands for "Software Development Kit", whereas "IDE" stands for "Integrated Development Environment".
print("\"SDK\" stands for \"Software Development Kit\", whereas \"IDE\" stands for \"Integrated Development Environment\".")


# Practice and check the output print("python is an \"awesome\" language.") print("python\n\t2023") print('I\'m from Entri.\b') print("\65") print("\x65") print("Entri", "2023", sep="\n") print("Entri", "2023", sep="\b") print("Entri", "2023", sep="*", end="\b\b\b\b")
print("python is an \"awesome\" language.")   # output : python is an "awesome" language.
print("python\n\t2023")         
# output : python
#                	2023
print('I\'m from Entri.\b')      # output : I'm from Entri    # \b won't be visible
print("\65")                     # output : 5     (Octal 65 = Decimal 53 = '5')
print("\x65")                    # output : e     \x65 is the hexadecimal representation of 'e'
print("Entri", "2023", sep="\n")     # output : Entri          \n corresponds to newline character so 2023 appears in a new line 
                                                2023
print("Entri", "2023", sep="\b")    # output :  Entri2023      # \b may not be visible in output
print("Entri", "2023", sep="*", end="\b\b\b\b")     # output :  Entri*20     



# Define the variables below. Print the types of each variable. What is the sum of your variables? (Hint: use a type conversion function.) What datatype is the sum? num=23 textnum="57" decimal=98.3
num=23 
textnum="57" 
decimal=98.3
print(type(num))  # output: <class 'int'>
print(type(textnum)) #output: <class 'str'>
print(type(decimal))  #output: <class 'float'>

# converting textnum to integer and then calculating sum
sum = num + int(textnum) + decimal
print("Sum =",sum)          #output: Sum = 178.3
print("Datatype of sum variable :", type(sum))          #output: Datatype of sum variable : <class 'float'>




# calculate the number of minutes in a year using variables for each unit of time. 
# print a statement that describes what your code does also. 
# Create three variables to store no of days in a year, minute in a hour, hours in a day, then calculate the total minutes in a year and print the values 
# (hint) total number of minutes in an year =No.of days in an year * Hours in a day * Minutes in an hour

total_days = 365
total_minutes = 60
total_hours = 24
print("Total no:of days in a year =",total_days)
print("Total minutes in an hour =",total_minutes)
print("Total hours in a day =",total_hours)
print("Total no:of minutes in an year =", total_days*total_hours*total_minutes)

# output :
# Total no:of days in a year = 365
# Total minutes in an hour = 60
# Total hours in a day = 24
# Total no:of minutes in an year = 525600



# Python code that asks the user to enter his/her name and then output/prints his/her name with a greeting.
# An example runs of the program: Please enter you name: Tony Hi Tony, welcome to Python programming :) 
name = input("Please enter your name:")
print(f"{name} Hi {name}, welcome to Python programming :) ")


# output : Please enter your name: Aparna
#          Aparna Hi Aparna, welcome to Python programming :)