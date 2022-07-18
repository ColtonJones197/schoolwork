# Gets a number between 1 and 3 from the user, showing how many sticks they'd like to grab
def get_taken_sticks(current_player_name: str) -> int:
    is_valid = False
    while not is_valid:
        stick_input = input(f'Please enter the amount of sticks you\'d like to take(1-3) {current_player_name}: ')
        try:
            amount = int(stick_input)
            if amount < 1 or amount > 3:
                print('Number of sticks needs to be between 1 and 3.')
            else:
                return amount
        except ValueError:
            print('Please enter a valid input.')

def display_board():
    print('board')

def display_summary():
    print('summary')

def main():
    print('main')

if __name__ == '__main__':
    main()