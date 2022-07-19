# Author: Colton Jones
# Section: ZA
# Description: Simulates STICK GAME in the console
from random import random, randrange

# takes in the current player and the number of sticks currently on the board
# returns the number of sticks taken by the player, which needs to be grabbed as an input.
def get_taken_sticks(current_player_number: int, sticks_on_board: int) -> int:
    # same thing as While True because this exits the function once a valid input is entered, but makes it more clear what the code is doing
    is_valid = False
    while not is_valid:
        stick_input = input(f'Player {current_player_number}\nPlease enter the amount of sticks you\'d like to take (1-3): ')
        try:
            amount = int(stick_input)
            if amount < 1 or amount > 3:
                print('Number of sticks needs to be 1, 2, or 3.')
            elif amount > sticks_on_board:
                print(f'There are only {sticks_on_board} sticks left. \nPlease enter an amount equal to or greater than the number of sticks left.')
            else:
                return amount
        except ValueError:
            print('Please enter a valid input.')

# gives a pretty print of the sticks on the board
def display_board(sticks_on_board: int) -> None:
    stick_length, stick_string, output = 5, '|  ', ''
    # creates the graphical representation of the sticks
    output += (stick_string * sticks_on_board + '\n') * stick_length
    # add the line at the bottom for the numbers
    for num in range(1, sticks_on_board + 1):
        output += f'{num}'.ljust(3)
    # display the output
    print(output)
    

# displays a summary of the most recent turn.
def display_summary(current_player_number: int, sticks_taken: int, sticks_remaining: int) -> None:
    print(f'Player {current_player_number} took {sticks_taken}! There are {sticks_remaining} sticks remaining.')

#control flow
def main():
    # initialize script
    should_continue_game = True
    starting_sticks, sticks_available = 20, 20
    players = [1, 2]
    turn_index = players[-1] # starts at the end for while loop flow, so that the correct winner is easy to determine
    magic_odds = 0.15 # percent chance that 1-4 sticks are randomly added back to the board

    print('WELCOME TO THE STICK GAME!')
    while should_continue_game:
        print('GAME START')
        # go through a turn until the end is reached
        while sticks_available > 0:
            # determine turn
            turn_index = turn_index + 1 if turn_index < len(players) - 1 else 0
            display_board(sticks_available)
            taken = get_taken_sticks(players[turn_index], sticks_available)
            sticks_available -= taken
            display_summary(players[turn_index], taken, sticks_available)
            # see if sticks should be added back to the board
            roll = random()
            if roll <= magic_odds:
                # figure out how many sticks to add back
                # needs the min because we never want to go above the number of starting sticks
                num_added_back = randrange(1, min(4, starting_sticks - sticks_available))
                sticks_available += num_added_back
                print(f'Whoa! {num_added_back} sticks magically reappear from the aether!\n{sticks_available} sticks are left now!')
        # if the loop exits, the player who's current turn it is loses
        print(f'Player {players[turn_index]} loses!')
        exit_input = input('Thanks for playing STICK GAME! Enter X to exit, otherwise the game will restart: ')
        should_continue_game = False if exit_input.upper() == 'X' else True

if __name__ == '__main__':
    main()
