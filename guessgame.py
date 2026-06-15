import random
thenumber=random.randint(1,99)
print("Are you ready to take a game named Guess the Number?")
prompt="What's the number (2 digits) in your mind? "
while True:
    players_guess=int(input(prompt))
    if players_guess==thenumber:
        print("You're correct!")
        break
    elif 0<players_guess<thenumber-10:
        print("It's too low")
    elif thenumber-10<=players_guess<=thenumber+10:
        print("You're quite near!")
    #elif 29<=players_guess<=35:
        #print("You're quite near!")
    elif players_guess>thenumber+10:
        print("It's too high")
