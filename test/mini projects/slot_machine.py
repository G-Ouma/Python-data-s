import random

MAX_LINES = 3 # global constants
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in range(len(columns)):
            symbol_to_check = columns[column][line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines 


def get_deposit(balance=0):
    while True:
        if balance == 0:
            amount = input("How much would you like to deposit? $")
        else:
            amount = input(f"Your current balance is ${balance}. Add more money to continue playing: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The amount should be greater than 0.")
        else:
            print("Enter a valid amount!")
    return amount


def get_lines():
    while True:
        lines = input("How many lines would you like to bet on? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"The number of lines should be between (1 - {MAX_LINES}).")
        else:
            print("Enter a valid number of lines!")
    return lines


def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"The amount should be between ({MIN_BET} - {MAX_BET}).")
        else:
            print("Enter a valid amount!")
    return amount


def get_slot_machine_spin(rows, cols, symbols): 
    # this loop generates list of symbols to randomly choose from
    all_symbols = []
    for symbol, symbol_count in symbols.items(): # iterating through a dictionary while assigning the key and item simultaneaously
        for _ in range(symbol_count): # printing out symbols w.r.t their availability 
            all_symbols.append(symbol) # accumulating the symbols in a list

    columns = []
    # this loop generates and accumulates individual columns in an overall list
    for _ in range(cols): # iterating through the desired, provided column range 
        column = []
        current_symbols = all_symbols[:] # creating a copy of the symbol list
        
        # this loop is here since a column is a collection of rows
        for _ in range(rows): # iterating through the desired, provided row range
            value = random.choice(current_symbols) # randomly choosing a symbol from the symbol list
            column.append(value) # adding the symbol to the column list, which rep the rows
            current_symbols.remove(value) # removing the selected symbol so as not to select it again
        
        columns.append(column) # adding the individual column to the overall columns list
    return columns 


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=' | ')
            else:
                print(column[row], end=" ")
        print()


def spin(balance):
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(
                f"You have insufficient funds to make your desired bet. Your balance is ${balance}.")
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines. Your total bet is ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print("You won on lines:", *winning_lines)
    print("------------------------------------\n")

    return winnings - total_bet


def main():
    balance = get_deposit()
    while True:
        print(f"Your current balance is ${balance}")
        answer = input("Press Enter to play (q to quit)")
        if answer == "q":
            break
        while True:
            lines = get_lines()
            bet = get_bet()
            total_bet = bet * lines
            if total_bet > balance:
                print(
                    f"You have insufficient funds to make your desired bet. Your balance is ${balance}.")
                balance = get_deposit(balance)
            else:
                break
        
        print(f"You are betting ${bet} on {lines} lines. Your total bet is ${total_bet}")

        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        print_slot_machine(slots)
        winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
        print(f"You won ${winnings}.")
        if winning_lines:
            print("You won on lines:", *winning_lines)
        balance += winnings - total_bet
        print(f"Your current balance is ${balance}")
        if balance == 0:
            print("You're out of money! Game over.")
            break

main()