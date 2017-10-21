"""This module tests the functions in trigrams.py."""


def test_create_word_list_type():
    """Test if creates a list."""
    from trigrams import create_word_list
    assert type(create_word_list('test.txt')) == list


def test_populate_dictionary_type():
    """Test if populate_dictionary returns a dictionary."""
    s = ['I', 'wish', 'I', 'may', 'I', 'wish', 'I', 'might']
    from trigrams import populate_dictionary
    assert type(populate_dictionary(s)) == dict


def test_new_text_type():
    """Test if create_new_text returns a string."""
    d = {'This is': 'test'}
    from trigrams import create_new_text
    assert type(create_new_text(d, 2)) == str


def test_main(capfd):
    """Test the main function and that it outputs."""
    from trigrams import main
    main('test_2.txt', 3)
    out, err = capfd.readouterr()
    assert out == 'This is test'


def test_populate_dictionary():
    """Test the created dictionary against known dictionary."""
    from trigrams import populate_dictionary
    test_dic = {'I may': ['I'],
                'I wish': ['I', 'I'],
                'may I': ['wish'],
                'wish I': ['may', 'might']}
    s = ['I', 'wish', 'I', 'may', 'I', 'wish', 'I', 'might']
    assert populate_dictionary(s) == test_dic
