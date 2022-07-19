# Gets a number between 1 and 3 from the user, showing how many sticks they'd like to grab

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

def main():
    print('main')

if __name__ == '__main__':
    display_board(12)
    input()