from typing import List
import java.io
import java.lang


class MonitoredOutputStream(java.io.OutputStream):
    """
    An OutputStream which utilizes a TaskMonitor to indicate output progress and
     allows the operation to be cancelled via the TaskMonitor.
    """





    def __init__(self, out: java.io.OutputStream, monitor: ghidra.util.task.TaskMonitor): ...



    def close(self) -> None:
        """
        Closes this output stream and releases any system resources
         associated with the stream.
         <p>
         The <code>close</code> method of <code>FilterOutputStream</code>
         calls its <code>flush</code> method, and then calls the
         <code>close</code> method of its underlying output stream.
        @exception IOException if an I/O error occurs.
        @see java.io.FilterOutputStream#flush()
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def flush(self) -> None:
        """
        Flushes this output stream and forces any buffered output bytes
         to be written out to the stream.
         <p>
         The <code>flush</code> method of <code>FilterOutputStream</code>
         calls the <code>flush</code> method of its underlying output stream.
        @exception IOException if an I/O error occurs.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def nullOutputStream() -> java.io.OutputStream: ...

    def setProgress(self, count: int) -> None:
        """
        Reset the current progress count to the specified value.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @overload
    def write(self, b: int) -> None:
        """
        Writes the specified <code>byte</code> to this output stream.
         <p>
         The <code>write</code> method of <code>FilterOutputStream</code>
         calls the <code>write</code> method of its underlying output stream,
         that is, it performs <code>out.write(b)</code>.
         <p>
         Implements the abstract <code>write</code> method of <code>OutputStream</code>.
        @param b the <code>byte</code>.
        @exception IOException if an I/O error occurs.
        """
        ...

    @overload
    def write(self, b: List[int]) -> None:
        """
        Writes <code>b.length</code> bytes to this output stream.
         <p>
         The <code>write</code> method of <code>FilterOutputStream</code>
         calls its <code>write</code> method of three arguments with the
         arguments <code>b</code>, <code>0</code>, and
         <code>b.length</code>.
         <p>
         Note that this method does not call the one-argument
         <code>write</code> method of its underlying stream with the single
         argument <code>b</code>.
        @param b the data to be written.
        @exception IOException if an I/O error occurs.
        @see java.io.FilterOutputStream#write(byte[], int, int)
        """
        ...

    @overload
    def write(self, b: List[int], off: int, len: int) -> None:
        """
        Writes <code>len</code> bytes from the specified
         <code>byte</code> array starting at offset <code>off</code> to
         this output stream.
         <p>
         The <code>write</code> method of <code>FilterOutputStream</code>
         calls the <code>write</code> method of one argument on each
         <code>byte</code> to output.
         <p>
         Note that this method does not call the <code>write</code> method
         of its underlying input stream with the same arguments. Subclasses
         of <code>FilterOutputStream</code> should provide a more efficient
         implementation of this method.
        @param b the data.
        @param off the start offset in the data.
        @param len the number of bytes to write.
        @exception IOException if an I/O error occurs.
        @see java.io.FilterOutputStream#write(int)
        """
        ...

    @property
    def progress(self) -> None: ...  # No getter available.

    @progress.setter
    def progress(self, value: int) -> None: ...
