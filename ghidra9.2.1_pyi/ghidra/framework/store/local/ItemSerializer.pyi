import ghidra.util.task
import java.io
import java.lang


class ItemSerializer(object):
    """
    ItemSerializer facilitates the compressing and writing of a data stream
     to a "packed" file.  The resulting "packed" file will contain the following meta-data
     which is available after construction:

     Item name
     Content type (int)
     File type (int)
     Data length

    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @overload
    @staticmethod
    def isPackedFile(file: java.io.File) -> bool:
        """
        A simple utility method to determine if the given file is a packed file as created by
         this class.
        @param file The file to check
        @return True if it is a packed file
        @throws IOException If there is a problem reading the given file
        """
        ...

    @overload
    @staticmethod
    def isPackedFile(inputStream: java.io.InputStream) -> bool:
        """
        A convenience method for checking if the file denoted by the given inputStream is a
         packed file.
         <p>
         <b>Note: </b> This method will NOT close the given inputStream.
        @param inputStream a stream for accessing bytes of what may be a packed file
        @return true if the bytes from the inputStream represent the bytes of a packed file
        @throws IOException If there is a problem accessing the inputStream
        @see #isPackedFile(File)
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def outputItem(itemName: unicode, contentType: unicode, fileType: int, length: long, content: java.io.InputStream, packedFile: java.io.File, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Read and compress data from the specified content stream and write to
         a packed file along with additional meta-data.
        @param itemName item name
        @param contentType content type
        @param fileType file type
        @param length content length to be read
        @param content content input stream
        @param packedFile output packed file to be created
        @param monitor task monitor
        @throws CancelledException
        @throws IOException
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
