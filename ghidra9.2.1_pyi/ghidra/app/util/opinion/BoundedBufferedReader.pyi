from typing import List
import java.io
import java.lang
import java.nio


class BoundedBufferedReader(java.io.Reader):




    @overload
    def __init__(self, in_: java.io.Reader):
        """
        Creates a buffering character-input stream that uses a default-sized
         input buffer.
        @param in A Reader
        """
        ...

    @overload
    def __init__(self, in_: java.io.Reader, sz: int):
        """
        Creates a buffering character-input stream that uses an input buffer of
         the specified size.
        @param in A Reader
        @param sz Input-buffer size
        @exception IllegalArgumentException If sz is &lt;= 0
        """
        ...



    def close(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def mark(self, readAheadLimit: int) -> None:
        """
        Marks the present position in the stream. Subsequent calls to reset()
         will attempt to reposition the stream to this point.
        @param readAheadLimit Limit on the number of characters that may be read while still
                    preserving the mark. An attempt to reset the stream after
                    reading characters up to this limit or beyond may fail. A
                    limit value larger than the size of the input buffer will
                    cause a new buffer to be allocated whose size is no smaller
                    than limit. Therefore large values should be used with care.
        @exception IllegalArgumentException If readAheadLimit is &lt; 0
        @exception IOException If an I/O error occurs
        """
        ...

    def markSupported(self) -> bool:
        """
        Tells whether this stream supports the mark() operation, which it does.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def nullReader() -> java.io.Reader: ...

    @overload
    def read(self) -> int:
        """
        Reads a single character.
        @return The character read, as an integer in the range 0 to 65535 (
                 <code>0x00-0xffff</code>), or -1 if the end of the stream has been
                 reached
        @exception IOException If an I/O error occurs
        """
        ...

    @overload
    def read(self, __a0: List[int]) -> int: ...

    @overload
    def read(self, __a0: java.nio.CharBuffer) -> int: ...

    @overload
    def read(self, cbuf: List[int], off: int, len: int) -> int:
        """
        Reads characters into a portion of an array.

         <p>
         This method implements the general contract of the corresponding
         <code>{@link Reader#read(char[], int, int) read}</code> method of the
         <code>{@link Reader}</code> class. As an additional convenience, it
         attempts to read as many characters as possible by repeatedly invoking
         the <code>read</code> method of the underlying stream. This iterated
         <code>read</code> continues until one of the following conditions becomes
         true:
         <ul>

         <li>The specified number of characters have been read,

         <li>The <code>read</code> method of the underlying stream returns
         <code>-1</code>, indicating end-of-file, or

         <li>The <code>ready</code> method of the underlying stream returns
         <code>false</code>, indicating that further input requests would block.

         </ul>
         If the first <code>read</code> on the underlying stream returns
         <code>-1</code> to indicate end-of-file then this method returns
         <code>-1</code>. Otherwise this method returns the number of characters
         actually read.

         <p>
         Subclasses of this class are encouraged, but not required, to attempt to
         read as many characters as possible in the same fashion.

         <p>
         Ordinarily this method takes characters from this stream's character
         buffer, filling it from the underlying stream as necessary. If, however,
         the buffer is empty, the mark is not valid, and the requested length is
         at least as large as the buffer, then this method will read characters
         directly from the underlying stream into the given array. Thus redundant
         <code>BufferedReader</code>s will not copy data unnecessarily.
        @param cbuf Destination buffer
        @param off Offset at which to start storing characters
        @param len Maximum number of characters to read
        @return The number of characters read, or -1 if the end of the stream has
                 been reached
        @exception IOException If an I/O error occurs
        """
        ...

    def readLine(self) -> unicode:
        """
        Reads a line of text. A line is considered to be terminated by any one of
         a line feed ('\n'), a carriage return ('\r'), or a carriage return
         followed immediately by a linefeed.
        @return A String containing the contents of the line, not including any
                 line-termination characters, or null if the end of the stream has
                 been reached
        @exception IOException If an I/O error occurs
        """
        ...

    def ready(self) -> bool:
        """
        Tells whether this stream is ready to be read. A buffered character
         stream is ready if the buffer is not empty, or if the underlying
         character stream is ready.
        @exception IOException If an I/O error occurs
        """
        ...

    def reset(self) -> None:
        """
        Resets the stream to the most recent mark.
        @exception IOException If the stream has never been marked, or if the mark has
                        been invalidated
        """
        ...

    def skip(self, n: long) -> long:
        """
        Skips characters.
        @param n The number of characters to skip
        @return The number of characters actually skipped
        @exception IllegalArgumentException If <code>n</code> is negative.
        @exception IOException If an I/O error occurs
        """
        ...

    def toString(self) -> unicode: ...

    def transferTo(self, __a0: java.io.Writer) -> long: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
