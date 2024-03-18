"""Simple number guessing game with different difficulties"""

import random

def play(mode):
    """Runs Game cylce until a loss or win
    
    Args:
        mode (int): Difficulty level.  1- easy, 2- moderate, 3-Hard,
    Returns:
        None
    """
    
    if mode == 1:
        range = 10
    if mode == 2:
        range = 50
    if mode == 3:
        range = 100
    
    secret_number = random.randint(1, range)
    max_tries = 3
    num_of_tries = 0
    # print(secret_number)    ----uncomment for debugging purposes----
    while num_of_tries < max_tries:
        user_guess = int(input(f"Num of tries left: {max_tries - num_of_tries}. Enter your guess between 1 and {range}: "))
        if user_guess == secret_number:
            print(f"You guessed {secret_number} correctlty in {num_of_tries+1} tries!")
            return
        else:
            print("Not Quite. Try again")
        num_of_tries+=1
    print(f"You ran out of tries, the number was {secret_number}")
    

   



def main():
    print("1. Easy\n2. Moderate\n3. Hard\n4. Quit")
    try: 
        mode = int(input("Select Option: "))
    except:
        print("Enter valid input please")
    
    
    while mode != 4:
        if(mode-1 in range(3)):#Ensure user inputs either 1, 2, or 3
            play(mode)
        else:
            print("Not an option")
        
        try: 
            mode = int(input("Select Option: "))
        except:
            print("Enter valid input please")
   

    

if __name__ == "__main__":
    main()