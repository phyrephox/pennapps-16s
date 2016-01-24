"""Simple HTTP Server.

This module builds on BaseHTTPServer by implementing the standard GET
and HEAD requests in a fairly straightforward manner.

"""


__version__ = "0.6"

__all__ = ["SimpleHTTPRequestHandler"]

import os
import posixpath
import BaseHTTPServer
import urllib
import urlparse
import cgi
import sys
import shutil
import mimetypes
from word_checker import WordChecker
from parser import Parser
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

class SimpleHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    """Simple HTTP request handler with GET and HEAD commands.

    The GET and HEAD requests are identical except that the HEAD
    request omits the actual contents of the file.

    """

    server_version = "SimpleHTTP/" + __version__ 
    done = False
    wordChecker = WordChecker(5000)
    parser = Parser()

    def do_GET(self):
        """Serve a GET request."""
        f = self.send_head()
        if f:
            try:
                self.copyfile(f, self.wfile)
            finally:
                f.close()

    def do_HEAD(self):
        """Serve a HEAD request."""
        f = self.send_head()
        if f:
            f.close()

    def send_head(self):
        """Common code for GET and HEAD commands.

        This sends the response code and MIME headers.

        Return value is either a file object (which has to be copied
        to the outputfile by the caller unless the command was HEAD,
        and must be closed by the caller under all circumstances), or
        None, in which case the caller has nothing further to do.
        """
        word = self.path[1:]
        print word
        #word = word.replace("%0D%0A", "%20")
        #word = word.replace("%0D", "%20")
        #word = word.replace("%0A", "%20")
        word = urllib.unquote(word)
        """word = word.replace("%20", " ")"""
        print "Input: " + word
        return self.return_translation(word)

    def return_translation(self, word):

        f = StringIO()
        f.write(self.translate(word))
        length = f.tell()
        f.seek(0)
        self.send_response(200)
        encoding = sys.getfilesystemencoding()
        self.send_header("Content-type", "text/plain; charset=%s" % encoding)
        self.send_header("Content-Length", str(length))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        return f

    def translate(self, word):
        """
        replace with word translation
        """

        """
        words = word.split()
        for i in range(len(words)):
            if SimpleHTTPRequestHandler.wordChecker.check_word(words[i].lower()):
                words[i] = words[i]
            else:
                words[i] = "<" + words[i] + ">"
        output = ""
        for oneword in words:
            output = output + oneword + " "
        output = output[:-1]
        """

        output = SimpleHTTPRequestHandler.parser.parseSection(word)
        #output = output.encode(encoding='UTF-8',errors='replace')
        print "Output: " + output
        return output

    def copyfile(self, source, outputfile):
        """Copy all data between two file objects.

        The SOURCE argument is a file object open for reading
        (or anything with a read() method) and the DESTINATION
        argument is a file object open for writing (or
        anything with a write() method).

        The only reason for overriding this would be to change
        the block size or perhaps to replace newlines by CRLF
        -- note however that this the default server uses this
        to copy binary data as well.

        """
        shutil.copyfileobj(source, outputfile)


def test(HandlerClass = SimpleHTTPRequestHandler,
         ServerClass = BaseHTTPServer.HTTPServer):
    BaseHTTPServer.test(HandlerClass, ServerClass)


"""if __name__ == '__main__':"""
test()
