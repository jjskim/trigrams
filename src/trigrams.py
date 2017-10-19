"""."""

# create an iterable list of all the words
list_of_words = string.split()

# create a dictionary
trigrams_dict = {}


# iterate through each pair in the list
def main(file_path, num_words):
    """."""
    import io
    # read the file
    f = io.open('test.txt', encoding='utf-8')
    string = f.read()
    f.close()

    for i in range(len(list_of_words) - 2):
        trigrams_dict_keys = ' '.join(list_of_words[i:i + 2])
        try:
            if len(trigrams_dict[trigrams_dict_keys]) > 0:
                trigrams_dict[trigrams_dict_keys].append(list_of_words[i + 2])
        except KeyError:
            trigrams_dict[trigrams_dict_keys] = [list_of_words[i + 2]]

    import random
    new_key = random.choice(list(trigrams_dict.keys()))
    new_text = new_key
    while (new_key in list(trigrams_dict.keys())):
        new_text = new_text + " " + random.choice(trigrams_dict[new_key])
        new_key = " ".join(new_text.split()[-2:])

    print(new_text)


main()


#print(trigrams_dict)