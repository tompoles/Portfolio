import random
SEPARATOR = '='*40
SEPARATOR_2 = '_'*40
name = input(f'Initiating...\nType your user name...')
# Main function
def main():
    greetings()
    number = number_selection()
    attempts = True
    while attempts:
        player_number = guessed_number()
        game_evaluation(number, player_number)
        game_status(attempts, number, player_number)
        attempts += 1
# Users greetings
def greetings():
    return print(f'{SEPARATOR}\nWelcome {name} in Bulls & Cows game!\nThere was generated 4 digit number for you.\n'
                 f'Go and try guess it\n{SEPARATOR_2}')
# Generated a random 4 digit number
def number_selection():
    gen_number = ''.join(random.sample("0123456789", 4))
    return gen_number
# Asked to guessed the given number
def guessed_number():
    return input(f'{name} enter your 4 digit number!\n:')
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
        elif number[i] in user_guess:
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
        status = f'{name} you won in {att} rounds on {level} difficulty'
        print(status, SEPARATOR_2, sep='\n')
        with open("bulls_cows.txt", "a+", newline='') as txt:
            txt.writelines(status), \
            txt.write('\n'), \
            txt.close()
        exit()
main()