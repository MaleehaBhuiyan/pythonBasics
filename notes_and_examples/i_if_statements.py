#If Statements 

#basic if statement 

is_female = True 
if is_female: 
    print("You are a Female")

#prints nothing because false 
is_female = False 
if is_female: 
    print("You are a Female")
    
#using else 
if is_female: 
    print("You are a Female")
else: 
    print("You are not a Female")


#making it more complex 
is_a_cat = True 
is_small = False 
    
#or keyword 

if is_a_cat or is_small:
    print("Awww")
else:
    print("Alrighty")

#and keyword 
if is_a_cat and is_small: 
    print("You are a small cat")
else: 
    print("You are either a cat but not small or small but not a cat or neither :(")
    

#Conditions 
#elif: else if, you can put another condition 
if is_a_cat and is_small: 
    print("You are a small cat")
elif is_a_cat and not(is_small):
        print("You are not a small cat")
else: 
    print("You are either a cat but not small or small but not a cat or neither :(")
    

