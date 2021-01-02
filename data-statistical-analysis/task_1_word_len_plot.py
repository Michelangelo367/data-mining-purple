from collections import OrderedDict

from matplotlib import pyplot as plt
import csv
import numpy as np

SPAM_FILE = 'output/spam_words.csv'
HAM_FILE = 'output/ham_words.csv'
WORD = 'word'
COUNT = 'count'
TITLE = 'Count of {} words by length chart'
SPAM = 'spam'
HAM = 'ham'


def calculate_avg(d):
    x = 0
    y = 0
    for key in d:
        c = d[key]
        x += key * c
        y += c
    return x / y


def main(file_name, msg_type):
    with open(file_name) as f:
        csv_reader = csv.DictReader(f)
        w_len_dict = {}
        for row in csv_reader:
            w_len = len(row[WORD])
            count_ = int(row[COUNT])
            if w_len in w_len_dict:
                w_len_dict[w_len] += count_
            else:
                w_len_dict[w_len] = count_

    total_w_sum = sum(w_len_dict.values())
    w_len_dict = {w_len[0]: w_len[1] / total_w_sum for w_len in w_len_dict.items()}
    w_len_dict = OrderedDict(sorted(w_len_dict.items(), key=lambda x: x[1], reverse=True))
    plt.style.use('fivethirtyeight')
    plt.title(TITLE.format(msg_type))
    words = w_len_dict.keys()
    x_indexes = np.arange(len(words))
    plt.xticks(x_indexes, words)
    plt.bar(x_indexes, w_len_dict.values(), color='#006a71', label='count of words by length')
    plt.xlabel("word length")
    plt.ylabel("count of words")
    plt.show()
    print('Average word length for {} is '.format(msg_type) + str(calculate_avg(w_len_dict)))


if __name__ == '__main__':
    main(SPAM_FILE, SPAM)
    main(HAM_FILE, HAM)
