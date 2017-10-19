"""."""


import io
# read the file
f = io.open('test.txt', encoding='utf-8')
string = f.read()
f.close()

# create an iterable list of all the words
list_of_words = string.split()

# create a dictionary
trigrams_dict = {}


# iterate through each pair in the list
def main():
    """."""
    for i in range(len(list_of_words) - 2):
        trigrams_dict_keys = ' '.join(list_of_words[i:i + 2])
        try:
            if len(trigrams_dict[trigrams_dict_keys]) > 0:
                trigrams_dict[trigrams_dict_keys].append(list_of_words[i + 2])
        except KeyError:
            trigrams_dict[trigrams_dict_keys] = [list_of_words[i + 2]]


main()


print(trigrams_dict)
