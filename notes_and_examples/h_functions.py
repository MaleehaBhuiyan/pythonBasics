#Funtions 

#a collection of code that performs a specific task 
#its good to break up your code into dddifferent functions 

#how to create a function 
def say_hi():
    print("Hello User")
    
#to execute the code you need to call it 
say_hi()

#the flow of functions 
print("Top")
say_hi()
print("Bottom")

#making the functions more powerful by giving them information through paramaters 
def say_goodnight(noun):
    print("Goodnight " + noun)

say_goodnight("moon")

#you can have more than one parameter 
def say_bye(name_one, name_two):
    print("Bye, " + name_one + ". Bye, " + name_two + ".")
say_bye("Maleeha", "Sadeyah")


#Return statement 

#sometimes we want information back from that function, execute code but then give me some information back 

def cube(number):
    return number * number * number 

result = cube(4)
print(result)