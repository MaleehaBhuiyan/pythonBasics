#Comparisons 

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3: 
        return num1 
    elif num2 >= num1 and num2 >= num3:
        return num2 
    else:
        return num3 

print(max_num(2, 32, 4))

#equal 

def same(word1, word2):
    if word1 == word2:
        return "Same word"
    else:
        return "Different word"

print(same("Hi", "Hi"))

#not equal 
def different_word(word1, word2):
    if word1 != word2:
        return "Unique words"
    else: 
        return "Basic Words"

print(different_word("Good morning", "Goodnight"))

#Building a better Calculator 

num1 = float(input("Enter first number: "))
operator = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
     print("Invalid Operator")