
import random
from hangman_words import word_list
from hangman_stages import stages, logo
from replit import clear


print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

display = []
for _ in range(word_length):
    display += "_"
print(f"{' '.join(display)}")
while not end_of_game:
    guess = input("Guess a letter: ").lower()
   
    clear()
    
    if guess in display:
      print("You've already guessed", guess)
    
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:

        lives -= 1
        print("You guessed",guess,"that's not in the word. You lose a life.")
        if lives== 3:
          print("Hint: It's an Emotion ;)")
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print("The word was",chosen_word)


    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

 
    print(stages[lives])