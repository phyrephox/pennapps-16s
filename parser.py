import pattern.en
from word_checker import WordChecker
from pyvector import WordVector

class Parser(object):
    def __init__(self):
        self.wordChecker = WordChecker(5000)
        self.WordVector = WordVector()

    def parseSection(self, section):
        p = pattern.en.parse(section, chunks = False, lemmata = True).split()
        finalS = []
        for sentence in p:
            s = []
            for w in sentence:
                s.append(w[0])
            final = []
            for count, word in enumerate(sentence):
                if self.wordChecker.check_word(word[0]):
                    continue
                final.append(word[0])
                if word[1][:3] == 'NNP' or word[1] in ['.',',',':','(',')']:
                    continue
                alternates = self.WordVector.get_neighbors(word[2])
                for test_word in alternates:
                    if not self.wordChecker.check_word(test_word):
                        continue
                    s[count] = test_word
                    print s
                    p_test = pattern.en.parse(' '.join(s), chunks = False, lemmata = True).split()
                    if p_test[0][count][1] == sentence[count][1]:
                        w = self.matchType(sentence[count], p_test[0][count])
                        if count == 0:
                            w = w.capitalize()
                        final[-1] = w
                        break
                s[count] = word[0]
            finalS.append(' '.join(final))
        return ''.join(finalS)

    def matchType(self, original, test):
        oPOS = original[1]
        nPOS = test[1]
        word = test[0]
        if oPOS == 'NN' and nPOS == 'NNS':
            word = pattern.en.singularize(test[0])
        if oPOS == 'NNS' and nPOS == 'NN':
            word = pattern.en.pluralize(test[0])
        if oPOS == 'JJR' and nPOS == 'JJ':
            word = pattern.en.comparative(test[0])
        if oPOS == 'JJS' and nPOS == 'JJ':
            word = pattern.en.superlative(test[0])
        if oPOS[:2] == 'VB':
            word = pattern.en.conjugate(test[0], oPOS)
        return word

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
            #print p
            POS = p[1]
            #print p, self.POS, POS
            if self.POS[:2] == p[1][:2]:
                #print 'same'
                if self.wordChecker.check_word(p[2]):
                    word = p[2]
                    #print word
                    if self.POS == 'NN' and p[1] == 'NNS':
                        word = pattern.en.singularize(p[2])
                    if self.POS == 'NNS' and p[1] == 'NN':
                        word = pattern.en.pluralize(p[2])
                    if self.POS == 'JJR' and p[1] == 'JJ':
                        word = pattern.en.comparative(p[2])
                    if self.POS == 'JJS' and p[1] == 'JJ':
                        word = pattern.en.superlative(p[2])
                    if self.POS[:2] == 'VB':
                        word = pattern.en.conjugate(p[2], self.POS)
                    return word

def parseMain():
    p = Parser()
    print p.parseSection('The quick brown fox jumps over the lazy dog.')
    #p.getLemma('purring')
    #print p.POS
    #print p.getRep(['bless'])
    #print pattern.en.superlative('easy')
    #print pattern.en.parse('easiest', lemmata=True)
    #print pattern.en.parse('a nicer pizza', lemmata=True)
    #print pattern.en.parse('I eat pizza')

if __name__ == "__main__":
    parseMain()
