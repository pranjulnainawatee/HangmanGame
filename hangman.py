import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    letters_used = []                       #list containing guessed letters
    tries = 6
    print("---------------LET'S PLAY HANGMAN!--------------")

    while not guessed and tries > 0:
        print(display_hangman(tries))
        print("Current word:", word_completion)
        print("------------------------------------------------")
        guess = input("\nGUESS A LETTER: ").upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in letters_used:
                print("You have already used that letter. Please try again!")
            elif guess not in word:
                print(guess, "is not in the word. Please try again!")
                tries = tries - 1
                letters_used.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                letters_used.append(guess)
                word_as_list = list(word_completion)            #to update occurrences of guess
                #to find all indices where 'guess' occur in 'word'
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:               #to replace each underscore at index with 'guess'
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        else:
            print("Not a valid guess. Please try again!")
        print("Letters used:",' '.join(letters_used))

    if guessed == True:
        print("\nCongrats, you guessed the word, "+ word + "! YOU WIN!")
    else:
        print("\nSorry, you ran out of lives. The word was " + word + ".")

def display_hangman(tries):
    stages = [  # final state: head, body, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, body, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, body, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, body, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and body
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("DO YOU WANT TO PLAY AGAIN? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()