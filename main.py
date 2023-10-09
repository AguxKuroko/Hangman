import random
import hangman
import words
import os

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



chosen_word = random.choice(words.word_list)

print(f"Welcome to {hangman.logo}GAME")

print("You have 6 lives - if you run out of them, you lose.")

#print(f'Pssst, the solution is {chosen_word}.')

display = []
for x in chosen_word:
  display.append("_")
  
print(display)

lives = 6


while "_" in display and lives > 0:
  guess = input("Guess a letter: ").lower()
  position = 0
  
  clear_screen()
  
  if guess in display:
   print(f"You have already guessed this letter - '{guess}'. Please try another one.")
  
  if guess in chosen_word: 
    for position in range(len(chosen_word)): 
      if guess == chosen_word[position]:
        display[position] = guess
  elif guess != chosen_word[position]:
    print(f"Your choice of letter - '{guess}' is wrong, try again.You still have {lives-1} left.")
    lives = lives - 1 
  print(hangman.stages[lives])
  print(display)
  
  
if lives > 0:
  print("You win")
else:
  print("You lose")
