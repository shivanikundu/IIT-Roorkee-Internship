#Use the random module to bulid a dice-roll simulator
import  random
def roll_dice():
    return random.randint(1,6)
while True:
    print("You rolled :", roll_dice())
    choice = input("Roll again : ")
    if choice != 'yes':
        print("Thanks for playing!")
        break