from typing import List
import java.lang


class GhidraRandomAccessFile(object, java.lang.AutoCloseable):
    """
    Instances of this class support both reading and writing to a
     random access file. A random access file behaves like a large
     array of bytes stored in the file system. There is a kind of cursor,
     or index into the implied array, called the file pointer.
     This implementation relies on java.net.RandomAccessFile,
     but adds buffering to limit the amount.
    """





    def __init__(self, file: java.io.File, mode: unicode):
        """
        Creates a random access file stream to read from, and optionally to
         write to, the file specified by the {@link File} argument.  A new {@link FileDescriptor} object is created to represent this file connection.

         <p>
         This implementation relies on java.net.RandomAccessFile,
         but adds buffering to limit the amount.
         <p>

         <a id="mode"></a><p> The <code>mode</code> argument specifies the access mode
         in which the file is to be opened.  The permitted values and their
         meanings are:

         <blockquote><table><caption style="visibility:hidden;font-size:0px">Access mode permitted values and meanings</caption>
         <tr><th><p style="text-align:left">Value</p></th><th><p style="text-align:left">Meaning</p></th></tr>
         <tr><td style="vertical-align:top"><code>"r"</code></td>
             <td> Open for reading only.  Invoking any of the <code>write</code>
             methods of the resulting object will cause an {@link java.io.IOException} to be thrown. </td></tr>
         <tr><td style="vertical-align:top"><code>"rw"</code></td>
             <td> Open for reading and writing.  If the file does not already
             exist then an attempt will be made to create it. </td></tr>
         <tr><td style="vertical-align:top"><code>"rws"</code></td>
             <td> Open for reading and writing, as with <code>"rw"</code>, and also
             require that every update to the file's content or metadata be
             written synchronously to the underlying storage device.  </td></tr>
         <tr><td style="vertical-align:top"><code>"rwd"&nbsp;&nbsp;</code></td>
             <td> Open for reading and writing, as with <code>"rw"</code>, and also
             require that every update to the file's content be written
             synchronously to the underlying storage device. </td></tr>
         </table></blockquote>
        @param file the file object
        @param mode the access mode, as described
                            <a href="#mode">above</a>
        @exception IllegalArgumentException if the mode argument is not equal
                       to one of <code>"r"</code>, <code>"rw"</code>, <code>"rws"</code>, or
                       <code>"rwd"</code>
        @exception FileNotFoundException that name cannot be created, or if some other error occurs
                    while opening or creating the file
        """
        ...



    def close(self) -> None:
        """
        Closes this random access file stream and releases any system
         resources associated with the stream. A closed random access
         file cannot perform input or output operations and cannot be
         reopened.
         <p>
         If this file has an associated channel then the channel is closed as well.
        @exception IOException if an I/O error occurs.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def length(self) -> long:
        """
        Returns the length of this file.
        @return the length of this file, measured in bytes.
        @exception IOException if an I/O error occurs.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def read(self, b: List[int]) -> int:
        """
        Reads up to <code>b.length</code> bytes of data from this file
         into an array of bytes. This method blocks until at least one byte
         of input is available.
        @param b the buffer into which the data is read.
        @return the total number of bytes read into the buffer, or
                     <code>-1</code> if there is no more data because the end of
                     this file has been reached.
        @exception IOException if an I/O error occurs.
        """
        ...

    @overload
    def read(self, b: List[int], offset: int, length: int) -> int:
        """
        Reads up to <code>length</code> bytes of data from this file into an
         array of bytes. This method blocks until at least one byte of input
         is available.
        @param b the buffer into which the data is read.
        @param offset the start offset of the data.
        @param length the maximum number of bytes read.
        @return the total number of bytes read into the buffer, or
                     <code>-1</code> if there is no more data because the end of
                     the file has been reached.
        @exception IOException if an I/O error occurs.
        """
        ...

    def readByte(self) -> int:
        """
        This method reads a byte from the file, starting from the current file pointer.
         <p>
         This method blocks until the byte is read, the end of the stream
         is detected, or an exception is thrown.
        @return the next byte of this file as a signed eight-bit
                     <code>byte</code>.
        @exception EOFException if this file has reached the end.
        @exception IOException if an I/O error occurs.
        """
        ...

    def seek(self, pos: long) -> None:
        """
        Sets the file-pointer offset, measured from the beginning of this
         file, at which the next read or write occurs.  The offset may be
         set beyond the end of the file. Setting the offset beyond the end
         of the file does not change the file length.  The file length will
         change only by writing after the offset has been set beyond the end
         of the file.
        @param pos the offset position, measured in bytes from the
                           beginning of the file, at which to set the file
                           pointer.
        @throws IOException if <code>pos</code> is less than
                                  <code>0</code> or if an I/O error occurs.
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
        Writes a byte to this file, starting at the current file pointer.
        @param b the data.
        @exception IOException if an I/O error occurs.
        """
        ...

    @overload
    def write(self, b: List[int]) -> None:
        """
        Writes <code>b.length</code> bytes from the specified byte array
         to this file, starting at the current file pointer.
        @param b the data.
        @exception IOException if an I/O error occurs.
        """
        ...

    @overload
    def write(self, b: List[int], offset: int, length: int) -> None:
        """
        Writes a sub array as a sequence of bytes.
        @param b the data to be written
        @param offset the start offset in the data
        @param length the number of bytes that are written
        @exception IOException If an I/O error has occurred.
        """
        ...
