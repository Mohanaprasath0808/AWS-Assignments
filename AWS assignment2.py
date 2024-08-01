import random

def generate_number():
    return str(random.randint(1000, 9999))

def count_cows_and_bulls(secret, guess):
    cows = sum(1 for s, g in zip(secret, guess) if s == g)
    bulls = sum(1 for g in guess if g in secret) - cows
    return cows, bulls

def cows_and_bulls_game():
    secret_number = generate_number()
    guesses = 0
    
    print("Welcome to the Cows and Bulls Game!")
    
    while True:
        guess = input("Enter a 4-digit number: ")
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input. Please enter a 4-digit number.")
            continue
        
        guesses += 1
        cows, bulls = count_cows_and_bulls(secret_number, guess)
        
        if cows == 4:
            print(f"Congratulations! You've guessed the correct number {secret_number} in {guesses} guesses.")
            break
        else:
            print(f"{cows} cows, {bulls} bulls")

if __name__ == "__main__":
    cows_and_bulls_game()
