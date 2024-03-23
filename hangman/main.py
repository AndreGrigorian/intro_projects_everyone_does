"""Simple Hangman console application."""

import random
from tkinter import *
from PIL import Image, ImageTk



#initialize global variables
images = ["h1.jpg", "h2.jpg","h3.jpg","h4.jpg","h5.jpg","h6.jpg","h7.jpg","h8.jpg","h9.jpg"]
image_index = 0
guessed_letters = []

def find_all(char, str):
    return [i for i in range(len(str)) if str[i] == char]

def main():

    #parse words.txt file   
    words = []
    with  open("words.txt", "r") as lines:
        for line in lines:
            #remove words that are 2 characters or shorter
            if(len(line.strip()) > 2):
                words.append(line.strip())

    random_word = random.choice(words).lower()
    progress_str = ["_" for x in random_word]  
    # print(random_word) #uncomment for debugging purposes


    #instantiate tkinter and run window
    m = Tk()
    m.title("Hangman")
    #configure grid layout
    m.grid_columnconfigure(0,weight=1)
    m.grid_columnconfigure(1, weight=1)
    #place image

    image = Image.open(f"./images/{images[image_index]}")
    photo =  ImageTk.PhotoImage(image)
    image_label = Label(m, image=photo)
    image_label.grid(row=0,column=0, columnspan=2)
    #progress label
    
    progress = Label(m, text=progress_str)
    progress.grid(row=1, column=0, columnspan=2)
    #text entry
    text_label = Label(m, text="Guess a Letter: ")
    text_label.grid(row=2, column=0, sticky=E)
    text_entry = Entry(m)
    text_entry.grid(row =2, column=1, sticky=W)
    
    #tkinter commands
    def on_submit():
        global image_index
        guess = text_entry.get().lower()
        status_label.configure(text="")# reset status label
        if len(guess) > 1 or guess == "":
            status_label.configure(text="Guess Must be one letter", foreground="red")
            return
        elif guess in random_word:
            #reveal letter location

            index = random_word.find(guess)
            indicies = find_all(guess, random_word)
            for index in indicies:
                progress_str[index] = guess
            progress.configure(text=progress_str)
            #check if user won
            if "_" not in progress_str:
                status_label.configure(text="Congratulations! You Won!", foreground="green")
        elif guess not in random_word:
            #progress hangman photo
            if guess in guessed_letters:
                status_label.configure(text=f"Already guessed '{guess}'. Try something new!", foreground="red")
                return 
            if image_index < len(images)-1:
                image_index = image_index + 1  
                image = Image.open(f"./images/{images[image_index]}")
                photo =  ImageTk.PhotoImage(image)
                image_label.configure(image=photo) 
                image_label.image = photo
            else: 
                status_label.configure(text=f"Hangman died, the word was {random_word}", foreground="red")
        else:
            status_label.configure(text="Something went wrong try again. ", foreground="red")
            return
        
        if(guess not in guessed_letters):
            guessed_letters.append(guess)
            guessed_letters_label.configure(text=f"Guessed letters:\n{','.join(guessed_letters)}")
            
    submit_button = Button(m, text="Ok", command=on_submit)
    submit_button.grid(row=3, column=0, columnspan=2)
    status_label = Label(m, text="")
    status_label.grid(row=4, column=0, columnspan=2)

    guessed_letters_label = Label(m, text="")
    guessed_letters_label.grid(row=5, column=0, columnspan=2)
    m.mainloop()

    


if __name__ == "__main__":
    main()