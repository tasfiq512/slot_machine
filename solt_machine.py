def deposit():
    while True:
        amount=input("What would you like to deposit? $ ")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number .")
    return amount
def get_number_of_line():
    while True:
        lines=input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines=int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number .")
    return lines
def get_bet():
    while True:
        amount=input("What would you like to bet on each line ? $ ")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<= amount<=MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET} .")
        else:
            print("Please enter a number .")
    return amount
def spin(balance):
    lines=get_number_of_line()
    while True:
      bet=get_bet()
      total_bet=bet*lines
      if total_bet>balance:
          print(f"You do not have enough to bet that amount,Your current balance is : ${balance}")
      else:
          break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots=get_slot_machine_spin(ROWS,COLS,symbol_value)
    print_slot_machine(slots)
    winning,winning_lines=check_winning(slots,lines,bet,symbol_value)
    print(f"You won ${winning}.")
    print(f"you won on lines:",*winning_lines)
    return winning -total_bet
def main():
    balance= deposit()
    while True:
        print(f"current balance is ${balance}")
        answer=input("press enter to spin (q to quit) .")
        if answer == "q":
            break
        balance+= spin(balance)

    print(f"you left with ${balance}")
   

main()