"""Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
Tags: short, math, simulation"""

import datetime
import random
from typing import Union, List


def getBirthdays(number_of_birthdays: int) -> List:
    """Returns a list of number random date objects for birthdays."""

    # The year is unimportant for our simulation, as long as all
    # birthdays have the same year.
    start_of_year = datetime.date(2001, 1, 1)

    # Get a random day into the year and append it to the birthday_list:
    birthday_list = [start_of_year + datetime.timedelta(random.randint(0, 364)) for _ in range(number_of_birthdays)]
    return birthday_list


def getMatch(birthday_list: List[datetime.date]) -> Union[None, datetime.date]:
    """Returns the date object of a birthday that occurs more than once
    in the birthdays list."""
    if len(birthday_list) == len(set(birthday_list)):
        return None  # All birthdays are unique, so return None.

    # Compare each birthday to every other birthday:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA  # Return the matching birthday.


# Display the intro:
print('''Birthday Paradox.

The birthday paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.\n''')

# Set up a tuple of month names in order:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:  # Keep asking until the user enters a valid amount.
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break  # User has entered a valid amount.

# Generate and display the birthdays:
print(f'Here are {numBDays} birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday.
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')

# Determine if there are two birthdays that match.
match = getMatch(birthdays)

# Display the results:
print('In this simulation, ', end='')
if match is not None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print(f'multiple people have a birthday on {dateText}.\n')
else:
    print('there are no matching birthdays.\n')

# Run through 100,000 simulations:
print(f'Generating {numBDays} random birthdays 100,000 times...')
input('Press Enter to begin...')

print('\nLet\'s run another 100,000 simulations.')
simMatch = 0  # How many simulations had matching birthdays in them.
for i in range(100000):
    # Report on the progress every 10,000 simulations:
    if i % 10000 == 0 and i != 0:
        print(f'{i} simulations ran...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) is not None:
        simMatch += 1
print('100000 simulations ran.\n')

# Display simulation results:
probability = round(simMatch / 100000 * 100, 2)
print(f'Out of 100000 simulations of {numBDays} people, there was a')
print(f'matching birthday in that group {simMatch} times. This means')
print(f'that {numBDays} people have a {probability} % chance of')
print('having a matching birthday in their group.')
