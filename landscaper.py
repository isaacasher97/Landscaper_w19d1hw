#players starting amount
money = 0
has_scissors = False

#Define function to cut lawn using teeth
def cut_lawn_teeth():
    global money
    money += 1
    print("You Spent the day cutting lawns with your teeth and earned $1.")

#Define funtion to cut lawn using scissors
def cut_lawn_scissors():
    global money
    money += 5
    print("You spent the day cutting lawns with rusty scissors and earned $5.")

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
    print("1. Cut the lawn with your teeth")
    print("2. Cut the lawn with rusty scissors")
    print("3. Buy rusty scissors")
    print("4. Quit")

    choice = input("Enter your choice: ")


    if choice == '1':
        cut_lawn_teeth()
    elif choice == '2':
        if has_scissors:
            cut_lawn_scissors()
        else:
            print("You don't have rusty scissors. Buy them first.")
    elif choice == '3':
        buy_scissors()
    if choice == '4':
        print("Thanks for playing landscaper!")
        break