# Defining a function for creating hidden line:

def Build_Hidden_Line(word, guessed_char):
    hidden_line = ""

    for c in word:
        if c in guessed_char:
            hidden_line += c

        elif c == " ":
            hidden_line += c

        else:
            hidden_line +=   "_"

    return hidden_line


# Function for Hangman image. 
def Hangman_Image():
    pass


def Player_one():
    while True:
        word = input("Player_One: Enter a word or phrase: ").strip().lower()
        if not word:
            print("The word can not be empty.")
            continue

        if not all(char.isalpha() or word == " " for char in word):
            print("Please enter character or space only.")
            continue
        # Hiding player one input.
        print("\n" * 50)

        return word

def Get_Max_Guesses():
    while True:
        try:
            guesses = int(input("Enter maximum incorrect guesses: "))
            if guesses < 1 or guesses >7:
                print("Please enter guesses between 1 to 7.")

        except ValueError:
            print("Invalid input! Please enter only whole number.")

        return guesses



  



