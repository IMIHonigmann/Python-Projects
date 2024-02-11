import os; os.system('cls' if os.name == 'nt' else 'clear')
import random
import re

miss = 'O'
hit = 7
balance = 20
youLost = False
numbers = [0, 0, 7]
random_number = random.choice(numbers)


def processWin():
    global balance
    global youLost
    balance += bettedMoney * 2 #throws an error
    youLost = False

while True:
    deposit = input('How much money would you like to deposit?: \n$')
    balance = re.sub(r'\D', '', deposit)
    
    uSure = input(f'So you wanna deposit {balance}$ is that correct? \n')

    if uSure.lower() == 'yes' or uSure == 'true' or uSure == 'yea':
        balance = int(balance)
        break
    else:
        print('fuck you pay me \n')


while True:
    while True:
        youLost = False
        print(f"You're current balance is {balance}$")

        userInputMoneyBet = input("Please input the amount of money you'd like to bet: \n$")
        bettedMoney = int(userInputMoneyBet)

        if bettedMoney > balance:
            print('Nice try bud you think i\'m stupid? \n')
        else: break

    while True:
        userInputBet = input('Please type in your bet (1-3): \n')
        bet = int(userInputBet)

        if bet > 3 or bet < 1:
            print('There are only 3 rows bro \n')
        elif bettedMoney * bet > balance:
            print("You wanna go bankrupt? You don't have that much money!")
        else: break

    def print_field(field):
        for row in field:
            print("[", end=" ")
            for element in row:
                print(f"{element:d}", end=" ")
            print("]")

    field = [[random.choice(numbers), random.choice(numbers), random.choice(numbers)], 
             [random.choice(numbers), random.choice(numbers), random.choice(numbers)], 
             [random.choice(numbers), random.choice(numbers), random.choice(numbers)]]
    
    loseableMoney = bettedMoney * bet

    print_field(field)

    if bet == 1:
        if field[0][0] == hit and field[0][1] == hit and field[0][2] == hit:
            processWin()
            break
        else:
            youLost = True
    elif bet == 2:
        countRows = 0
        for i in range(0, 2):
            if field[i][0] == hit and field[i][1] == hit and field[i][2] == hit:
                    processWin()
                    break
            else:
                youLost = True
    elif bet == 3:
        countRows = 0
        for i in range(0, 3):
            if field[i][0] == hit and field[i][1] == hit and field[i][2] == hit:
                    processWin()
                    break
            else:
                youLost = True

    balance -= loseableMoney
    
    if youLost:
        print('You won nothing')
        print('You lost ' + str(loseableMoney) + '$')
    else:
        print('You won ' + str(bettedMoney * 2) + '$ yay')

    
    print('Your current balance:' + str(balance) + '$')
    continueBets = input('Would you like to cash out?: \n')
    
    if continueBets == 'yes':
        print('Goodbye Hope we see you next time!')
        break
    
