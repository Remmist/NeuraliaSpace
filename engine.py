import numpy as np


# METHOD TO CREATE CORPUS FOR MARKOV'S CHAIN
def make_pairs(corpus):
    for i in range(len(corpus) - 1):
        yield (corpus[i], corpus[i + 1])


# MAIN METHOD TO GENERATE MESSAGES (MARKOV'S CHAIN)
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


# METHOD TO COUNT LINES
def count_lines(lines):
    count = 0
    for i in lines:
        count += 1
    return count


# METHOD TO CHECK IS THERE ENOUGH DATA TO GENERATE A MESSAGE
def isEnoughData(path):
    try:
        file = open(path, 'r', encoding='utf8')
    except FileNotFoundError:
        return False
    count = count_lines(file.readlines())
    if count < 100:
        file.close()
        return False
    else:
        file.close()
        return True


# METHOD TO SAVE INCOMING MESSAGE FROM CHAR
def saveData(path, msg):
    file = open(path, 'a+', encoding='utf8')
    file.seek(0, 2)
    file.write(msg + '\n')
    file.close()