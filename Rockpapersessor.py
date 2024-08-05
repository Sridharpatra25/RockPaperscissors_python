import random

print(" Hey buddy, welcome to Gaming Hub!")
print("     --- RULES ---")
print("""Rock vs Paper -> Paper wins
Rock vs Scissors -> Rock wins
Paper vs Scissors -> Scissors wins\n""")

while True:
    print("Enter your choice\n 1- Rock\n 2- Paper\n 3- Scissors")
    choice = int(input("Enter your choice: "))

    while choice > 3 or choice < 1:
        print("Please enter a valid input")
        choice = int(input("Enter your choice: "))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    print(f"Your choice is: {choice_name}")

    print("Now it's the computer's turn...")
    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print(f"Computer's choice is: {comp_choice_name}")
    print(f"{choice_name} vs {comp_choice_name}")

    if comp_choice_name == choice_name:
        print("-- It's a DRAW --")
        result = "DRAW"
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
        result = "Paper"
    elif (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 2):
        result = "Scissors"
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        result = "Rock"

    if result == "DRAW":
        print("--- It's a draw ---")
    elif result == choice_name:
        print("--- You win ---")
    else:
        print("--- Computer wins ---")

    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break

print("Thanks for playing!")


    



            
