# Importing random library
import random

# Function that allow us to check the number and generate a random one
def Game():
    random_name = random.randint(1, 100)
    number = 0
    while number != random_name:
        number = input("Type a number!: ")
        if int(number) == random_name:
            print("You win!")
            return True
        elif int(number) <= random_name:
            print("The number is LOWER than the number on the console.")
        elif int(number) >= random_name:
            print("The number is HIGHER than the number on the console.")
        else:
            print("You should type a number")


# Showing data to the user
print(
    """Welcome to 'Guess the number' Game!
Here, the console is going to think a number. Then, you are going to try to guess it by typing it.
But, don't worry! The number is between 1-100 and the console will tell you if you've typed a number higher or lower than the number that it thought.
Good Luck! """
)
Game()
