# In this quiz i am gonna ask some question from the user and if he got the right answer, we will get him a score.

print("Welcome to the quiz game! ")
game_player = input("Do you want to play game?? ")
player_name = input("Please enter your name here ")

if game_player.lower() != "yes" :
    quit("Ok! Have a nice day ")

if player_name.lower() == "umair":
    quit("Sorry we cant allow anybody with the name of 'Umair' ")    
        
print("Welcome on board! ")
score = 0

# Question no 1
question = input("What does CPU stand for: ")
if question.lower() == "centeral processing unit":
    print("You got the right answer: ")
    score += 1
else:
    ("Your answer is not correct! ")

# Question no 2

question = input("What does GPU stand for ")
if question.lower() == "graphics processing unit":
    print("You got the right answer: ")
    score += 1
else:
    ("Your answer is not correct! ")

# Question no 3

question = input("What does RAM stand for: ")
if question.lower() == "random access memory":
    print("You got the right answer: ")
    score += 1
else:
    ("Your answer is not correct! ")

# Question no 4

question = input("What does PSU stand for: ")
if question.lower() == "power supply unit":
    print("You got the right answer: ")
    score += 1
else:
    ("Your answer is not correct! ")

print(f"Thanks for Playing {player_name}, Your score is {score}  ")
