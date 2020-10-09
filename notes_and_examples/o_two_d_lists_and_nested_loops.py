#2d lists and nested loops

number_grid = [ 
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

#selecting individual elements from the grid, this gets the number 1, goes by row and then column 

print(number_grid[0][0])

#nested for loop to print out all the elements in this array 

for row in number_grid: #this will out put the whole grid, the four rows 
    for col in row: #this will print out each individual number because it is going through each row 
        print(col)

#Building a translator 

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou": #.lower() => converts the letters in a string to lowercase 
            if letter.isupper(): #.isupper() => returns true if a letter in a string is upper case or false if a letter is lower case
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))



