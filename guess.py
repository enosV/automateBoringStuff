#This is game about guessing a number
import random

print('Hello user. What is your name?')
name = input()

print('well, ' + name + ', I am thinking of number between 1 - 20')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print ('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is for the correct guess!

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' tries')
else:
    print('Nope, the number I was thinking of was ' + str(secretNumber))

