import random

rock = '''

           _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
'''
paper ='''
---------------
|             |
|   PAPER     |
|             |
---------------


'''

scissors ='''
  _______
 |       |
 |   ✂   |
 |_______|

 '''

     
user_choice=int(input("enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors"))
if user_choice >= 3 or user_choice < 0:
    print("you entered invalid number, you lose")
else:    
    computer_choice=random.randint(0,2)
    print("Computer choice:")
    print(computer_choice)
    if computer_choice == user_choice:
       print("its a draw") 
    elif computer_choice > user_choice: #2 > 0
       print ("you lose")
    elif user_choice > computer_choice: #2 > 0
       print("you win")
    elif computer_choice == 0 and user_choice ==2:
       print("you lose")
    elif user_choice == 0 and computer_choice ==2:
       print("you win")
                      
