#! /usr/bin/python2
#
# There is a Google Word2Vec thing and I wantto use it. I'll use this I guess?
# Author : John Hewitt
#

from subprocess import Popen
import MutableFile

class WordVecer:
    filename = ""
    db_proc = None
    input_obj = None

    def __init__(self, filename):
        self.filename = filename
        slef.input_obj = MutableFile.MutableFile()
        self.db_proc = Popen(["./distance ", filename], stdin=self.input_obj)
        (stdout, sterr) = self.db_proc.communicate()

    def check_word(self, word):
        self.db_proc


