import pattern.en
from word_checker import WordChecker

class Parser(object):
    def __init__(self):
        self.wordChecker = WordChecker(5000)


    """
    This function return True if the word should be used as is
    this happens if the word is a proper noun or already simple
    """
    def getLemma(self, word):
        p = pattern.en.parse(word, chunks = False, lemmata = True).split()[0][0]
        #print p
        self.POS = p[1]
        if self.wordChecker.check_word(p[2]):
            return p[0], True
        if p[1][:3] == 'NNP':
            return p[0], True
        return p[2], False

    def getRep(self, words):
        for word in words:
		p = pattern.en.parse(word, chunks = False, lemmata = True).split()[0][0]
                if self.POS[0:2] == p[1][0:2]:
                    #print 'same'
                    if self.wordChecker.check_word(p[2]):
                        if self.POS[:2] == 'NN':
                            if self.POS[3]
                        return p[2]

def parseMain():
    p = Parser()
    p.getLemma('ate')
    p.getRep(['eat', 'ate', 'food'])
    #print pattern.en.parse('I eat pizza')

if __name__ == "__main__":
    parseMain()
