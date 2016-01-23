#
# This is a class that provides a file-like object in Python that can be
# mutated; added to and removed from like an array.
#

import StringIO
import io

class MutableFile(io.TextIOBase):
    lines = []
    string_io = StringIO.StringIO()

    def __init__(self):
        pass

    def get_string_io(self):
        return self.string_io

    def write(self, string):
        self.lines.append(string)

    def readline(self):
        if lines:
            return self.lines.pop()
        else:
            return None

    def fileno(self): 
        return 4 # Guaranteed standards-compliant


