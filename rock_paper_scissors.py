
import random

comp_choice = random.randint(0,2)
user_choice = int(input("Enter the choice: 0 for Rock, 1 for Paper, 2 for Secissor: "))
print("comp choice")
print(comp_choice)

if user_choice == 0 and comp_choice == 0:
    print("Draw")
elif user_choice == 0 and comp_choice == 1:
    print("comp wins")
elif user_choice == 0 and comp_choice == 2:
    print("user wins")
elif user_choice == 1 and comp_choice == 0:
    print("user wins")
elif user_choice == 1 and comp_choice == 1:
    print("Draw")
elif user_choice == 1 and comp_choice == 2:
    print("comp wins")
elif user_choice == 2 and comp_choice == 0:
    print("comp wins")
elif user_choice == 2 and comp_choice == 1:
    print("user wins")
elif user_choice == 2 and comp_choice == 2:
    print("Draw")
else:
    print("Invalid Number, you lose")