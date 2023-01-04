# importing library
import random

# defining 3 lists with n number of elements
FEELING = ["sadness", "disgust", "happiness", "loneliness", "anger", "anticipation", "fear",
            "jealousy", "love", "surprise", "irritation", "nervousness", "sympathy", "attraction"]
COLOR = ["maroon", "magenta", "violet", "olive", "lime", "crimson",
          "azure", "indigo", "red", "brown", "purple", "orange", "gray", "navy"]
ANIMAL = ["meerkat", "penguin", "aardvark", "badger", "chimpanzee", "echidna",
           "ferret", "groundhog", "beaver", "kangaroo", "hamster", "hwak", "gorilla", "leopard"]

print("Password Generator\n==================\n")

# loop to take the number of password needed and print it out and check the user input too
while True:
    try:
        noOfPassword = int(input("How many passwords are needed? "))
        if noOfPassword >= 1 and noOfPassword <= 24:
            for i in range(noOfPassword):
                print(
                    f"\n{i+1} --> {random.choice(FEELING)+random.choice(COLOR)+random.choice(ANIMAL)}")
            break
        else:
            print("\nPlease enter a value between 1 and 24.")
    except ValueError:
        print("\nPlease enter a number.")
