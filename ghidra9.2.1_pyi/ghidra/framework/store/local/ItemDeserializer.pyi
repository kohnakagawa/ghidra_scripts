import ghidra.util.task
import java.io
import java.lang


class ItemDeserializer(object):
    """
    ItemDeserializer facilitates the reading of a compressed data stream
     contained within a "packed" file.  A "packed" file contains the following meta-data
     which is available after construction:

     Item name
     Content type (int)
     File type (int)
     Data length

    """





    @overload
    def __init__(self, packedFile: generic.jar.ResourceFile): ...

    @overload
    def __init__(self, packedFile: java.io.File):
        """
        Constructor.
        @param packedFile item to deserialize.
        @throws IOException
        """
        ...



    def dispose(self) -> None:
        """
        Close packed-file input stream and free resources.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getContentType(self) -> unicode:
        """
        Returns packed content type
        """
        ...

    def getFileType(self) -> int:
        """
        Returns packed file type.
        """
        ...

    def getItemName(self) -> unicode:
        """
        Returns packed item name
        """
        ...

    def getLength(self) -> long:
        """
        Returns unpacked data length
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def saveItem(self, out: java.io.OutputStream, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Save the item to the specified output stream.
         This method may only be invoked once.
        @param out
        @param monitor
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

    @property
    def contentType(self) -> unicode: ...

    @property
    def fileType(self) -> int: ...

    @property
    def itemName(self) -> unicode: ...

    @property
    def length(self) -> long: ...
