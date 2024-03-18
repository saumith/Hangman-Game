import random
from hangman_words import word_list
from hangman_art import stages, logo
print(logo)
chosen_word = random.choice(word_list)

word_length= len(chosen_word)
lives=6
display=[]
for i in range(word_length):
  display.append('_ ')
end=False
while not end:
  char=""
  for i in display:
    char+=i
  print(char)
  guess = input("\nGuess a letter: ").lower()
  
  for i in range(word_length):
      letter=chosen_word[i]
      if letter == guess:
        display[i] = guess
  if guess not in chosen_word:
      lives-=1
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
      print(stages[lives])
      if lives==0:
        end=True
        print("You lose")
        print(f"The word is {chosen_word}")
        
  if '_ ' not in display:
    end=True
    print(f"You guessed it, the word is {chosen_word}")
    print("You win")
  
