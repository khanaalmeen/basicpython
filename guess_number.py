from random import randint
guesses = 1
num = randint(1, 10)
guess = int(input("guess a number between 1 and 10 = "))

while guess != num:
    if guess > num:
        print("Number guessed is too high")
        guess = int(input("Guess again."))
        guesses = guesses+1
    elif guess < num:
        print("Number guessed is too low")
        guess = (int(input("Guess again.")))
        guesses= guesses + 1


print()
print("Congragulations u guessed it correctly")
print("It took you", guesses,"guesses")
