import java.lang


class ReverseLineReader(object):
    """
    Reads in a single line of text from a given input file, in reverse order.

     CONOPS:
     	1. Start at a given position in the file and read BUFFER_SIZE bytes into a byte array
      2. From the end of the array, read a character
      3. If the character represents a newline (or carriage return), the line is finished, so return.
      4. If not, continue reading.
    """

    raf: java.io.RandomAccessFile



    def __init__(self, encoding: unicode, raf: java.io.RandomAccessFile):
        """
        @param encoding
        @param raf
        @throws IOException
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def readLine(self) -> unicode:
        """
        Reads a single line from the current file pointer position, in reverse.  To do this we do
         the following:

         1. Read a 'large enough' number of bytes into a buffer (enough to guarantee a full line of
            text.
         2. Move backwards through the bytes just read until a newline or carriage return is found.
         3. Throw away the rest of the bytes and return the line found.
        @return
        @throws IOException
        """
        ...

    def setFilePos(self, position: long) -> None:
        """
        Moves the file pointer to the given byte location.
        @param position
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def filePos(self) -> None: ...  # No getter available.

    @filePos.setter
    def filePos(self, value: long) -> None: ...
