import numpy as np


def make_pairs(corpus):
    for i in range(len(corpus) - 1):
        yield (corpus[i], corpus[i + 1])


def GenerateMessage(path, quantity):
    file = open(path, encoding='utf8').read()
    corpus = file.split()
    pairs = make_pairs(corpus)

    word_dict = {}

    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]

    first_word = np.random.choice(corpus)

    chain = [first_word]

    n_words = quantity

    for i in range(n_words):
        chain.append(np.random.choice(word_dict[chain[-1]]))

    return ' '.join(chain)


def count_lines(lines):
    count = 0
    for i in lines:
        count += 1
    return count
