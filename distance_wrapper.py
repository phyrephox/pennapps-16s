#! /bin/bash/python 
# Wraps the Distance C library
# Author : John Hewitt
# 

from ctypes import *
#from numpy.ctypeslib import ndpointer
clib = cdll.LoadLibrary('./libtest.so')
clib.get_neighbors.restype = POINTER(c_char_p)
#clib.get_neighbors.restype = c_char_p

class Distance:

    def __init__(self):
        #self.testlib = ctypes.CDLL('/home/john/pennapps16s/pennapps-16s/trunk/a.out')
        #print clib.simple()
        self.state = clib.construct()
        #print self.state

    def distance(self, word):
        #self.testlib.myprint()
        words = clib.get_neighbors(self.state, word)
        ws = words[:5]
        return ws
        """ws = []
        for i in range(100):
            ws[i]"""

d = Distance()
d.distance('hello')
