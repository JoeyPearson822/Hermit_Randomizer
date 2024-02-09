"""
Program to randomly select a hermit to watch on YouTube

"""

import random
import os

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
    return chosen_hermit


# Entry point for the program
if __name__ == '__main__':
    # Create empty list to be populated with the as yet unchosen hermits
    hermits_to_choose_from = []

    # Read the file with the unchosen hermits
    with open('remaining_hermits.txt', 'r') as file:
        for remaining_hermit in file:
            hermits_to_choose_from.append(remaining_hermit)

    chosen_hermit = choose_random_hermit()

    with open("remaining_hermits.txt", "r") as input:
        with open("temp.txt", "w") as output:
            # iterate all lines from file
            for line in input:
                # if substring is in a line, then don't write it
                if chosen_hermit not in line:
                    output.write(line)

    # replace file with original name
    os.replace('temp.txt', 'remaining_hermits.txt')
        