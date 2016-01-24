#! /bin/bash/python 
# Wraps the Distance C library
# Author : John Hewitt
# 

from ctypes import *
#from numpy.ctypeslib import ndpointer
clib = cdll.LoadLibrary('./trunk/distance')
clib.get_neighbors.restype = POINTER(c_char_p)
#clib.construct.argtypes = [c_char_p, POINTER(c_float)]
#clib.get_neighbors.restype = c_char_p

class Distance:

    def __init__(self):
        #self.testlib = ctypes.CDLL('/home/john/pennapps16s/pennapps-16s/trunk/a.out')
        #print clib.simple()
        self.M_arr = (c_float * 3000000 * 300)()
        #cast(self.M_arr, POINTER(c_float))
        #print self.M_arr
        self.vocab_arr = (c_char * 3000000 * 50)()
        #cast(self.vocab_arr, POINTER(c_float))
        self.state = (c_byte * 413296)()
        #print self.state
        clib.construct('GoogleNews-vectors-negative300.bin', self.M_arr, self.vocab_arr, self.state)
        #print self.state

    def get_neighbors(self, word):
        if isinstance(word, unicode):
            word = word.encode('utf-8')
        print(isinstance(word, unicode))
        #self.testlib.myprint()
        print 'get', word

       # self.output_add = (POINTER(c_char) * 100)()
       # for i in range(0, 100):
       #     ctype.
        self.ret_array = ((c_char * 2000) * 100)()

        words = clib.get_neighbors(self.state, word, byref(self.ret_array))
        #print words[0]
        ws = words[:100]
        print ws
        return ws
        """ws = []
        for i in range(100):
            ws[i]"""

