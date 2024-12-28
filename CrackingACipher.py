# November 15, 2023

import os

# Gets an index representing the current letter cycled by the cipher amount, then converts it to a letter
def encrypt_letter(letter: str, cipher: int):
    index = cycle(get_letter_index(letter), cipher)
    return return_letter_by_index(index)

# The reverse of encrypt_letter
def decrypt_letter(letter: str, cipher: int):
    return encrypt_letter(letter, -cipher) 

# calls the encrypt letter function for every letter in the string
def encrypt_string(string: str, cipher: int):
    encrypted_letters = [encrypt_letter(letter, cipher) for letter in string]
    return ''.join(encrypted_letters)

# The reverse of encrypt_string
def decrypt_string(string: str, cipher: int):
    return encrypt_string(string, -cipher)

# Inputs a letter, and outputs an int representing that letter
def get_letter_index(letter: str):
    return ord(letter) - ord('a')

# Takes an int and returns a letter
def return_letter_by_index(letter: int):
    return chr(letter + ord('a'))

# Calculates the likelihood that the letter occurs 
def get_letter_likelihood(letter: str):
    letter_likelihoods = {
            'e': 12.7,
            't': 9.1,
            'a': 8.2,
            'o': 7.5,
            'i': 7.0,
            'n': 6.7,
            's': 6.3,
            'h': 6.1,
            'r': 6.0,
            'd': 4.3,
            'l': 4.0,
            'c': 2.8,
            'u': 2.8,
            'm': 2.4,
            'w': 2.4,
            'f': 2.2,
            'g': 2.0,
            'y': 2.0,
            'p': 1.9,
            'b': 1.5,
            'v': 0.98,
            'k': 0.77,
            'j': 0.15,
            'x': 0.15,
            'q': 0.095,
            'z': 0.074
            }
    return letter_likelihoods[letter]

# Iterates through all the letters in the inputted text and calculates how likely they are. 
# This function returns how likely the string is correct
def get_likelihood_score(text: str):
    return sum(map(get_letter_likelihood, text))

# Takes an integer and cycles it by the specified amount.
def cycle(index: int, ammount: int, base: int = 26):
    return (index + ammount) % base

def check_cipher_itteration(text: str, cipher:int):
    # Creates a tuple entry containing the cipher the score it got
    own_value = (cipher, get_likelihood_score(decrypt_string(text, cipher)))
    # If the cipher is a cycle of 26, it assumes it is the best to prevent infinite recursion
    if cipher >= 26:
        return own_value
    # Runs this very function and stores it's return value
    next_cipher = check_cipher_itteration(text, cipher+1)
    # Checks if this function got a better score, or one further up the chain.
    # It returns the highest scoring cipher tuple
    if own_value[1] > next_cipher[1]:
        return own_value
    else:
        return next_cipher

# Returns a string with only a-z letters
def sanitize_string(new_string: str):
    lower_string = new_string.lower()
    return ''.join(x for x in lower_string if (x in "abcdefghijklmnopqrstuvwxyz"))

# The core function. It takes a string encrypted by the cipher and returns an un-encrypted string
def crack_cipher(input_text):
    text_to_decrypt = sanitize_string(input_text)
    correctCypher = check_cipher_itteration(text_to_decrypt, 0) 
    result = decrypt_string(text_to_decrypt, correctCypher[0])
    return result 

# Gets the contents of a file
def get_file_contents(file_name):
    if os.listdir().__contains__(file_name):
        try:
            with open(file_name, 'r') as decryption_target:
                return decryption_target.read()
        except:
            print("Something went wrong!")
    else:
        print("That file does not exist!")
    return None

# Lists files in the same directory, and gives the user an easy way to choose which one to decrypt
def get_file_name(): 
    print("Please choose a file with the cipher!")
    possible_files = os.listdir()
    num = 0
    print("q: quit")
    while num < len(possible_files):
        print(f"{num}: {possible_files[num]}")
        num += 1
    choice = input("choice: ")
    if choice == 'q':
        exit()
    try:
        return possible_files[int(choice)]
    except:
        return "NotAFile@thatDir"

# Core loop that initiates all the other logic
def main():
    file_name = get_file_name()
    text_to_decrypt = get_file_contents(file_name)
    if text_to_decrypt != None:
        print(crack_cipher(text_to_decrypt))
    main()

main()
