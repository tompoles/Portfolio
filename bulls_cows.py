import random
SEPARATOR = '='*40
# Main function
def main():
    user_gr = greetings()
   
# Users greetings
def greetings():
    name = input(f'Initiating...\nType your user name...')
    return print(f'{SEPARATOR}\nWelcome {name} in Bulls & Cows game!')
# Generated a random 4 digit number
def number_sel():
    with open('game_numbers.txt', 'w') as txt:
        number = txt.read().split()
        return
# Asked to guessing the given number
# evaluates the user's tip and returns the number of matches.
main()