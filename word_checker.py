import string

class WordChecker(object):
    def __init__(self, num_words):
        self.word_list = []
        self.word_set = set(self.word_list)
        #f = open('google-10000-english/google-10000-english-usa.txt', 'r')
        f = open('words.csv', 'r')
        for line in f:
            if line[0] == '#':
                continue
            word = string.split(line, ',')[1]
            word = string.strip(word[6:])
            self.word_list.append(word)
        self.word_set = set(self.word_list[:num_words])

    def check_word(self, word):
        return string.strip(word) in self.word_set

def wordMain():
    size = int(raw_input('Enter the number of words to compare against: '))
    w = WordChecker(size)
    print (w.word_set)
    while(True):
        toCheck = raw_input('Enter a word to check: ')
        print (w.check_word(toCheck))
if __name__ == "__main__":
    wordMain()
