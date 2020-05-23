import random
SEPARATOR = '='*40
# Main function
def main():
    user_gr = greetings()
    guessing_number = number_selection()

   
# Users greetings
def greetings():
    name = input(f'Initiating...\nType your user name...')
    return print(f'{SEPARATOR}\nWelcome {name} in Bulls & Cows game!')
# Generated a random 4 digit number
# def number_selection():
#     with open('game_numbers.txt', 'a+') as txt:
#         number = txt.readlines().split()
#         return random.choice(number)
def number_selection():
    number = ''.join(random.sample("0123456789", 4))
# Asked to guessing the given number

# evaluates the user's tip and returns the number of matches.
main()