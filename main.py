import random
from replit import clear
from art import logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) ==2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.remove(1)
  return sum(cards)

def compare(player_score,computer_score):
  if player_score > 21 and computer_score > 21:
    return "You went over. You lose "
  
  if player_score == computer_score:
    return "Its a Draw! Try again"
  elif computer_score == 0:
    return "You Lose!"
  elif player_score == 0:
    return "You Win!"
  elif player_score > 21:
    return "You Lose!"
  elif 21 < computer_score:
    return "You Win!"
  if player_score > computer_score:
    return "You Win!"
  else:
    return "You Lose!"

def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  is_gameover = False
  while not is_gameover:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print("------------------------------------------------------------------")
    print(f"----> Your cards : {user_cards} Current Score : {user_score}")
    print(f"----> COmputer cards: {computer_cards[0]}")
    print("------------------------------------------------------------------")
    
    if user_score == 0 or computer_score ==0 or user_score > 21:
      is_gameover = True
    else :
      user_choice = input("'y' --> another card or 'n'--> pass:\n")
      if user_choice == "y":
        user_cards.append(deal_card())
      else:
        is_gameover = True
  
  while computer_score !=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print("------------------------------------------------------------------")
  print(f"----> Your FInal cards : {user_cards} FInal Score : {user_score}")
  print(f"----> COmputer FInal cards: {computer_cards} Computer FInal Score : {computer_score}")
  print("------------------------------------------------------------------")
  print(compare(user_score,computer_score))

while input("Want to play Black jack: YES --> 'y' NO -->'n':\n") =='y':
  clear()
  play_game()

  

