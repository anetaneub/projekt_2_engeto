import random

# Generování náhodného čísla
def generate_number():
    digits = list("0123456789")
    result = ""
    while len(result) < 4:
        next_digit = random.choice(digits)
        digits.remove(next_digit)
        result += next_digit
    return (result)

# Funkce pro výpočet bulls a cows
def get_bulls_and_cows(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    return bulls, cows

def plural_s(n, word):
    return word if n == 1 else word + "s"

def get_input(prompt):
    try:
        return input(prompt)          
    except NameError:
        return raw_input(prompt)     

# Hlavní herní smyčka
def play_game():
    secret = generate_number()
    attempts = 0

    separator = "-" * 47
    print("Hi there!\n{0}\nI've generated a random 4 digit number for you.\n"
          "Let's play a bulls and cows game.\n{0}".format(separator))

    while True:
        guess = get_input("Enter a number: ")
        print(separator)

        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("Please enter a valid 4-digit number with unique digits.")
            continue

        attempts += 1
        bulls, cows = get_bulls_and_cows(secret, guess)

        if bulls == 4:
            print("Correct, you've guessed the right number\nin {0} guesses!".format(attempts))
            print(separator)
            print("That's amazing!")
            break
        else:
            if bulls == 0 and cows == 0:
                print("No match – any bull or cow.")
            else:
                print("{0} {1}, {2} {3}".format(
                    bulls, plural_s(bulls, "bull"),
                    cows, plural_s(cows, "cow")))
            print(separator)

# Spuštění hry
if __name__ == "__main__":
    play_game()