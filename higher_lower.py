import random, os
from art import *
from game_data import data


#initialize global variables
SCORE = 0
CONT = True
ACCOUNT_B = random.choice(data)


def format_data(account):
    '''pull key values from each account'''
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return f'{account_name}, {account_desc}, from {account_country}.'


def answer(guess, a_followers, b_followers):
    '''Verify the answer. Parameters: guess, a_followers, b_followers'''
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


print(logo)


#initiate game loop
try:
    while CONT:

        #logic used to move position 2 (ACCOUNT_B) to position 1 (account_a) after a correct guess.
        account_a = ACCOUNT_B
        ACCOUNT_B = random.choice(data)
        #if both accounts are the same then randomize position 2 (ACCOUNT_B)
        while account_a == ACCOUNT_B:
            ACCOUNT_B = random.choice(data)


        print(f'Compare A: {format_data(account_a)}')
        print(vs)
        print(f'Compare B: {format_data(ACCOUNT_B)}')

        guess = input('Who has more followers? Type (A) or (B)\n ~ ').lower()

        #create local variables for follower counts and then pass to answer function and create local variable
        a_followers = account_a['follower_count']
        b_followers = ACCOUNT_B['follower_count']
        correct = answer(guess, a_followers, b_followers)

        #clear screen and present logo again
        os.system('clear')
        print(logo)
        
        #present answer, tally if correct, exit game loop if incorrect
        if correct:
            print(f'You are correct! Current score: {SCORE}')
            SCORE += 1
        else:
            print(f'Sorry, you are incorrect. :( Final score: {SCORE}')
            CONT = False

except KeyboardInterrupt:
    print('\nSee you later.')