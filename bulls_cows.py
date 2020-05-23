import random
SEPARATOR = '='*40
SEPARATOR_2 = '_'*40
name = input(f'Initiating...\nType your user name...')
# Main function
def main():
    greetings()
    number = number_selection()
    print(number)
    attempts = True
    while attempts:
        attempts += 1
        # attempts = 0
        player_number = guessed_number()
        game_evaluation(number, player_number)
        game_status(attempts, number, player_number)
        exit()

# Users greetings
def greetings():
    return print(f'{SEPARATOR}\nWelcome {name} in Bulls & Cows game!\nThere was generated 4 digit number for you.\n'
                 f'Go and try guess it\n{SEPARATOR_2}')
# Generated a random 4 digit number
def number_selection():
    gen_number = ''.join(random.sample("0123456789", 4))
    return gen_number
# Hide selected number
def hide_number(number):
    return len(number) * ["*"], round(1.4 * len(number), 0)
# Asked to guessed the given number
def guessed_number():
    return input(f'{name} enter your number!\n:')
# evaluates the user's tip and returns the number of matches.
def evaluation_of_tip(tip, number, hidden_num):
    for index, num in enumerate(number):
        if num in tip:
            hidden_num[index] = num
# def game_evaluation(attempt, player, hidden_number):
def game_evaluation(number, user_guess):
    cowbull = [0,0]
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbull[1]+=1
        else:
            cowbull[0]+=1
    return print(f'{cowbull[1]} Bulls, {cowbull[0]} Cows')
# Game status
def game_status(att, number, user_guess):
    if user_guess == number:
        if att <= 5:
            level = "'Damn I'm good'"
        elif att <= 10:
            level = "'Come and get some'"
        elif att <= 13:
            level = "'Let's rock'"
        else:
            level = "'Piece of cake'"
    status = f'You won in {att} rounds on {level} difficulty'
    print(status, SEPARATOR_2, sep='\n')
main()