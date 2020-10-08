#Getting input from users 

name = input("Enter your name: ")
print("Hello " + name + "!")

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! I am " + age + " years old.")

#Building a basic calculator 

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

# int() converts string only into integer 
result = int(num1) + int(num2)

print(result)

#Building a basic calculator 

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

# float() converts string into float(decimal) 
result = float(num1) + float(num2)

print(result)

#Build a Mad Libs game 

color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color + ".")
print(plural_noun + " are blue.")
print("I love " + celebrity + ".")

#Building my own Mad Libs Game 

place = input("Enter a place: ")
animal = input("Enter an animal: ")
event = input("Enter an event: ")

print("If you go down in the " + place +  " today, you\'re sure of a big surprise.")
print("If you go down in the " + place + " today, you'd better go in disguise.")
print("For every " + animal + " that ever there was will gather there for certain")
print("Because today's the day the " + animal + "s have their " + event )
