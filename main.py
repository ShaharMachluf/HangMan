def opening_screen():
    """present the opening screen with max tries.
       :param MAX_TRIES: the number of tries the player gets to guess the word
       :type MAX_TRIES: int
       :return: max tries
       :rtype: int"""
    HANGMAN_ASCII_ART= """
   _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \\ / _' | '_ ' _ \\ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/"""

    MAX_TRIES = 6
    print(HANGMAN_ASCII_ART, "\nyour max tries are:", MAX_TRIES)
    return MAX_TRIES

def is_valid_input(letter_guessed, old_letters_guessed):
    """check if the guess received is a valid letter for the game.
       :param letter_guessed: the input from the user
       :param old_letters_guessed: list of letters the user guessed
       :type letter_guessed: string
       :type old_letters_guessed: list
       :return: weather the input is valid for the game
       :rtype: bool"""
    check1 = True
    is_english = letter_guessed.isalpha()
    if(len(letter_guessed) > 1) or (is_english == False):
        check1 = False
    if((old_letters_guessed.count(letter_guessed) == 0) and (check1 == True)):
        return True
    else:
        return False
        
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """check if the letter guessed is new or was already guessed.
       :param letter_guessed: the input from the user
       :param old_letters_guessed: list of letters the user guessed
       :type letter_guessed: string
       :type old_letters_guessed: list
       :return: weather the letter entered the list
       :rtype: bool"""
    if(is_valid_input(letter_guessed, old_letters_guessed) == True):
        old_letters_guessed.append(letter_guessed)
        old_letters_guessed.sort() 
        return True
    else:
        print("X\n", "->".join(old_letters_guessed))
        return False
        
def show_hidden_word(secret_word, old_letters_guessed):
    """show the current status of the right guesses
       :param secret_word: the secret word that the user need to guess
       :param old_letters_guessed: list of letters the user gussed
       :type secret_word: string
       :type old_letters_guessed: list
       :return: new word
       :rtype: stirng"""
    word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            word = word + letter
        else:
            word = word + " _ "
    return word
    
def check_win(secret_word, old_letters_guessed):
    """check if the player won
       :param secret_word: the word that the user need to guess
       :param old_letters_guessed: list of letters the user gussed
       :type secret_word: string
       :type old_letters_guessed: list
       :return: if the player won
       :rtype: bool"""
    check = True
    for letters in secret_word:
        if old_letters_guessed.count(letters) == 0:
            check = False
    return check
    
def print_hangman(num_of_tries):
    """print the hangman's status.
       :param num_of_tries: the number of failed tries of the user
       :type num_of_tries: int
       :return: None"""
    HANGMAN_PHOTOS = {0 : """x-------x""", 1 : """
    x-------x
    |
    |
    |
    |
    |

    """ , 2 : """
    x-------x
    |       |
    |       0
    |
    |
    |
    """, 3 : """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """, 4: """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
	""", 5 : """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """, 6 : """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \
    |
    """}
    return HANGMAN_PHOTOS[num_of_tries]
    
def choose_word(file_path, index):
    """choose a guess word.
       :param file_path: file of words
       :param index: number the user choose
       :guess_word: the chosen word
       :type file_path: file
       :type index: int
       :type guess_word: string
       :return: the guess word
       :rtype: string"""
    f = open(file_path, "r")
    #the words in the file as a string
    words = f.read()
    word_list = words.split()
    #the words in he file as a list
    while len(word_list) < index:
        index -= len(word_list)
    guess_word = word_list[index - 1]
    return guess_word
        
def main():
    MAX_TRIES = opening_screen()
    old_letters_guessed = []
    num_of_tries = 0
    file_path = input("Please enter a path to a file of words:")
    index = int(input("Please enter a random number to select the secret word:"))
    secret_word = choose_word(file_path, index)
    print(print_hangman(num_of_tries))
    print(" _ " * len(secret_word))
    while(num_of_tries < MAX_TRIES):
    #the game last until the player gets to the max tries and loses or guess the entire secret word and wins.
        letter = input("guess a letter: ")
        if try_update_letter_guessed(letter, old_letters_guessed):
        #check if the letter is valid
            letter = letter.lower()
            print(letter)
            if secret_word.count(letter) != 0:   
            #check if the letter is in the secret word.
                print(show_hidden_word(secret_word, old_letters_guessed))
            else:
                print(":(")
                num_of_tries += 1
                print(print_hangman(num_of_tries))
        else:
            print("Please guess only one letter in english")
        if check_win(secret_word,old_letters_guessed):
        #check every round if the player won. if so, end the game.
            break
    if check_win(secret_word,old_letters_guessed):
        print("WE HAVE A WINNER!")
    else:
        print("Sorry, you lost")

if __name__ == "__main__":
    main()
