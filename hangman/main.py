"""Simple Hangman console application."""

import random

def play(word):
    max_tries = 6
    num_tries = 0
    guess = input("Guess a letter: ").lower()
    while(guess != word):
        num_tries+=1
        pass
    print(f"You successfully saved the man! The word was indeed {word}")

def main():
    #parse words.txt file
    words = []
    with  open("words.txt", "r") as lines:
        for line in lines:
            #remove words that are 2 characters or shorter
            if(len(line) > 2):
                words.append(line)

    random_word = random.choice(words).lower()
    play(random_word)


if __name__ == "__main__":
    main()