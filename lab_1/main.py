"""
Lab 1
A concordance extraction
"""
def tokenize(text: str) -> list:
    """
    Splits sentences into tokens, converts the tokens into lowercase, removes punctuation
    :param text: the initial text
    :return: a list of lowercased tokens without punctuation
    e.g. text = 'The weather is sunny, the man is happy.'
    --> ['the', 'weather', 'is', 'sunny', 'the', 'man', 'is', 'happy']
    """

    if not isinstance(text, str):
        return []


    clean_tokens = []
    for token in text.lower().split():
        word = ''
        for character in token:
            if character.isalpha():
                word += character
        if word:
            clean_tokens.append(word)
    return clean_tokens

def remove_stop_words(tokens: list, stop_words: list) -> list:
    """
    Removes stop words
    :param tokens: a list of tokens
    :param stop_words: a list of stop words
    :return: a list of tokens without stop words
    e.g. tokens = ['the', 'weather', 'is', 'sunny', 'the', 'man', 'is', 'happy']
    stop_words = ['the', 'is']
    --> ['weather', 'sunny', 'man', 'happy']
    """

    if not isinstance(tokens, list) or not isinstance(stop_words, list):
        return []

    return [item for item in tokens if item not in stop_words_set]


def calculate_frequencies(tokens: list) -> dict:
    """
    Calculates frequencies of given tokens
    :param tokens: a list of tokens without stop words
    :return: a dictionary with frequencies
    e.g. tokens = ['weather', 'sunny', 'man', 'happy']
    --> {'weather': 1, 'sunny': 1, 'man': 1, 'happy': 1}
    """
if not isinstance(tokens, list) or None in tokens:
        return {}

    # here goes the main logic
    freq_dict = {}
    for token in tokens:
        if token in freq_dict:
            freq_dict[token] += 1
        else:
            freq_dict[token] = 1
    return freq_dict

def get_top_n_words(freq_dict: dict, top_n: int) -> list:
    """
    Returns the most common words
    :param freq_dict: a dictionary with frequencies
    :param top_n: a number of the most common words to return
    :return: a list of the most common words
    e.g. tokens = ['weather', 'sunny', 'man', 'happy', 'and', 'dog', 'happy']
    top_n = 1
    --> ['happy']
    """
    if not isinstance(freq_dict, dict) or not isinstance(top_n, int) or None in freq_dict:
        return []

    frequencies_and_words_sorted = sorted(list(freq_dict.items()), key=lambda i: i[1], reverse=True)
    result = []
    for word_freq in frequencies_and_words_sorted[:top_n]:
        result.append(word_freq[0])
    return result

def get_concordance(tokens: list, word: str, left_context_size: int, right_context_size: int) -> list:
    """
    Gets a concordance of a word
    A concordance is a listing of each occurrence of a word in a text,
    presented with the words surrounding it
    :param tokens: a list of tokens
    :param word: a word-base for a concordance
    :param left_context_size: the number of words in the left context
    :param right_context_size: the number of words in the right context
    :return: a concordance
    e.g. tokens = ['the', 'weather', 'is', 'sunny', 'the', 'man', 'is', 'happy',
                    'the', 'dog', 'is', 'happy', 'but', 'the', 'cat', 'is', 'sad']
    word = 'happy'
    left_context_size = 2
    right_context_size = 3
    --> [['man', 'is', 'happy', 'the', 'dog', 'is'], ['dog', 'is', 'happy', 'but', 'the', 'cat']]
    """

    if not isinstance(tokens, list) or not isinstance(word, str)\
            or None in tokens:
        return []
    if left_context_size is True or right_context_size is True\
            or not isinstance(left_context_size, int) or not isinstance(right_context_size, int):
        return []

    if left_context_size < 0:
        left_context_size = 0
    if right_context_size < 0:
        right_context_size = 0
    if left_context_size == 0 and right_context_size == 0:
        return []

    contexts = []
    for index, element in enumerate(tokens):
        if element == word:
            contexts.append(tokens[index-left_context_size:index+right_context_size+1])
    return contexts

def get_adjacent_words(tokens: list, word: str, left_n: int, right_n: int) -> list:
    """
    Gets adjacent words from the left and right context
    :param tokens: a list of tokens
    :param word: a word-base for the search
    :param left_n: the distance between a word and an adjacent one in the left context
    :param right_n: the distance between a word and an adjacent one in the right context
    :return: a list of adjacent words
    e.g. tokens = ['the', 'weather', 'is', 'sunny', 'the', 'man', 'is', 'happy',
                    'the', 'dog', 'is', 'happy', 'but', 'the', 'cat', 'is', 'sad']
    word = 'happy'
    left_n = 2
    right_n = 3
    --> [['man', 'is'], ['dog, 'cat']]
    """
contexts = get_concordance(tokens, word, left_n, right_n)
adjacent_words = []
for context in contexts:
    if not left_n:
        adjacent_words.append([context[-1]])
    elif not right_n:
        adjacent_words.append([context[0]])
    else:
        adjacent_words.append([context[0], context[-1]])
return adjacent_words


def read_from_file(path_to_file: str) -> str:
    """
    Opens the file and reads its content
    :return: the initial text in string format
    """
    with open(path_to_file, 'r', encoding='utf-8') as file:
        data = file.read()
    return data


def write_to_file(path_to_file: str, content: list):
    """
    Writes the result in a file
    """
    with open(path_to_file, 'w', encoding='utf-8') as file:
        for context in content:
            file.write(' '.join(context)+'\n')
        file.close()


def sort_concordance(tokens: list, word: str, left_context_size: int, right_context_size: int, left_sort: bool) -> list:
    """
    Gets a concordance of a word and sorts it by either left or right context
    :param tokens: a list of tokens
    :param word: a word-base for a concordance
    :param left_context_size: the number of words in the left context
    :param right_context_size: the number of words in the right context
    :param left_sort: if True, sort by the left context, False – by the right context
    :return: a concordance
    e.g. tokens = ['the', 'weather', 'is', 'sunny', 'the', 'man', 'is', 'happy',
                    'the', 'dog', 'is', 'happy', 'but', 'the', 'cat', 'is', 'sad']
    word = 'happy'
    left_context_size = 2
    right_context_size = 3
    left_sort = True
    --> [['dog', 'is', 'happy', 'but', 'the', 'cat'], ['man', 'is', 'happy', 'the', 'dog', 'is']]
    """
    contexts = get_concordance(tokens, word, left_context_size, right_context_size)
    if not isinstance(left_sort, bool):
        return []
    if not contexts:
        return []
    if (left_sort and left_context_size < 0) or (not left_sort and right_context_size < 0):
        return []

    if left_sort:
        return sorted(contexts)

    word_index = contexts[0].index(word)
    right_contexts = [(context[word_index + 1:], context[:word_index + 1]) for context in contexts]
    right_contexts_sorted = sorted(right_contexts)
    return [sorted_right_context[1] + sorted_right_context[0] for sorted_right_context in right_contexts_sorted]