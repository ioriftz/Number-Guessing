import random

def main():
    number = random.randint(1,100)
    chances = int(3)
    print('Welcome to Number Guessing.')
    greaterNumber = int(number-5)
    greater = random.randint(greaterNumber, greaterNumber+4)
    smaller = random.randint(int(number+1), int(number+5))
    print('Your number is greater than ' + str(greater) + ' and smaller than ' + str(smaller) + '.')
    displayHint(chances)
    print('Type your guess:')
    guess = input()
    while chances != 0:
        if int(guess) != number:
            chances -= 1
            if chances == 0:
                print('You lost.')
                return
            else:
                displayHint(chances)
                print('Type your guess:')
                guess = input()
        if int(guess) == number:
            print('You won!')
            return

def displayHint(hint):
    print('You have ' + str(hint) + ' hints left.')

main()