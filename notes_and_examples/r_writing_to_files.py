#writing to files


#appending to the file 
employee_file = open("employees.txt", "w")

#adding another employee onto the file
employee_file.write("Toby - Human Resources")

#adding another employee on a new line 
employee_file.write("\nKelly - Customer Service")

#writing to a file
#its going to override the entire file
employee_file.write("\nKelly - Customer Service")

#you can write a new file 
employee_file = open("employees1.txt", "w")
employee_file.write("\nKelly - Customer Service")

#you can use different extensions too 
employee_file = open("index.html", "w")
employee_file.write("<p>This is HTML</p>")

employee_file.close()