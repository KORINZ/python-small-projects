"""A deductive logic game where you must guess a number based on clues.
Tags: short, game, puzzle"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 5


def main() -> None:
    print(f'''Bagels, a deductive logic game.

There is a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is.

  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.\n''')

    while True:
        # This stores the secret number the player needs to guess:
        secret_num = getSecretNum()
        print(f'You have {MAX_GUESSES} guesses to get it.')

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            print(f'Guess #{num_guesses}: ')
            guess = input('> ')

            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Invalid input. Try again.\nGuess #{num_guesses}: ')
                guess = input('> ')

            print(getClues(guess, secret_num))
            num_guesses += 1

            if guess == secret_num:
                break  # They're correct, so break out of this loop.
            if num_guesses > MAX_GUESSES:
                print('Game over. You ran out of guesses.')
                print(f'The answer was {secret_num}.')

        # Ask player if they want to play again.
        print('Do you want to play again? (input "y" to continue, anything else to exit)')
        if input('> ') != "y":
            break
    print('Thanks for playing!')


def getSecretNum() -> str:
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = [str(i) for i in range(10)]
    random.shuffle(numbers)  # Shuffle them into random order.

    # Return the first NUM_DIGITS digits in the list for the secret number:
    return ''.join(numbers[:NUM_DIGITS])


def getClues(guess: str, secret_num: str) -> str:
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""
    if guess == secret_num:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secret_num:
            # A correct digit is in the incorrect place.
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'  # There are no correct digits at all.
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)


if __name__ == '__main__':
    main()
