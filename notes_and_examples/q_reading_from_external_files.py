#External files

#you can use the python read command

#first you need to open the file
# first argument is the file, second is the mode
# we are going to use "r" which means read, "w" means write where you can change the file, "a" means append where u can add info to the end of the file, "r+" means read and write

employee_file = open("employees.txt", "r")


#the functions we can do with the file 

#how to check if a file is readable, you can use a function called readable... this is going to return a boolean value 
print(employee_file.readable())

#to read
print(employee_file.read())

#to read individual line 
print(employee_file.readline())

#a better funtion to read lines, it puts all the lines in a file and puts it in a list
print(employee_file.readlines()[1])

#can create a for loop
for employee in employee_file.readlines():
    print(employee)

# when you open a file you have to make sure you close it as well
employee_file.close()