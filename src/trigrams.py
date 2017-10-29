"""This module uses a trigram to create new text from existing text source."""
import sys
import random

USAGE = """
Usage: trigrams.py file_path num_words

    Where file_path is required and should specify the path to a txt file
    and num_words is required and should be an integer specifying the number
    of maximum words to print.

"""


def create_word_list(file_path):
    """Function creates a list of words from a text file.
    input: file_path of text file used to create trigram
    output: list of words
    """
    with open(file_path, 'r') as file:
        string = file.read()
    list_of_words = string.split()
    return list_of_words


def populate_dictionary(list_of_words):
    """Function that takes in a list of words and creates a dictonary of key value
    pairs.
    """
    trigrams_dict = {}
    for i in range(len(list_of_words) - 2):
        trigrams_dict_keys = ' '.join(list_of_words[i:i + 2])
        try:
            if len(trigrams_dict[trigrams_dict_keys]) > 0:
                trigrams_dict[trigrams_dict_keys].append(list_of_words[i + 2])
        except KeyError:
            trigrams_dict[trigrams_dict_keys] = [list_of_words[i + 2]]
    return trigrams_dict


def create_new_text(trigrams_dict, num_words):
    """Function that concatenates new text from the trigrams dictionary until
    the num_words condition is met.
    """
    new_key = random.choice(list(trigrams_dict.keys()))
    new_text = new_key.capitalize().split()
    text_length = len(new_text)
    while text_length < num_words:
        try:
            new_text.append(random.choice(trigrams_dict[new_key]))
            new_key = " ".join(new_text[-2:])
            text_length = len(new_text)
        except KeyError:
            new_key = random.choice(list(trigrams_dict.keys()))
            text_length = len(new_text)
    return " ".join(new_text)


def main(file_path, num_words):
    """
    This is the main function that calls the other functions in
    this module.  It then can stdout.write the text to a new file.
    """
    try:
        list_of_words = create_word_list(file_path)
        trigrams_dict = populate_dictionary(list_of_words)
        new_text = create_new_text(trigrams_dict, num_words)
        return new_text
    except RuntimeError:
        print("Try to keep the number of words under 1,000,000")
        sys.exit(1)

    sys.stdout.write(new_text)


if __name__ == '__main__':  # pragma: no cover
    if len(sys.argv) != 3:
        print(USAGE)
        sys.exit(1)

    print(main(sys.argv[1], int(sys.argv[2])))
