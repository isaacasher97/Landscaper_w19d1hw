#players starting amount
money = 0
has_scissors = False

#Define function to cut lawn using teeth
def cut_lawn():
    global money
    money += 1
    print("You Spent the day cutting lawns with your teeth and earned $1.")

# Define a function to buy rusty scissors
def buy_scissors():
    global money, has_scissors
    if money >= 5 and not has_scissors:
        money -= 5
        has_scissors = True
        print("You bought a pair of rusty scissors.")
    elif has_scissors:
        print("You already have scissors.")
    else:
        print("You don't have enough money to buy scissors.")


# Main game loop
while True:
    print(f"Your current balance: ${money}")
    print("What do you want to do?")
    print("1. Cut the lawn")
    print("2. Buy rusty scissors")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        cut_lawn()
    if choice == '2':
        buy_scissors()
    if choice == '3':
        print("Thanks For Playing Landscaper!")
        break
