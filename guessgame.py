import random
thenumber=random.randint(1,99)
print("""Some rules:
If 'You are quite near', it means you have reached a range that the number plus or minus 5
If 'It is too low' or 'It is too high', they mean you have reached out of the range where the number plus or minus 5""")
print("Are you ready to take a game named Guess the Number?")
prompt="What's the number in your mind? "
while True:
    try:
        players_guess=int(input(prompt))
    except ValueError:
        print("Please enter a positive integer number with 2 digits!")
        continue
    if players_guess==thenumber:
        print("You are correct!")
        break
    elif 0<players_guess<thenumber-5:
        print("It is too low")
    elif thenumber-5<=players_guess<=thenumber+5:
        print("You are quite near!")
    elif 100>players_guess>thenumber+5:
        print("It is too high")
    elif players_guess>=100:
        print("Please enter a number from 1 to 99")
    elif players_guess<=0:
        print("Please enter a number from 1 to 99")
