from replit import db
from random import random
from os import system

num_words = len(db.keys())

# DATA
# [x] a bunch of words for the program to pick
# key = number
# value = word

# FUNCTIONALITY
# display the game
# pick a word
# --- turn --
# ask the player for a letter
# know a character is in the word
# update the letters found
# remember the number of tries the player has
# determine if the player loses, wins, or chooses again

def pick_a_word():
  random_number = 0
  while not str(random_number) in db.keys():
    # from 0 to 1
    random_number = random()
    # change random_number to 1 -> num_words
    random_number = 1 + round(random_number * (num_words-1))
    # get word from database
  word = db[str(random_number)]
  return word

word = pick_a_word()
word_length = len(word)

# sets all letters to unguessed
word_dict = {}
for letter in word:
  word_dict[letter] = False

def display_game(wrong, guesses_left):
  system("clear")
  if wrong:
    print("\nThat's not a letter. Try again!")
    print("You have", guesses_left, "guesses left")
  print("\n", end="")
  for letter in word:
    if word_dict[letter]:
      print(letter, end="")
    else:
      print("_", end="")
  print("\n\n")
  
  print("Guess any letter!\n")

#start game
game_over = False
wrong = False
num_guesses = 0
while(not game_over):
  # ask the user for a letter
  display_game(wrong, (word_length - 1) - num_guesses)
  guess = input("")

  if guess in word:
    word_dict[guess] = True
    wrong = False
  else:
    wrong = True
    num_guesses = num_guesses + 1

  has_won = True
  for key,val in word_dict.items():
    has_won = has_won and val
  
  if has_won:
    game_over = True
  
  if num_guesses == word_length - 1:
    print("You lost! The word was", word)
    game_over = True

if has_won:
  system("clear")
  print(word, "\n")
  print("You won!")