#players starting amount
money = 0
has_scissors = False
has_push_lawnmower = False
has_fancy_lawnmower = False

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

# Define funtion to cut the lawn using old push lawnmower
def cut_lawn_with_pushmower():
    global money
    money += 50
    print("You spent the day cutting lawns with an old-timey push lawnmower and earned $50.")

# Define a function to cut the lawn using a fancy battery-powered lawnmower
def cut_lawn_with_fancy_lawnmower():
    global money
    money += 100
    print("You spent the day cutting lawns with a fancy battery-powered lawnmower and earned $100.")


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

# Define a function to buy an old-timey push lawnmower
def buy_push_lawnmower():
    global money, has_push_lawnmower
    if money >= 25 and not has_push_lawnmower and has_scissors:
        money -= 25
        has_push_lawnmower = True
        print("You bought an old-timey push lawnmower.")
    elif has_push_lawnmower:
        print("You already have an old-timey push lawnmower.")
    elif not has_scissors:
        print("You can't buy a lawnmower without rusty scissors. Buy scissors first.")
    else:
        print("You don't have enough money to buy a lawnmower.")

# Define a function to buy a fancy battery-powered lawnmower
def buy_fancy_lawnmower():
    global money, has_fancy_lawnmower
    if money >= 250 and not has_fancy_lawnmower and has_push_lawnmower:
        money -= 250
        has_fancy_lawnmower = True
        print("You bought a fancy battery-powered lawnmower.")
    elif has_fancy_lawnmower:
        print("You already have a fancy battery-powered lawnmower.")
    elif not has_push_lawnmower:
        print("You can't buy a fancy lawnmower without an old-timey push lawnmower. Buy the push lawnmower first.")
    else:
        print("You don't have enough money to buy a fancy lawnmower.")


# Main game loop
while True:
    print(f"Your current balance: ${money}")
    print("What do you want to do?")
    print("1. Cut the lawn with your teeth")
    print("2. Cut the lawn with rusty scissors")
    print("3. Cut the lawn with an old-timey push lawnmower")
    print("4. Cut the lawn with a fancy battery-powered lawnmower")
    print("5. Buy rusty scissors")
    print("6. Buy an old-timey push lawnmower")
    print("7. Buy a fancy battery-powered lawnmower")
    print("8. Quit")


    choice = input("Enter your choice: ")


    if choice == '1':
        cut_lawn_teeth()
    elif choice == '2':
        if has_scissors:
            cut_lawn_scissors()
        else:
            print("You don't have rusty scissors. Buy them first.")
    elif choice == '3':
        if has_push_lawnmower:
            cut_lawn_with_pushmower()
        else:
            print("You don't have an old-timey push lawnmower. Buy it first.")
    elif choice == '4':
        if has_fancy_lawnmower:
            cut_lawn_with_fancy_lawnmower()
        else:
            print("You don't have a fancy battery-powered lawnmower. Buy it first.")
    if choice == '5':
        buy_scissors()
    if choice == '6':
        buy_push_lawnmower()
    if choice == '7':
        buy_fancy_lawnmower()
    if choice == '8':
        print("Thanks for playing Landscaper!")
        break