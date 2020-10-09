#Dictionaries 

#creating a program to convert a 3 dig month name to a full mounth name 

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Nov": "November",
    "Dec": "December"
}

#accessing a specific key 
print(monthConversions["Nov"])

#another way of accessing a key is using .get 
#does not return an error when a value is not in a dictionary, you can actually pass in a default value

print(monthConversions.get("Mar"))

print(monthConversions.get("Luv"))

print(monthConversions.get("Luv", "not a value"))

#you can also use numbers as keys 
fruits = {
    0: "apple",
    1: "bannana",
    2: "orange"
}

print(fruits)


