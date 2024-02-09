"""
Program to randomly select a hermit to watch on YouTube

"""

import random

def choose_random_hermit():
    """
    Choose random hermit from the list of remianing hermits,
    then remove the chosen hermit from the list

    """
    # randomly select a hermit
    chosen_hermit = random.choice(hermits_to_choose_from)
    # remove the chosen hermit from the list
    hermits_to_choose_from.remove(chosen_hermit)
    # output the result, and enjoy the YouTube video!
    print('Hermit to watch next:', chosen_hermit)


# Entry point for the program
if __name__ == '__main__':
    # Create empty list to be populated with the as yet unchosen hermits
    hermits_to_choose_from = []

    # Read the file with the unchosen hermits
    with open('remaining_hermits.txt', 'r') as file:
        for remaining_hermit in file:
            hermits_to_choose_from.append(remaining_hermit)

    # Randomize hermit selection
    choose_random_hermit()

    # Overwrite the file, excluding the chosen hermit
    with open('remaining_hermits.txt', 'w') as file:
        for remaining_hermit in file:
            file.write(remaining_hermit)
        