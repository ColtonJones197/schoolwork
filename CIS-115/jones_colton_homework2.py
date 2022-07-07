# Author: Colton Jones
# Partner: no
# Section: ZA
# Project: Vending Machine
# Description: Single python script created to simulate an out of control vending machine

from random import random


if __name__ == '__main__':
    state = 'A'
    total_inserted, cost = 0, 0.99
    item_1, item_2, item_3 = 2, 6, 3
    vending_machine_items = {'Chocolate Covered Balls': item_1, 'Unicorn Horn': item_2, 'Big Dogs WOOF WOOF': item_3}
    command_state_mappings = {'S': 'B', 'R': 'F', 'E': 'G'}
    
    while state != 'G':
        match state:
            #start
            case 'A':
                    print('Welcome to the vending machine!\nCurrent options:\n\t(S)tart\n\t(R)estock\n\t(E)xit')
                    user_input = input('Please pick an option: ')
                    first_letter = user_input[0].upper()
                    if first_letter in 'SRE':
                        state = command_state_mappings[first_letter]
                    else:
                        print('Please enter a valid command!')
            case 'B':
                    change_input = input('Please insert change (Enter a number), or request a (R)efund: ')
                    if change_input[0].upper() == 'R':
                        # do the refund
                        print('Issuing refund...')
                        state = 'E'
                    change = float(change_input)
                    if random() <= 0.31:
                        print('Whoopsy doopsy! The gremlin magic ate your change!')
                        print(f'Please insert more change. Amount needed: {cost - total_inserted}')
                    else:
                        total_inserted += change
                        if total_inserted > cost:
                            state = 'C'
                        else:
                            print(f'Please insert more change. Amount needed: {cost - total_inserted}')
            case 'C':
                print('You have enough change! Here are the available items: ')
                name_output = ''
                selection_num = 1
                for item, amt in vending_machine_items:
                    name_output += f'({selection_num}) {item}: {amt} left' + '\n'
                    selection_num += 1
                print(name_output)
                selected = int(input('Please select an item: '))
                if vending_machine_items[selected - 1] <= 0:
                    print('This item is out of stock! Please select a different item!')
                else:
                    vending_machine_items[selected - 1] -= 1
                    
