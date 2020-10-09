#try except helps us watch out for specific errors and helps us handle them, helps protect our program.. catches invalidinputs 

# example
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input")


# you can catch specific errors 

try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:  
    print("Divided by Zero")
except ValueError:
    print("Invalid Input")


#you can store error as a variable
#This is best practice in python
try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:  
    print(err)
except ValueError:
    print("Invalid Input")
