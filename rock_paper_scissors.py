import random


Rock = '''
  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

Paper = '''

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
Scissors = '''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

user_choice = input(
    "Enter your choice (0 for Rock, 1 for Paper, or 2 for Scissors): \n")

# choice of the computer
choices = [Rock, Paper, Scissors]
computer = random.choice(choices)

# start of If statement

if user_choice == "0" and computer == Rock:
    print(Rock+"\n Rock\n" + Rock + "\nRock\n This is a tie.")
elif user_choice == "1" and computer == Rock:
    print(Paper+"\n Paper\n" + Rock + "\nRock\n You win!")
elif user_choice == "2" and computer == Rock:
    print(Scissors+"\n Scissors \n" + Rock + "\nRock\n You loose.")
elif user_choice == "0" and computer == Paper:
    print(Rock+"\n Rock\n" + Paper + "\nPaper\n You loose.")
elif user_choice == "1" and computer == Paper:
    print(Paper+"\n Paper\n" + Paper + "\nPaper\n This is a tie.")
elif user_choice == "2" and computer == Paper:
    print(Scissors+"\n Scissors \n" + Paper + "\nPaper\n You win!")
elif user_choice == "0" and computer == Scissors:
    print(Rock+"\n Rock\n" + Scissors + "\nScissors\n You win! ")
elif user_choice == "1" and computer == Scissors:
    print(Paper+"\n Paper\n" + Scissors + "\nScissors\n You loose.")
elif user_choice == "2" and computer == Scissors:
    print(Scissors+"\n Scissors \n" + computer +
          "\nScissors\n  This is a tie. ")

else:
    print("You Typed an invalid number, You loose.")
