# THE HABIBI CASINO
# Adam Abbas from Bloomsbury of New Jersey
# kitty's name: Habibi (obviously)

def play_slots():
    # TOP DOLLAR SLOT MACHINE
    from random import choice
    # CREATE SYMBOLS
    symbols = ["🍒", "🍊", "🍋", "🍇", "🍉", "🍌", "🍎", "🥭", "🥝", "👑"]
    # CREATE TOP DOLLAR PRIZES
    top_dollar_prizes = [100, 200, 300, 400, 500, 1000, 2500, 5000, 30000]

    # WELCOME USER
    def main():
        play_or_rules = input("Welcome to Top Dollar Slots!\nType 'P' to play or 'R' to view the rules, "
                              "Type 'Q' to quit...\n").title()
        if play_or_rules == "Q":
            print("Goodbye!")
            game_choice()


        elif play_or_rules == "R":
            print("Welcome to Top Dollar Slots, a uniquely designed, prize-based slot machine.\n"
                  "Each spin grants a chance to land the Top Dollar wheel.\n"
                  "If you land a crown symbol : 👑 in the middle column of the middle row,\n"
                  "the Top Dollar wheel is executed; allowing you to win a prize after 3 spins.\n"
                  "NOTE: You will have 3 chances to spin the Top Dollar wheel when executed and\n"
                  "you get to decide which prize you wish to keep via the spin again/take prize options,\n"
                  "but beware that once you spin the Top Dollar wheel again, you are no longer eligible for the\n"
                  "preceding prize. NOTE: 👑 MUST LAND IN MIDDLE COLUMN TO GRANT TOP DOLLAR BONUS.\n"
                  "This is Top Dollar Slots, crack a spin!")
        elif play_or_rules == "P":
            pass

        # INITIALIZE BALANCE TO 0
        balance1 = 0
        # STARTING DEPOSIT
        while True:
            try:
                dep_amount = int(input("\nDeposit to start playing! 🎰\nMinimum Deposit = $25\nDeposit: $"))
                balance1 = deposit(balance1, dep_amount)
                print(f"Your balance is now ${balance1}, crack a spin!")
                spin_loop(balance1)
                break
            except ValueError:
                print("Invalid Entry!")
                continue

    # 1st FUNCTION - Deposit
    def deposit(balance1, dep_amount):
        balance1 += dep_amount
        return balance1

    # 2nd FUNCTION - Top Dollar Wheel
    def top_dollar_spin(balance1, result2_row2):
        td_spin1 = choice(top_dollar_prizes)
        print("TOP DOLLAR!")

        # TD OUTCOMES:
        spin_or_take1 = input(f"2 tries left! Type 'T' to take this ${td_spin1} cash prize or 'S' to spin again!\n").title()

        # If user takes prize
        if spin_or_take1 == "T":
            balance1 += td_spin1
            print(f"CONGRATS! Your balance is now ${balance1}")
            spin_loop(balance1)

        # If user spins again
        elif spin_or_take1 == "S":
            td_spin2 = choice(top_dollar_prizes)
            spin_or_take2 = input(f"1 try left! Type 'T' to take this ${td_spin2} cash prize or 'S' to spin again!\n").title()

            # If user takes prize
            if spin_or_take2 == "T":
                balance1 += td_spin2
                print(f"CONGRATS! Your balance is now ${balance1}!")
                spin_loop(balance1)

            # If user spins again
            elif spin_or_take2 == "S":
                td_spin3 = choice(top_dollar_prizes)
                balance1 += td_spin3
                print(f"CONGRATS! You won ${td_spin3}! Your balance is now ${balance1}!")
                spin_loop(balance1)

    # 3rd FUNCTION - Spin Loop
    def spin_loop(balance1):
        while True:
            try:
                # Validation for sufficient balance
                if balance1 > 0:

                    # Induce spin loop
                    spin_or_quit = input("Type 'S' to Spin, 'C' to Cashout, or 'R' to view rules...\n").title()
                    if spin_or_quit == "S":

                        # ROW 1 SPIN
                        result1_row1 = choice(symbols)
                        result2_row1 = choice(symbols)
                        result3_row1 = choice(symbols)
                        print(result1_row1, result2_row1, result3_row1)
                        # ROW 2 SPIN
                        result1_row2 = choice(symbols)
                        result2_row2 = choice(symbols)
                        result3_row2 = choice(symbols)
                        print(result1_row2, result2_row2, result3_row2)
                        # ROW 3 SPIN
                        result1_row3 = choice(symbols)
                        result2_row3 = choice(symbols)
                        result3_row3 = choice(symbols)
                        # DISPLAY RESULTS
                        print(result1_row3, result2_row3, result3_row3)
                        # CHECK FOR TOP DOLLAR
                        if result2_row2 == "👑":
                            top_dollar_spin(balance1, result2_row2)
                        else:
                            pass
                        # INDUCE PAYOUTS
                        payout_row1(balance1, result1_row1, result2_row1, result3_row1)
                        payout_row2(balance1, result1_row2, result2_row2, result3_row2)
                        payout_row3(balance1, result1_row3, result2_row3, result3_row3)


                    # CASHOUT
                    elif spin_or_quit == "C":
                        cashout = input(f"Are you sure you'd like to cashout your ${balance1}?\nYes or No?\n").title()
                        if cashout == "Yes":
                            print(f"Very well, here's your ${balance1}\nGood game 👋🏽\n")
                            main()
                            break

                        # CONFIRM CASHOUT
                        elif cashout == "No":
                            print("Get back in there champ!")
                            continue
                        # DISPLAY RULES
                    elif spin_or_quit == "R":
                        print("Welcome to Top Dollar Slots, a uniquely designed, prize-based slot machine.\n"
                              "Each spin grants a chance to land the Top Dollar wheel.\n"
                              "If you land a crown symbol : 👑 in the middle column of the middle row,\n"
                              "the Top Dollar wheel is executed; allowing you to win a prize after 3 spins.\n"
                              "NOTE: You will have 3 chances to spin the Top Dollar wheel when executed and\n"
                              "you get to decide which prize you wish to keep via the spin again/take prize options,\n"
                              "but beware that once you spin the Top Dollar wheel again, you are no longer eligible for the\n"
                              "preceding prize. NOTE: 👑 MUST LAND IN MIDDLE COLUMN TO GRANT TOP DOLLAR BONUS.\n"
                              "This is Top Dollar Slots, crack a spin!")
                        continue

                # IF USER BUSTS
                elif balance1 <= 0:
                    print("BUST! Better luck next time bud...")
                    break

            except ValueError:
                print("Invalid Entry!")
                continue

    # 4th FUNCTION - Payout for First Row
    def payout_row1(balance1, result1_row1, result2_row1, result3_row1):
        balance1 -= 25
        if result1_row1 == result2_row1 == result3_row1:
            balance1 += 2500
            print(f"JACKPOT!!! Your balance is now ${balance1}!")
        else:
            print(f"Balance: ${balance1}")
        spin_loop(balance1)

    # 5th FUNCTION - Payout for Second Row
    def payout_row2(balance1, result1_row2, result2_row2, result3_row2):
        balance1 -= 25
        if result1_row2 == result2_row2 == result3_row2:
            balance1 += 2500
            print(f"JACKPOT!!! Your balance is now ${balance1}!")
        else:
            print(f"Balance: ${balance1}")
        spin_loop(balance1)

    # 5th FUNCTION - Payout for Third Row
    def payout_row3(balance1, result1_row3, result2_row3, result3_row3):
        balance1 -= 25
        if result1_row3 == result2_row3 == result3_row3:
            balance1 += 2500
            print(f"JACKPOT!!! Your balance is now ${balance1}!")
        else:
            print(f"Balance: ${balance1}")
        spin_loop(balance1)

    ##########################################
    # CALL MAIN
    if __name__ == "__main__":
        main()

def play_roulette():
    from random import choice
    # Let's code roulette

    # Build American table
    usa_table = tuple(range(37)) + (0, 00)
    # Build European table
    eur_table = tuple(range(37))
    # Colors
    colors = "Red", "Black"

    def main1():
        print("ROULETTE")
        style = str(input("Type 'A' for American table, Type 'E' for European table, "
                          "Type 'Q' to quit!\n")).title()
        if style == "Q":
            quit = str(input("Are you sure you'd like to quit playing roulette?\nYes or No?\n"))
            if quit == "Yes":
                print("Very well...")
                game_choice()
            elif quit == "No":
                print("Get back in there champ!")
                main1()
        elif style == "A":
            deposit2()
            print("American")
            print(usa_table)
            usa_bet_loop()

        elif style == "E":
            deposit2()
            print("European")
            print(eur_table)
            eur_bet_loop()


    def deposit2():
        global balance
        balance = 0
        dep_amount = int(input("Enter a starting deposit: | Min. Bet = $25\nDeposit: $"))
        balance += dep_amount
        print(f"Your balance is now ${balance}!")
        return balance

    # USA GAME
    def usa_bet_loop():
        global balance
        while True:
            try:
                bet_type = str(input("\n\nType 'N' to bet on numbers, type 'C' to bet on colors,"
                                     " type 'Q' to cashout!\n")).strip().title()
                if bet_type == "Q":
                    cashout = str(input(f"Are you sure you'd like to cashout your balance of ${balance}?\n"
                                        "Yes or No?\n")).strip().title()
                    # CASHOUT USA GAME
                    if cashout == "Yes":
                        print(f"Very well... Here is your ${balance}, good game.\n")
                        game_choice()
                    elif cashout == "No":
                        print("Get back in there champ!")
                        continue

                # USA NUMBERS BET
                elif bet_type == "N":
                    usa_num_bet = int(input("Type the number you wish to bet on\n0-36/00\n"))
                    if int(usa_num_bet) not in tuple(range(37)):
                        print("Invalid Number, try again!")
                        continue
                    elif usa_num_bet < 0:
                        print("Please enter a number greater than 0.")
                        continue
                    elif usa_num_bet > 36:
                        print("Invalid Number")
                        continue
                    else:
                        # USA NUMBERS BET AMOUNT
                        while True:
                            try:
                                usa_num_bet_amount = int(input("How much $ would you like to bet?\nBet Amount: $"))
                                if usa_num_bet_amount < 25:
                                    print("Bet must be at least $25")
                                    continue
                                elif usa_num_bet_amount > balance:
                                    print("You don't have a sufficient balance for this bet!")
                                    continue
                                else:
                                    # USA NUMBERS BET RESULTS
                                    usa_num_spin_result = choice(usa_table)
                                    # USA NUMBERS PAYOUT
                                    if usa_num_spin_result == usa_num_bet:
                                        balance += int(usa_num_bet_amount * 35)
                                        print(f"BALL DROPPED IN {usa_num_spin_result}")
                                        print(f"Your balance is now ${balance}!!!")
                                        break
                                    elif usa_num_spin_result != usa_num_bet:
                                        balance -= int(usa_num_bet_amount)
                                        print(f"Ball dropped in {usa_num_spin_result}")
                                        print(f"Your balance is now ${balance}...")
                                        break
                            except ValueError:
                                print("Invalid Entry!")
                                continue

                # USA COLOR BET
                elif bet_type == "C":
                    while True:
                        try:
                            usa_color_bet = str(input("Type 'R' to bet on Red, type 'B' to bet on black...\n")).title()
                            # USA RED BET
                            if str(usa_color_bet) == "R":
                                while True:
                                    try:
                                        # USA RED BET AMOUNT
                                        usa_color_bet_amount = int(input("How much $ would you like to bet?\nBet Amount: $"))
                                        if usa_color_bet_amount < 25:
                                            print("Bet must be at least $25")
                                            continue
                                        elif usa_color_bet_amount > balance:
                                            print("You don't have a sufficient balance for this bet!")
                                            continue
                                        else:
                                            # USA RED BET RESULTS
                                            usa_color_spin_result = choice(usa_color_bet)
                                            # PAYOUT FOR USA RED BET
                                            if usa_color_spin_result == usa_color_bet:
                                                balance += int(usa_color_bet_amount * 2)
                                                print(f"BALL DROPPED IN RED!!!")
                                                print(f"Your balance is now ${balance}!")
                                                usa_bet_loop()
                                                break

                                            elif usa_color_spin_result != usa_color_bet:
                                                balance -= int(usa_color_bet_amount)
                                                print(f"Ball dropped in black...")
                                                print(f"Your balance is now ${balance}.")
                                                usa_bet_loop()
                                                break
                                    except ValueError:
                                        print("Invalid Entry!")
                                        continue

                            # USA BLACK BET
                            elif str(usa_color_bet) == "B":
                                while True:
                                    try:
                                        # USA BLACK BET AMOUNT
                                        usa_color_bet_amount = int(input("How much $ would you like to bet?\nBet Amount: $"))
                                        if usa_color_bet_amount < 25:
                                            print("Bet must be at least $25")
                                            continue
                                        elif usa_color_bet_amount > balance:
                                            print("You don't have a sufficient balance for this bet!")
                                            continue
                                        else:
                                            # USA BLACK BET RESULTS
                                            usa_color_spin_result = choice(usa_color_bet)
                                            # PAYOUT FOR USA BLACK BET
                                            if usa_color_spin_result != usa_color_bet:
                                                balance += int(usa_color_bet_amount * 2)
                                                print(f"BALL DROPPED IN BLACK!!!")
                                                print(f"Your balance is now ${balance}!")
                                                usa_bet_loop()
                                                break

                                            elif usa_color_spin_result == usa_color_bet:
                                                balance -= int(usa_color_bet_amount)
                                                print(f"Ball dropped in red...")
                                                print(f"Your balance is now ${balance}.")
                                                usa_bet_loop()
                                                break

                                    except ValueError:
                                        print("Invalid entry! Please try again...")
                                        continue
                        except TypeError:
                            print("Invalid Entry!")
                            continue
            except ValueError:
                print("Invalid Entry, please enter an integer.")
                continue

    ########################################################################################################################
    # EUR GAME
    def eur_bet_loop():
        global balance
        while True:
            try:
                bet_type = str(input("\n\nType 'N' to bet on numbers, type 'C' to bet on colors,"
                                     " type 'Q' to cashout!\n")).strip().title()
                if bet_type == "Q":
                    cashout = str(input(f"Are you sure you'd like to cashout your balance of ${balance}?\n"
                                        "Type 'Y' for yes, type 'N' for no...\n")).strip().title()
                    # CASHOUT EUR GAME
                    if cashout == "Y":
                        print(f"Very well... Here is your ${balance}, good game.\n")
                        main1()
                    elif cashout == "N":
                        print("Get back in there champ!")
                        continue

                # EUR NUMBERS BET
                elif bet_type == "N":
                    eur_num_bet = int(input("Type the number you wish to bet on\n0-36/00\n"))
                    if int(eur_num_bet) not in tuple(range(37)):
                        print("Invalid Number, try again!")
                        continue
                    elif eur_num_bet < 0:
                        print("Please enter a number greater than 0.")
                        continue
                    elif eur_num_bet > 36:
                        print("Invalid Number")
                        continue
                    else:
                        # EUR NUMBERS BET AMOUNT
                        while True:
                            try:
                                eur_num_bet_amount = int(input("How much $ would you like to bet?\nBet Amount: $"))
                                if eur_num_bet_amount < 25:
                                    print("Bet must be at least $25")
                                    continue
                                elif eur_num_bet_amount > balance:
                                    print("You don't have a sufficient balance for this bet!")
                                    continue
                                else:
                                    # EUR NUMBERS BET RESULTS
                                    eur_num_spin_result = choice(eur_table)
                                    # EUR NUMBERS PAYOUT
                                    if eur_num_spin_result == eur_num_bet:
                                        balance += int(eur_num_bet_amount * 35)
                                        print(f"BALL DROPPED IN {eur_num_spin_result}")
                                        print(f"Your balance is now ${balance}!!!")
                                        break
                                    elif eur_num_spin_result != eur_num_bet:
                                        balance -= int(eur_num_bet_amount)
                                        print(f"Ball dropped in {eur_num_spin_result}")
                                        print(f"Your balance is now ${balance}...")
                                        break
                            except ValueError:
                                print("Invalid Entry!")
                                continue

                # EUR COLOR BET
                elif bet_type == "C":
                    while True:
                        try:
                            eur_color_bet = str(input("Type 'R' to bet on Red, type 'B' to bet on black...\n")).title()
                            # EUR RED BET
                            if str(eur_color_bet) == "R":
                                while True:
                                    try:
                                        # EUR RED BET AMOUNT
                                        eur_color_bet_amount = int(input("How much $ would you like to bet?\nBet Amount: $"))
                                        if eur_color_bet_amount < 25:
                                            print("Bet must be at least $25")
                                            continue
                                        elif eur_color_bet_amount > balance:
                                            print("You don't have a sufficient balance for this bet!")
                                            continue
                                        else:
                                            # EUR RED BET RESULTS
                                            eur_color_spin_result = choice(eur_color_bet)
                                            # PAYOUT FOR EUR RED BET
                                            if eur_color_spin_result == eur_color_bet:
                                                balance += int(eur_color_bet_amount * 2)
                                                print(f"BALL DROPPED IN RED!!!")
                                                print(f"Your balance is now ${balance}!")
                                                eur_bet_loop()
                                                break
                                            elif eur_color_spin_result != eur_color_bet:
                                                balance -= int(eur_color_bet_amount)
                                                print(f"Ball dropped in black...")
                                                print(f"Your balance is now ${balance}.")
                                                eur_bet_loop()
                                                break
                                    except ValueError:
                                        print("Invalid Entry!")
                                        continue

                            # EUR BLACK BET
                            elif str(eur_color_bet) == "B":
                                while True:
                                    try:
                                        # EUR BLACK BET AMOUNT
                                        eur_color_bet_amount = int(input("How much $ would you like to bet?\nBet Amount: $"))
                                        if eur_color_bet_amount < 25:
                                            print("Bet must be at least $25")
                                            continue
                                        elif eur_color_bet_amount > balance:
                                            print("You don't have a sufficient balance for this bet!")
                                            continue
                                        else:
                                            # EUR BLACK BET RESULTS
                                            eur_color_spin_result = choice(eur_color_bet)
                                            # PAYOUT FOR EUR BLACK BET
                                            if eur_color_spin_result != eur_color_bet:
                                                balance += int(eur_color_bet_amount * 2)
                                                print(f"BALL DROPPED IN BLACK!!!")
                                                print(f"Your balance is now ${balance}!")
                                                eur_bet_loop()
                                                break
                                            elif eur_color_spin_result == eur_color_bet:
                                                balance -= int(eur_color_bet_amount)
                                                print(f"Ball dropped in red...")
                                                print(f"Your balance is now ${balance}.")
                                                eur_bet_loop()
                                                break
                                    except ValueError:
                                        print("Invalid entry! Please try again...")
                                        continue
                        except TypeError:
                            print("Invalid Entry!")
                            continue
            except ValueError:
                print("Invalid Entry, please enter an integer.")
                continue

    if __name__ == "__main__":
        main1()
###########################################################################################
# DICE GAME
from random import choice

roll_results = ("1", "2", "3", "4", "5", "6")
balance = 0
def play_dice():
    play_or_rules = str(input("Welcome to our Dicey Dice Roller game!\n"
                              "Type 'P' to play, 'R' to view the rules, or 'Q' to quit...\n")).title()
    if play_or_rules == "Q":
        print("Goodbye! 👋🏽")
        game_choice()

    elif play_or_rules == "P":
        dep_amount = int(input("Enter your starting balance!\nMin. Deposit = $25\n$"))
        deposit(dep_amount)
        bet_amount = int(input("Place your bet!\n$25, $50, $100, $250, $500, $750, $1000\n$"))
        dice_roller_loop(bet_amount)

    elif play_or_rules == "R":
        print("Dicey Dice Roller!\nHere at Habibi Slots, we offer our customers a "
              "chance to take on the house 1v1 with Dicey Dice Roller!\n"
              "Simply place your bet and roll!\nThe house bot will also roll a die "
            "with values ranging from 1-6. Whoever rolls the highest number wins!\n"
            "Thanks for play Dicey Dice Roller at the Habibi Casino! Good luck out there!")
        play_dice()

# FIRST FUNCTION = DEPOSIT
def deposit(dep_amount):
    global balance
    balance += dep_amount
    return f"Your balance is now ${balance}!"

# 2nd FUNCTION - PAYOUT WIN
def payout_win(bet_amount):
    global balance
    balance += bet_amount
    print(f"Your balance is now ${balance}!")
    return balance


# 3rd FUNCTION - PAYOUT LOSS
def payout_loss(bet_amount):
    global balance
    balance -= bet_amount
    print(f"Your balance is now ${balance}...")
    return balance

def dice_roller_loop(bet_amount):
    global balance
    while True:
        try:
            user_move = str(input("Type 'R' to roll or 'C' to cashout...\n")).title()
            if user_move == "R":
                user_roll = int(choice(roll_results))
                bot_roll = int(choice(roll_results))
                if user_roll > bot_roll:
                    print(f"You rolled a {user_roll}...")
                    print(f"Bot rolled a {bot_roll}!!!")
                    payout_win(bet_amount)
                    continue
                elif user_roll < bot_roll:
                    print(f"You rolled a {user_roll}...")
                    print(f"Bot rolled a {bot_roll}")
                    payout_loss(bet_amount)
                    continue
                else:
                    print(f"You rolled a {user_roll}...")
                    print(f"Bot rolled a {bot_roll}")
                    print(f"TIE! Your balance is still ${balance}")
                    continue

            elif user_move == "C":
                print(f"Very well... here is your ${balance}, good game!")
                break
            if balance <= 0:
                print(f"BUST! Your balance is now ${balance}!")
                play_dice()
            else:
                play_dice()
        except ValueError:
            print("Invalid Entry!")

def play_blackjack():
    # BLACKJACK
    from random import choice

    balance = 0
    cards = ("A", "K", "J", "Q", 2, 3, 4, 5, 6, 7, 8, 9)
    royals = "K", "J", "Q", "A"
    numbers =  2, 3, 4, 5, 6, 7, 8, 9, 10
    suits = ("♦", "♠", "♣", "❤")

    # DEALER HAND DRAW
    dealer_card1 = choice(cards)
    dealer_card2 = choice(cards)
    dealer_hand_value = 0

    # USER HAND DRAW
    # user_card1 = choice(cards)
    # user_card2 = choice(cards)
    user_hand_value = 0
    # DEPOSIT LOOP
    while True:
        try:
            deposit = int(input("Welcome to Blazin' Blackjack!\nMake a Deposit to start playing! Min. Bet = $5\n"
                                "\nDeposit: $"))
            if deposit < 5:
                raise ValueError("Invalid Entry, amount must be at least $5.")
            else:
                balance += deposit
                print(f"Your balance is now ${balance}!")
                break
        except ValueError:
            print("Invalid Entry, please enter an integer value.")
    # BET LOOP
    while True:
        try:
            user_hand_value = 0
            dealer_hand_value = 0
            bet_or_quit = str(input("\nType 'B' to Bet or 'C' to Cashout!\n")).title().strip()
            if bet_or_quit == "B":
                bet = int(input("Place your bet! Min. Bet = $5!\nBet Amount: $"))
                if bet > balance:
                    print("Invalid Bet, amount exceed balance.")
                elif bet < 5:
                    print("Invalid Bet, Minimum Bet = $5.")
                else:
                    # IF DEALER 1st CARD IS ROYAL
                    if dealer_card1 in royals:
                        dealer_card1 = 10
                        dealer_hand_value += int(dealer_card1)

                    # IF DEALER 1st CARD IS NUM
                    elif dealer_card1 in numbers:
                        dealer_hand_value += int(dealer_card1)

                    # IF DEALER 1st CARD IS ACE
                    elif dealer_card1 == "A":
                        dealer_card1 = 11
                        dealer_hand_value += int(dealer_card1)

                    # IF DEALER 2nd CARD IS ROYAL
                    if dealer_card2 in royals:
                        dealer_card2 = 10
                        dealer_hand_value += int(dealer_card2)

                    # IF DEALER 2nd CARD IS NUM
                    elif dealer_card2 in numbers:
                        dealer_hand_value += int(dealer_card2)

                    # IF DEALER 2nd CARD IS ACE
                    elif dealer_card2 == "A":
                        dealer_card2 = 11
                        dealer_hand_value += int(dealer_card2)

                    # DEALER BLACKJACK
                    if dealer_hand_value == 21:
                        print(f"\nDealer Hand: |{dealer_card1}{choice(suits)}| = {dealer_hand_value}\n💰🅱🅻🅰🅲🅺🅹🅰🅲🅺")
                        balance -= bet
                        print(f"\nYour balance is now ${balance}")
                        break
                    else:
                        print(f"\nDealer Hand: |{dealer_card1}{choice(suits)}|")
                    ########################################################################################################
                        user_card1 = choice(cards)
                        user_card2 = choice(cards)
                        # IF USER 1st CARD IS ROYAL
                        if user_card1 in royals:
                            user_card1 = 10
                            user_hand_value += int(user_card1)

                        # IF USER 1st CARD IS NUM
                        elif user_card1 in numbers:
                            user_hand_value += int(user_card1)

                        # IF USER 1st CARD IS ACE
                        elif user_card1 == "A":
                            while True:
                                try:
                                    ace_choice = int(input(f"\nYou drew an Ace... Make it 1 or 11?\nYour Hand:"
                                                           f" {user_card2}{choice(suits)}"
                                                           f"\nAce Value:"))
                                    if ace_choice < 1:
                                        raise ValueError("Invalid Entry! 1 or 11?")

                                    elif ace_choice > 11:
                                        raise ValueError("Invalid Entry! 1 or 11?")
                                    else:
                                        user_hand_value += int(ace_choice)
                                        break
                                except ValueError:
                                    print("Invalid Entry!")

                        # IF USER 2nd CARD IS ROYAL
                        if user_card2 in royals:
                            user_card2 = 10
                            user_hand_value += int(user_card2)

                        # IF USER 2nd CARD IS NUM
                        elif user_card2 in numbers:
                            user_hand_value += int(user_card2)

                        # IF USER 2nd CARD IS ACE
                        elif user_card2 == "A":
                            while True:
                                try:
                                    ace_choice = int(input(f"\nYou drew an Ace... Make it 1 or 11?\nYour Hand:"
                                                           f" {user_card1}{choice(suits)}"
                                                           "\nAce Value: "))
                                    if ace_choice < 1:
                                        raise ValueError("Invalid Entry! 1 or 11?")
                                    elif ace_choice > 11:
                                        raise ValueError("Invalid Entry! 1 or 11?")
                                    else:
                                        user_hand_value += int(ace_choice)
                                        break
                                except ValueError:
                                    print("Invalid Entry!")
                        # USER BLACKJACK
                        if user_hand_value == 21:
                            print(f"\nUser Hand: |{user_card1}{choice(suits)}| |{user_card2}{choice(suits)}| = "
                                  f"{user_hand_value}"
                                  f"\n💰🅱🅻🅰🅲🅺🅹🅰🅲🅺")
                            balance += int(bet)
                            print(f"\nYour balance is now ${balance}")
                            break
                        else:
                            print(f"\nUser Hand: |{user_card1}{choice(suits)}|{user_card2}{choice(suits)}| ="
                                  f" {user_hand_value}")
                    # HIT OR STAY LOOP
                    while True:
                        try:
                            if user_hand_value < 21:
                                user_move = str(input("\nType 'H' to Hit or 'S' to Stay!\n")).title().strip()
                                if user_move == "H":
                                    user_card3 = choice(cards)
                                    if user_card3 in numbers:
                                        user_hand_value += int(user_card3)
                                        print(f"User Hand: |{user_card1}{choice(suits)}|{user_card2}{choice(suits)}|"
                                              f"{user_card3}"
                                              f"{choice(suits)}| = {user_hand_value}\nDealer Hand: {dealer_card1}")
                                        if user_hand_value == 21:
                                            print(f"\nUser Hand: |{user_card1}{choice(suits)}||{user_card2}{choice(suits)}| "
                                                  f"= {user_hand_value}"
                                                  f"\n💰🅱🅻🅰🅲🅺🅹🅰🅲🅺")
                                            balance += int(bet)
                                            print(f"\nYour balance is now ${balance}")
                                            break
                                        # IF USER BUSTS
                                        elif user_hand_value > 21:
                                            print(f"BUST!")
                                            balance -= bet
                                            print(f"\nYour balance is now ${balance}")
                                            break
                                        else:
                                            pass
                                    elif user_card3 in royals:
                                        user_card3 = 10
                                        user_hand_value += int(user_card3)
                                        print(f"User Hand: |{user_card1}{choice(suits)}|{user_card2}{choice(suits)}|"
                                              f"{user_card3}"
                                              f"{choice(suits)}| = {user_hand_value}")

                                        if user_hand_value == 21:
                                            print(f"\nUser Hand: |{user_card1}{choice(suits)}|{user_card2}{choice(suits)}|"
                                                  f" = {user_hand_value}"
                                                  f"\n💰🅱🅻🅰🅲🅺🅹🅰🅲🅺")
                                            balance += int(bet)
                                            print(f"\nYour balance is now ${balance}")
                                            break

                                        # IF USER BUSTS
                                        elif user_hand_value > 21:
                                            print(f"BUST!")
                                            balance -= bet
                                            print(f"\nYour balance is now ${balance}")
                                            break
                                    else:
                                        print(f"Your Hand: |{user_card1}{choice(suits)}|{user_card2}{choice(suits)}|"
                                              f" = {user_hand_value}")
                                        print(f"\nDealer Hand: |{dealer_card1}{choice(suits)}|{dealer_card2}{choice(suits)}| "
                                              f"= {dealer_hand_value}")
                                        # IF USER BUSTS
                                        if user_hand_value > 21:
                                            print(f"BUST!")
                                            balance -= bet
                                            print(f"\nYour balance is now ${balance}")
                                            break


                                elif user_move == "S":
                                    print(f"\nYour Hand: |{user_card1}{choice(suits)}|{user_card2}{choice(suits)}|"
                                          f" = {user_hand_value}")
                                    print(f"\nDealer Hand: |{dealer_card1}{choice(suits)}|{dealer_card2}{choice(suits)}|"
                                          f" = {dealer_hand_value}")
                                    if user_hand_value > dealer_hand_value:
                                        balance += bet
                                        print(f"\nYOU WIN! Your balance is now ${balance}!")
                                        break
                                    elif user_hand_value < dealer_hand_value:
                                        balance -= bet
                                        print(f"\nYour balance is now ${balance}!")
                                        break
                                    elif user_hand_value == dealer_hand_value:
                                        print("YOU TIED!")
                                        print(f"Your balance is still ${balance}!")

                            elif user_hand_value < 0:
                                print(f"Your Balance: $0")
                                print("Sorry, better luck next time 👋🏽...")
                        except ValueError:
                            print("Invalid Entry!")

            elif bet_or_quit == "C":
                cash_out = str(input("Are you sure you'd like to cashout?\nYes or No?\n")).title()
                if cash_out == "Yes":
                    print(f"Very well... here's your ${balance}\nGOOD GAME!")
                    break
                elif cash_out == "No":
                    print("Atta boy! Get back in there CHAMP!")
                    continue

        except ValueError:
            print("Invalid Entry, please enter an integer value.")
#####################################################################################
# COMMAND LINE INTERFACE
def game_choice():
    while True:
        try:
            print("\nWelcome to the Habibi Casino!\n")
            game_choice = input("Which game would you like to play?\n"
                        "\nType 1 for Top Dollar Slots,\n"
                        "Type 2 for Roulette,\n"
                            "Type 3 for Dicey Dice Roller,\n"
                            "Type 4 for Blazin' Blackjack!\n")

            if game_choice == "1":
                play_slots()
                continue

            elif game_choice == "2":
                play_roulette()
                continue

            elif game_choice == "3":
                play_dice()
                continue

            elif game_choice == "4":
                play_blackjack()
                continue

        except ValueError:
            print("Invalid input. Please choose a valid option.")
if __name__ == "__main__":
    game_choice()