#! /usr/bin/python2
#
# There is a Google Word2Vec thing and I wantto use it. I'll use this I guess?
# Author : John Hewitt
#

from subprocess import Popen
import MutableFile
import sys
import subprocess
import time


class WordVector:

    def get_neighbors(self, word):
        line  = 'echo ' + word + ' > ' +  "/tmp/srv-input"
        subprocess.call(line, shell=True)
        time.sleep(3)
        words = []

        with open('output') as f:
            for i in range(0,5):
                f.readline()
            for line in f:
                words.append(line.strip().split('\t')[0])
        return words




