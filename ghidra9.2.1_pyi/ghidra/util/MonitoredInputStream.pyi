from typing import List
import java.io
import java.lang


class MonitoredInputStream(java.io.InputStream):
    """
    An InputStream which utilizes a TaskMonitor to indicate input progress and
     allows the operation to be cancelled via the TaskMonitor.
    """





    def __init__(self, in_: java.io.InputStream, monitor: ghidra.util.task.TaskMonitor): ...



    def available(self) -> int:
        """
        Returns the number of bytes that can be read from this input
         stream without blocking.
         <p>
         This method
         simply performs <code>in.available()</code> and
         returns the result.
        @return the number of bytes that can be read from the input stream
                     without blocking.
        @exception IOException if an I/O error occurs.
        """
        ...

    def close(self) -> None:
        """
        Closes this input stream and releases any system resources
         associated with the stream.
         This
         method simply performs <code>in.close()</code>.
        @exception IOException if an I/O error occurs.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def mark(self, readlimit: int) -> None:
        """
        Marks the current position in this input stream. A subsequent
         call to the <code>reset</code> method repositions this stream at
         the last marked position so that subsequent reads re-read the same bytes.
         <p>
         The <code>readlimit</code> argument tells this input stream to
         allow that many bytes to be read before the mark position gets
         invalidated.
         <p>
         This method simply performs <code>in.mark(readlimit)</code>.
        @param readlimit the maximum limit of bytes that can be read before
                              the mark position becomes invalid.
        @see java.io.FilterInputStream#reset
        """
        ...

    def markSupported(self) -> bool:
        """
        Tests if this input stream supports the <code>mark</code>
         and <code>reset</code> methods.
         This method
         simply performs <code>in.markSupported()</code>.
        @return <code>true</code> if this stream type supports the
                  <code>mark</code> and <code>reset</code> method;
                  <code>false</code> otherwise.
        @see java.io.InputStream#mark(int)
        @see java.io.InputStream#reset()
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def nullInputStream() -> java.io.InputStream: ...

    @overload
    def read(self) -> int:
        """
        Reads the next byte of data from this input stream. The value
         byte is returned as an <code>int</code> in the range
         <code>0</code> to <code>255</code>. If no byte is available
         because the end of the stream has been reached, the value
         <code>-1</code> is returned. This method blocks until input data
         is available, the end of the stream is detected, or an exception
         is thrown.
         <p>
         This method
         simply performs <code>in.read()</code> and returns the result.
        @return the next byte of data, or <code>-1</code> if the end of the
                     stream is reached.
        @exception IOException if an I/O error occurs.
        """
        ...

    @overload
    def read(self, b: List[int]) -> int:
        """
        Reads up to <code>byte.length</code> bytes of data from this
         input stream into an array of bytes. This method blocks until some
         input is available.
         <p>
         This method simply performs the call
         <code>read(b, 0, b.length)</code> and returns
         the  result. It is important that it does
         <i>not</i> do <code>in.read(b)</code> instead;
         certain subclasses of  <code>FilterInputStream</code>
         depend on the implementation strategy actually
         used.
        @param b the buffer into which the data is read.
        @return the total number of bytes read into the buffer, or
                     <code>-1</code> if there is no more data because the end of
                     the stream has been reached.
        @exception IOException if an I/O error occurs.
        @see java.io.FilterInputStream#read(byte[], int, int)
        """
        ...

    @overload
    def read(self, b: List[int], off: int, len: int) -> int:
        """
        Reads up to <code>len</code> bytes of data from this input stream
         into an array of bytes. This method blocks until some input is
         available.
         <p>
         This method simply performs <code>in.read(b, off, len)</code>
         and returns the result.
        @param b the buffer into which the data is read.
        @param off the start offset of the data.
        @param len the maximum number of bytes read.
        @return the total number of bytes read into the buffer, or
                     <code>-1</code> if there is no more data because the end of
                     the stream has been reached.
        @exception IOException if an I/O error occurs.
        """
        ...

    def readAllBytes(self) -> List[int]: ...

    @overload
    def readNBytes(self, __a0: int) -> List[int]: ...

    @overload
    def readNBytes(self, __a0: List[int], __a1: int, __a2: int) -> int: ...

    def reset(self) -> None:
        """
        Repositions this stream to the position at the time the
         <code>mark</code> method was last called on this input stream.
         <p>
         This method
         simply performs <code>in.reset()</code>.
         <p>
         Stream marks are intended to be used in
         situations where you need to read ahead a little to see what's in
         the stream. Often this is most easily done by invoking some
         general parser. If the stream is of the type handled by the
         parse, it just chugs along happily. If the stream is not of
         that type, the parser should toss an exception when it fails.
         If this happens within readlimit bytes, it allows the outer
         code to reset the stream and try another parser.
        @exception IOException if the stream has not been marked or if the
                       mark has been invalidated.
        @see java.io.FilterInputStream#mark(int)
        """
        ...

    def setProgress(self, count: int) -> None:
        """
        Reset the current progress count to the specified value.
        """
        ...

    def skip(self, n: long) -> long:
        """
        Skips over and discards <code>n</code> bytes of data from the
         input stream. The <code>skip</code> method may, for a variety of
         reasons, end up skipping over some smaller number of bytes,
         possibly <code>0</code>. The actual number of bytes skipped is
         returned.
         <p>
         This method
         simply performs <code>in.skip(n)</code>.
        @param n the number of bytes to be skipped.
        @return the actual number of bytes skipped.
        @exception IOException if an I/O error occurs.
        """
        ...

    def toString(self) -> unicode: ...

    def transferTo(self, __a0: java.io.OutputStream) -> long: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def progress(self) -> None: ...  # No getter available.

    @progress.setter
    def progress(self, value: int) -> None: ...
