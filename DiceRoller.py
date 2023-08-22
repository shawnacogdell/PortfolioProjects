import random

print('Welcome to Roll-a-thon 20k')
print("---------------------------")

print("How many twenty sided dice would you like to roll?")

while True:
    try:
        numberSelected = int(input("Type an number between 1 and 10: "))
        if 0 < numberSelected <= 10:
            break
        else:
            print("Invalid. Try again.")
    except:
        print("Please use a number. Try again.")


def rollDice(amount_to_roll):
    total_sum = 0
    possible_faces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for die in range(amount_to_roll):
        roll = random.choice(possible_faces)
        print("Die ", die + 1, ": ", roll)
        total_sum += roll
    ave_roll = total_sum / amount_to_roll
    print("Total Sum: ", total_sum)
    print("Average Roll: ", ave_roll)


rollDice(numberSelected)
