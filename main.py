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

  



