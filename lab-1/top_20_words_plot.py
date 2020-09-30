import csv
from matplotlib import pyplot as plt
import numpy as np

SPAM_FILE = 'output/spam_words.csv'
HAM_FILE = 'output/ham_words.csv'
WORD = 'word'
COUNT = 'count'
TITLE = 'Top 20 {} words'
SPAM = 'spam'
HAM = 'ham'


def main():
    draw_chart(SPAM_FILE, SPAM)
    draw_chart(HAM_FILE, HAM)


def draw_chart(f_name, msg_type):
    with open(f_name) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        words = []
        frequency = []
        for row in csv_reader:
            words.append(row[WORD])
            frequency.append(row[COUNT])
        plt.style.use('fivethirtyeight')
        plt.title(TITLE.format(msg_type))
        words = words[0:20]
        words.reverse()
        frequency = frequency[:20]
        frequency.reverse()
        x_indexes = np.arange(len(words))
        plt.xticks(x_indexes, words)
        plt.bar(x_indexes, frequency, color='#006a71', label='Most frequent {} words'.format(msg_type))
        plt.xlabel("words")
        plt.ylabel("frequency")
        plt.gca().invert_xaxis()
        plt.show()


# Провести частотний аналіз появи слів для двох категорій.
# Вивести на графіках 20 слів, які зустрічаються найчастіше для кожної категорії окремо.
if __name__ == '__main__':
    main()
