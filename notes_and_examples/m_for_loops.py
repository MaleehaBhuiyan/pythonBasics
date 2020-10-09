#for loop
#allows us to loop through different collection on items, we use them to loop through different arrays, a string series of numbers etc.

#loop through a string 
for letter in "Giraffe Academy":
    print(letter)

#loop through an array 
friends = ["Molly", "Maria", "McKenzie"]
for friend in friends:
    print(friend)

#loop through a series of numbers
#range excludes the last number 
for num in range(10):
    print(num)

for num in range(3,10):
    print(num)

#example 

friends = ["Molly", "Mariana", "Millie"]

for index in range(len(friends)):
    print(index)

#this is another way to print out the names 
for index in range(len(friends)):
    print(friends[index])

#you can put logic in these for loops
for index in range(3):
    if index == 0:
        print("First Iteration")
    else:
        print("Not first Iteration")
