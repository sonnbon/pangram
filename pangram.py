# CS161 - HW5: Pangrams
# Connor Williams

# Program asks for and analyzes a sentence. After receiving the
# sentence, the program outputs whether or not the given
# sentence is a pangram.

# Function converts alpha characters into integer numbers between
# 0 and 25 (0 and 25 included).
# This function given by the 'HW5_Pangrams "Hints" section' of
# the homework assignment guidelines.
def code(character):

    # Non alpha characters will return as None.
    if not character.isalpha():
        return None

    # Unicode number associated with lowercase of character
    # assigned to variable.
    code = ord(character.lower())

    # Returns number between 0 and 25 by subtracting the
    # 'a' unicode number.
    return code - ord('a')

# Function takes a string and checks whether it is a pangram.
def is_pangram(string):

    # Range (0, 26) (not including 26) is assigned to variable.
    alpha_range = range(26)

    # Empty list assigned to variable to become a list of numbers
    # substituting for the original characters of the string.
    char_code = []

    # For loops through each character in the string and calls the code()
    # function to check that it is not None.
    for c in string:
        if code(c) is not None:

            # Integer numbers appended to char_code will be between
            # 0 and 25 (25 included).
            char_code.append(code(c))

    # For loops through alpha_range, checking to see if any numbers,
    # 0 through 25, are not in the char_code list.
    for n in alpha_range:

        # If a number from alpha_range is not in char_code, then
        # string cannot be a pangram.
        if n not in char_code:
            print(f"\n** {string} ** is not a pangram.")
            print("It does not contain all the letters of the alphabet.\n")

            # Calls function to ask if user wants to try another string.
            start_over()

            # Returns False and ends For loop and function.
            return False

    # False was not returned, so every number in alpha_range must have
    # been in string. Therefore, string is a pangram.
    print(f"\n** {string} ** is a pangram!")
    print("It contains all the letters of the alphabet!\n")

    # Calls function to ask if user wants to try another string.
    start_over()

    # Returns True and ends function.
    return True

# Function asks whether the user wants to test their input again.
def start_over():
    print("--- Would you like to try another word or phrase? ---")

    # User input assigned to variable.
    start_over = input("Yes (y) or No (n)? ")

    # While loop and if/elif/else statement checking whether user
    # enters "Yes" to try another phrase or "No" to end the program.
    while True:
        if start_over.lower() == "yes" or start_over.lower() == "y":

            # Ask for user input and store the input as a string.
            phrase = input("\nPlease enter a word or phrase: ")

            # Calls function to check whether phrase is a pangram.
            is_pangram(phrase)
            break
        elif start_over.lower() == "no" or start_over.lower() == "n":

            # Calls function to print an exiting program statement.
            goodbye()
            break
        elif start_over == "":

            # Calls function to print an exiting program statement.
            goodbye()
            break
        else:

            # Variable reassigned for new user input and While loops again.
            start_over = input("Sorry, was that a Yes (y) or No (n)? ")

# Function prints an exiting program statement.
def goodbye():
    print("\n*** You are exiting the Pangrams program ***")

# Print statement welcome message.
print("*** You are using the Pangrams program ***")

# Input statement to begin program.
input("Press Enter to continue...")

# Ask for user input and store the input as a string.
phrase = input("\nPlease enter a word or phrase: ")

# Calls function and takes users input as a string argument.
is_pangram(phrase)


