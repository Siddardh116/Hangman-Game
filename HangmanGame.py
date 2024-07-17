import random

def get_random_word(word_list):
    """Selects a random word from the provided list."""
    return random.choice(word_list)

def display_word(word, guessed_letters):
    """Displays the word with guessed letters revealed and the rest as underscores."""
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word_list = ["python", "hangman", "challenge", "programming", "openai"]
    word = get_random_word(word_list)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 3
    
    print("Welcome to Hangman!")
    print(f"You have {max_incorrect_guesses} incorrect guesses allowed.")
    
    while incorrect_guesses < max_incorrect_guesses:
        print(display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess. You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")
        
        print()
    
    if incorrect_guesses == max_incorrect_guesses:
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()
