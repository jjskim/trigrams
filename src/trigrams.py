"""."""


def create_word_list(file_path):
    """."""
    import io
    f = io.open(file_path, encoding='utf-8')
    string = f.read()
    f.close()
    list_of_words = string.split()
    return list_of_words


def populate_dictionary(list_of_words):
    """."""
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
    """."""
    import random
    new_key = random.choice(list(trigrams_dict.keys()))
    new_text = new_key.capitalize()
    count = 2
    while (new_key in list(trigrams_dict.keys()) and count < num_words):
        new_text = new_text + " " + random.choice(trigrams_dict[new_key])
        new_key = " ".join(new_text.split()[-2:])
        count += 1
    return new_text


def main(file_path, num_words):
    """."""
    list_of_words = create_word_list(file_path)
    trigrams_dict = populate_dictionary(list_of_words)
    new_text = create_new_text(trigrams_dict, num_words)
    print(new_text)


main('test.txt', 100)
