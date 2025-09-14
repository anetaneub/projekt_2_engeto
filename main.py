import random

# Generování náhodného čísla
def generate_number():
    """
    Vygeneruje čtyřciferné náhodné číslo s unikátními číslicemi.
    První číslice nikdy není nula.
   Returns:
        str: řetězec se 4 číslicemi
    """
    digits = random.sample("0123456789", 4)
    if digits[0] == "0":
        digits[0], digits[1] = digits[1], digits[0]  # prohoď první dvě číslice
    return "".join(digits)

# Funkce pro výpočet bulls a cows
def get_bulls_and_cows(secret, guess):
    """
Porovná tajné číslo s tipem hráče a vrátí počet bulls a cows.
Returns:
    tuple: (bulls, cows)
     """
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    return bulls, cows

# Funkce pro validaci tipu
def is_valid_guess(guess):
    """
    Ověří, zda tip je platný.
    Returns:
        bool: True pokud tip splňuje podmínky
    """
    return (
        guess.isdigit()
        and len(guess) == 4
        and len(set(guess)) == 4
        and guess[0] != "0"
    )


# Funkce pro správný tvar slova 
def plural_s(n, word):
    """
    Vrátí správný tvar slova podle počtu.
    Returns:
        str: jednotné nebo množné číslo slova
    """
    return word if n == 1 else word + "s"

#Funkce pro načtení vstupu
def get_input(prompt):
    """
    Načte vstup od uživatele (funguje v Pythonu 2 i 3).
    Returns:
        str: text zadaný uživatelem
    """
    try:
        return input(prompt)          
    except NameError:
        return raw_input(prompt)     

# Hlavní herní smyčka
def play_game():
    """
    Spustí hru Bulls and Cows v konzoli.
    """
    secret = generate_number()
    attempts = 0
    separator = "-" * 47
    
    print("Hi there!\n{0}\nI've generated a random 4 digit number for you.\n"
          "Let's play a bulls and cows game.\n{0}".format(separator))

    while True:
        guess = get_input("Enter a number: ")
        print(separator)

        if not is_valid_guess(guess):
            print("Please enter a valid 4-digit number with unique digits and no leading zero.")
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
