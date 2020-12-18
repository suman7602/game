a = input("Please enter your name=")
print("wellcome",a)
print("Please select a choice from below")
choice = (int(input("\n press '1' for rock \n press '2' for paper \n press '3' for sizer ")))
if choice == 1:
    usr_turn ='Rock'
    print("your choice= rock")
elif choice == 2:
    usr_turn = 'Paper'
    print("your choice= Paper")
elif choice ==3:
    usr_turn = 'Scissor'
    print("your choice= scissor")
import random
choice = random.randint(4, 6)
if choice == 4:
    mac_turn = 'Rock'
    print("Computer choice= rock")
elif choice == 5:
    mac_turn = 'Paper'
    print("Computer choice= paper")
elif choice == 6:
    mac_turn ='Scissor'
    print("Computer choice= scissor")
if usr_turn == 'Rock' and mac_turn == 'Scissor':
    print(a,"You win")
elif usr_turn == 'Paper'and mac_turn == 'Rock':
    print(a,"You win")
elif usr_turn == 'Scissor'and mac_turn =='Paper':
    print(a,"You win")
elif usr_turn =='Scissor'and mac_turn =='Rock':
    print(a,"You lost")
elif usr_turn =='Rock'and mac_turn =='Paper':
    print(a,"You lost")
elif usr_turn =='Paper'and mac_turn =='Scissor':
    print(a,"You Lost")
elif usr_turn =='Rock'and mac_turn =='Rock':
    print(a,"Match Draw")
elif usr_turn =='Paper'and mac_turn =='Paper':
    print(a,"Match Draw")
elif usr_turn =='Scissor'and mac_turn =='Scissor':
    print(a,"Match Draw")