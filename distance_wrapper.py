#! /bin/bash/python 
# Wraps the Distance C library
# Author : John Hewitt
# 

import ctypes

class Distance:
    testlib = None

    def __init__(self):
        self.testlib = ctypes.CDLL('/home/john/pennapps16s/pennapps-16s/trunk/a.out')

    def distance(self, word):
        self.testlib.myprint()
