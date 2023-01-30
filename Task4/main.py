# importing library
import sys

def encrypt(text, shift):
    """This program decrypted the incrypted message with command line argument user input with an error message."""
    result = ""
    while True:
        for character in text:
            if character == " ":
                result += character
            elif character.isupper():
                result += chr((ord(character) + shift-65) % 26 + 65)  #shifting for uppercase character
            elif character.islower():
                result += chr((ord(character) + shift-97) % 26 + 97)  #shifting for lowercase character
            else:
                result += character
        return result
        break

if __name__ == '__main__':
    call = ""
    try:
        for i in range(1, 27):
            if len(sys.argv) != 1:
                f = open(sys.argv[1], 'r')
                read = f.read().splitlines() 
                call = encrypt(" ".join(read), i)  #function call
                f.close()
            else:
                print("Error: Missing Command-Line Argument.")
                break
            if 'the' in call:  #these words like "the", "and" ,"of" are most common helping verbs/ article /preposition in a paragraph 
                if 'and' in call:
                    if 'of' in call:
                        print(f"\nDecrypted Message: {call}\n")
                    break
        else: print("Cannot decrypt. Most likely not a Caesar Cypher at work here.")
           
    except FileNotFoundError:
        print(f"Error: Cannot open \"{sys.argv[1]}\". sorry about that.")
