# Author: Colton Jones
# Partner: no
# Section: ZA
# Project: Vending Machine
# Description: Single python script created to simulate a quirky vending machine

from random import random

if __name__ == '__main__':
    state = 'A'
    total_inserted, cost = 0, 0.99
    # starting quantities of the different items
    item_1, item_2, item_3 = 2, 6, 3
    # key-value pair tracking quantities of each item
    vending_machine_items = {'Chocolate Covered Balls': item_1, 'Unicorn Horn': item_2, 'Big Dogs WOOF WOOF': item_3}
    # maps user input from the start to the expected state because I didn't want another nested case
    command_state_mappings = {'S': 'B', 'R': 'F', 'E': 'G'}
    
    while state != 'G':
        match state:
            # Start
            case 'A':
                    print('Welcome to the vending machine!\nCurrent options:\n\t(S)tart\n\t(R)estock\n\t(E)xit')
                    user_input = input('Please pick an option: ')
                    first_letter = user_input[0].upper() # cast to upper for easier usability
                    # if it has a mapping, set the state, otherwise loop back to the start
                    if first_letter in command_state_mappings.keys():
                        state = command_state_mappings[first_letter]
                    else:
                        print('Please enter a valid command!')
            # Insert
            case 'B':
                    change_input = input('Please insert change (Enter a number), or request a (R)efund: ')
                    if change_input[0].upper() == 'R':
                        # do the refund
                        print('Issuing refund...')
                        state = 'E'
                    change = float(change_input)
                    if random() <= 0.31:
                        print('Whoopsy doopsy! The gremlin magic ate your change!')
                    else:
                        total_inserted += change
                    if total_inserted > cost:
                        state = 'C'
                    else:
                        print(f'Please insert more change. Amount needed: {cost - total_inserted}')
            # Select
            case 'C':
                print('You have enough change! Here are the available items: ')
                name_output = ''
                selection_num = 1
                # my pretty print of the items in the vending machine
                for item, amt in vending_machine_items.items():
                    name_output += f'({selection_num}) {item}: {amt} left' + '\n'
                    selection_num += 1
                print(name_output)
                selection_input = input('Please select an item or ask for a (R)efund: ')
                # Worth noting any other text will crash the program.
                if selection_input[0] == 'R':
                    state = 'E'
                else:
                    selected = int(selection_input)
                    # We just need the values so that's all that the script pulls from here.
                    if list(vending_machine_items.values())[selected - 1] <= 0:
                        print('This item is out of stock! Please select a different item!')
                    else:
                        state = 'D'
            # Dispense
            case 'D':
                # get the name of the selected item so that we can say we're dispensing it
                # and then modify its quantity in the dictionary
                selected_item = list(vending_machine_items.keys())[selected - 1]
                print(f'Dispensing {selected_item}...')
                vending_machine_items[selected_item] -= 1
                total_inserted -= cost
                state = 'E' if total_inserted > 0 else 'A' # go to return change if there's change, otherwise go back to the start
            # Return Change
            case 'E':
                print('Returning change of {:.2f}'.format(total_inserted))
                # Just resets the total to 0, presumably would also spit out some actual change if this were a real vending machine
                total_inserted = 0
                state = 'A' # Back to the start
            # Restock
            case 'F':
                print('Restocking items...')
                vending_machine_items = {'Chocolate Covered Balls': item_1, 'Unicorn Horn': item_2, 'Big Dogs WOOF WOOF': item_3}
                state = 'A' # Back to the start
    # This means that the user has specified they would like to exit (state has been set to G)
    print('Thank you for using the gremlin vending machine! Exiting now...')
                    
