import random

HANGMAN_PICS = [
    """
  +---+
      |
      |
      |
     ===""",
    """
  +---+
  O   |
      |
      |
     ===""",
    """
  +---+
  O   |
  |   |
      |
     ===""",
    """
  +---+
  O   |
 /|   |
      |
     ===""",
    """
  +---+
  O   |
 /|\  |
      |
     ===""",
    """
  +---+
  O   |
 /|\  |
 /    |
     ===""",
    """
  +---+
  O   |
 /|\  |
 / \  |
     ===""",
    """
  +---+
 [O   |
 /|\  |
 / \  |
     ===""",
    """
  +---+
 [O]  |
 /|\  |
 / \  |
     ===""",
]

words = {
    "Colors": "red orange yellow green blue indigo violet white black brown".split(),
    "Shapes": "square triangle rectangle circle ellipse rhombus trapazoid chevron pentagon hexagon septagon octogon".split(),
    "Fruits": "apple orange lemon lime pear watermelon grape grapefruit cherry banana cantalope mango strawberry tomato".split(),
    "Animals": "bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra".split(),
    "Rock bands": "riff hermetica molotov sumo apocalyptica".split(),
}

clues = {
    "riff": "The first true hard-rock band in Argentina.",
    "hermetica": "The most important trash-metal band in South America.",
    "molotov": "A band with two bass players.",
    "sumo": "An Argentine rock-reggae band founded by an Italian.",
    "apocalyptica": "A band that decided to play metal songs with classical instruments.",
}


def get_random_word(word_dict):
    """This function returns a random string from the passed dictionary
    of lists of strings, and the key also."""

    # First, randomly select a key from the dictionary:
    word_key = random.choice(list(word_dict.keys()))

    # Second, randomly select a word from the key's list in the dictionary:
    word_index = random.randint(0, len(word_dict[word_key]) - 1)

    return [word_dict[word_key][word_index], word_key]


def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()

    print("Missed letters:", end=" ")
    for letter in missed_letters:
        print(letter, end=" ")
    print()

    blanks = "_" * len(secret_word)

    # replace blanks with correctly guessed letters
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1 :]

    # show the secret word with spaces in between each letter
    for letter in blanks:
        print(letter, end=" ")
    print()


def get_guess(already_guessed):
    """Returns the letter the player entered. This function makes sure the
    player entered a single letter, and not something else."""
    while True:
        print("Guess a letter.")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in already_guessed:
            print("You have already guessed that letter. Choose again.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a LETTER.")
        else:
            return guess


def play_again():
    """This function returns True if the player wants to play again,
    otherwise it returns False."""
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")


print("H A N G M A N")

difficulty = "X"
while difficulty not in "EMH":
    print("Enter difficulty: E - Easy, M - Medium, H - Hard")
    difficulty = input().upper()
if difficulty == "M":
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == "H":
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missed_letters = ""
correct_letters = ""
secret_word, secret_set = get_random_word(words)
game_is_done = False

while True:
    print("The secret word is in the set: " + secret_set)
    display_board(missed_letters, correct_letters, secret_word)

    # A??ado esto para que imprima la pista en el caso que sea una banda.
    if secret_set == "Rock bands":
        print(f"Clue: {clues[secret_word]}")

    # Let the player type in a letter.
    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters = correct_letters + guess

        # Check if the player has won
        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print('Yes! The secret word is "' + secret_word + '"! You have won!')
            game_is_done = True
    else:
        missed_letters = missed_letters + guess

        # Check if player has guessed too many times and lost.
        if len(missed_letters) == len(HANGMAN_PICS) - 1:
            display_board(missed_letters, correct_letters, secret_word)
            # A??ado esto para que imprima la pista en el caso que sea una banda.
            if secret_set == "Rock bands":
                print(f"Clue: {clues[secret_word]}")
            print(
                "You have run out of guesses!\nAfter "
                + str(len(missed_letters))
                + " missed guesses and "
                + str(len(correct_letters))
                + ' correct guesses, the word was "'
                + secret_word
                + '"'
            )
            game_is_done = True

    # Ask the player if they want to play again (but only if the game is done).
    if game_is_done:
        if play_again():
            missed_letters = ""
            correct_letters = ""
            game_is_done = False
            secret_word, secret_set = get_random_word(words)
        else:
            break