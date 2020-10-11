import numpy as np

corpus = open('data.txt', encoding='utf8').read()
data = corpus.split()


def make_pairs(a):
    for x in range(len(a) - 1):
        yield a[x], a[x + 1]


pairs = make_pairs(data)

word_dict = {}
for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]
first_word = np.random.choice(data)
print(first_word)
chain = [first_word]
n_words = 15
for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))
print(' '.join(chain))
max_key = None
max_len = 0
for key in word_dict:
    if len(word_dict[key]) >= max_len:
        max_key = key
        max_len = len(word_dict[key])
print("\nThe word \"", max_key, "\" has the maximum number of options, which equals ", max_len)
# print("\nThe options are :")
# for item in word_dict[max_key]:
#   print(item)
