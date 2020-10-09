#My mini fortune teller tarrot game 

topics = {
    1: "Love",
    2: "Friendship",
    3: "Money",
    4: "Career"
}

fortunes = {
    1:"Today it's up to you to create the peacefulness you long for.",
    2:"A friend asks only for your time not your money.",
    3:"If you refuse to accept anything but the best, you very often get it.",
    4:"A smile is your passport into the hearts of others.",
    5:"Your high-minded principles spell success.",
    6:"Hard work pays off in the future, laziness pays off now.",
    7:"Change can hurt, but it leads a path to something better.",
    8:"Enjoy the good luck a companion brings you.",
    9:"People are naturally attracted to you.",
    10:"Hidden in a valley beside an open stream- This will be the type of place where you will find your dream.",
}

colors = {
    "red": "1, 6, 4",
    "blue": "2, 9, 7",
    "purple": "5, 4, 1",
    "pink": "7, 3, 10",
    "black": "8, 10, 2",
}

color_string = "red blue purple pink black"

playing = True
still_playing = True 
topic_num = None
color = None
fortune_num = None

print("Welcome to Fifi's Fortunes, choose a number 1-4...\n")
while playing: 
    
    print("1.Love\n2.Friendship\n3.Money\n4.Career\n")
    topic_num = int(input("Enter the topic number: "))
    
    if topic_num >= 1 and topic_num <= 4:
        print("\nYou chose " + topics[topic_num] + ". Please select one of the following colors: red, blue, purple, pink or black.\n")
    else:
        print("\nPlease Select a number 1-4.")
        topic_num = int(input("Enter the topic number: "))
        print("\nYou chose " + topics[topic_num] + ". Please select one of the following colors: red, blue, purple, pink or black.\n")

    color = input("Enter a color: ")
    if color in color_string:
        print("\nYou chose " + color + ". Here are your special numbers: " + colors[color] + ". Please choose one to get your fortune.")
    else:
        print("Please enter a valid color.")
        color = input("Enter a color: ")
        print("\nYou chose " + color + ". Here are your special numbers: " + colors[color] + ". Please choose one to get your fortune.")

   

    fortune_num = int(input("Enter a special number: "))
    if str(fortune_num) in colors[color]: 
        print("\nThe fortune for your " + topics[topic_num] + " life is as follows: \n" + fortunes[fortune_num])
    else:
        print("\nPlease choose one of your special numbers.")
        fortune_num = int(input("Enter a special number: "))
        print("\nThe fortune for your " + topics[topic_num] + " life is as follows: \n" + fortunes[fortune_num])
    
    print("\nWould you like to play again? Please enter y for Yes or n for No.")
    still_playing = (input("y/n: "))
    
    if still_playing == "y":
        print("\nAlright, let's play again! Choose a number 1-4")
    elif still_playing == "n":
        playing = False
        print("\nCome again soon!\n\n\n")

    
