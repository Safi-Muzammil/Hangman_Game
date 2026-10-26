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

def Hangman_Image():
    pictures = [
        """
         +---+
             |
             |
             |
            ===
        """,
        """
         +---+
         O   |
             |
             |
            ===
        """,
        """
         +---+
         O   |
         |   |
             |
            ===
        """,
        """
         +---+
         O   |
        /|   |
             |
            ===
        """,
        """
         +---+
         O   |
        /|\\  |
             |
            ===
        """,
        """
         +---+
         O   |
        /|\\  |
        /    |
            ===
        """,
        """
         +---+
         O   |
        /|\\  |
        / \\  |
            ===
        """
    ]

    return pictures



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


def Play_Game(word, max_guesses):
    guessed_char = []
    wrong_guesses = 0
    pictures = Hangman_Image ()

    while wrong_guesses < max_guesses:
        hidden_line = Build_Hidden_Line(word, guessed_char)
        print(pictures[wrong_guesses])
        print("Word: ", hidden_line)
        print("Wrong guesses: ", wrong_guesses, "/", max_guesses)

        if hidden_line == word:
            print("Congratulations! You have guessed the word.")
            return

        guess = input("Guess a letter: ").strip().lower()

        # validate the player's guess:

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter at a time.")
            continue
        if guess in guessed_char:
            print("You have already guessed this letter.")

            continue
        guessed_char.append(guess)

        if guess not in word:
            wrong_guesses += 1
            print("Incorrect guess!")

        else:
            print("Correct guess!")

    # Displaying final image:
    print(pictures[min(wrong_guesses, len(pictures) - 1)])
    print("Word: ", word)
    print("Game over! You ran out of guesses.")


# main function to run the game:

def main():
    print("-----Hangman Game-----")

    word = Player_one()
    max_guesses = Get_Max_Guesses()
    Play_Game(word, max_guesses)


if __name__ == "__main__":
    main()


  



