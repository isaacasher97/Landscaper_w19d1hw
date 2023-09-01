#players starting amount
money = 0

#Define function to cut lawn using teeth
def cut_lawn():
    global money
    money += 1
    print("You Spent the day cutting lawns with your teeth and earned $1.")

# Main game loop
while True:
    print(f"Your current balance: ${money}")
    print("What do you want to do?")
    print("1. Cut the lawn")
    print("2. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        cut_lawn()
    if choice == '2':
        print("Thanks for playing!")
        break
