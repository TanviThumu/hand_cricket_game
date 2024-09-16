def bowling():
   import random
   print("You chose Bowling.")
   comp_score = 0
   out = False
   while not out:
      user = int(input("Enter your ball (1 to 10): "))
      computer=random.randint(1,10)
      print(f"Computer chose {computer}")

      if user == computer:
         print("Computer is out!")
         out=True
      else:
         comp_score += computer
   print(f"Computer score is {comp_score}")
   print("Now it's your turn to bat.")

   user_score=0
   out= False
   while not out:
      user=int(input("Enter your run (1 to 10): "))
      computer=random.randint(1,10)
      print(f"Computer chose {computer}")

      if user ==  computer:
         print("You are out.")
         out=True
      elif comp_score < user_score:
         out=True
      else:
         user_score+=user
   print(f"Your total score is {user_score}")

   if comp_score > user_score:
      print("Computer won the match. Best luck next time.")
   elif comp_score < user_score:
    print("You won the match.")
   else:
    print("It's a draw.")
   

def batting():
   import random
   print("You chose Batting.")
   user_score = 0
   out = False

   while not out:
    user = int(input("Enter your run (1 to 10): "))
    computer = random.randint(1, 10)
    print(f"Computer chose {computer}")
    
    if user == computer:
        print("You are out!")
        out = True
    else:
        user_score += user

   print(f"Your total score is {user_score}")
   print("Now it's your turn to bowl.")

   comp_score = 0
   out = False

   while not out:
    user = int(input("Enter your ball (1 to 10): "))
    computer = random.randint(1, 10)
    print(f"Computer chose {computer}")
    if user == computer:
        print("Computer is out!")
        out = True
    elif comp_score>user_score:
        out=True  
    else:
        comp_score += computer
   print(f"Computer's total score is {comp_score}")

   if comp_score > user_score:
      print("Computer won the match. Best luck next time.")
   elif comp_score < user_score:
    print("You won the match.")
   else:
    print("It's a draw.")


def choice():
    user = input("1. Bowling 2. Batting\n").lower()
    
    if user == "1" or user == "bowling":
        bowling()
    elif user == "2" or user == "batting":
        batting()
    else:
        print("Please enter a valid choice.")
        choice() 
    
    again = input("Do you want to play again? (Yes/No): ").lower()
    if again == "yes":
        choice()
    elif again == "no":
        print("Hope you enjoyed the game. Thank you!")
    else:
        print("Invalid input.")
        choice()  


choice()

