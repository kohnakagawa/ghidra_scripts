from typing import List
import java.io
import java.lang


class ChunkReader(object):
    """
    This class handles reading data from the input file, in the form of Chunk objects.  Each
     chunk is stored in the ChunkModel and represents a single block of text that is
     displayed in the FVTable.
    """





    def __init__(self, file: java.io.File, model: ghidra.framework.main.logviewer.model.ChunkModel):
        """
        @param file
        @param model
        @throws IOException
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFile(self) -> java.io.File:
        """
        Returns the file being read.
        @return
        """
        ...

    def getFileSize(self) -> long:
        """
        Returns the number of bytes in the input file.
        @return number of bytes
        @throws IOException
        """
        ...

    def getStartOfNextLine(self, startByte: long) -> long:
        """
        Returns the start of the next line after the given byte. To do this, simply read
         backwards from the given point until a newline or carriage return is found.
        @param startByte
        @return
        @throws IOException
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def readBytes(self, startByte: long, endByte: long) -> List[int]:
        """
        Reads all bytes from the given byte to the end byte. If the amount of bytes to be read is
         greater than the size of an INT, we will have to read this in several chunks, hence the
         need to return a list of arrays, and not just a single byte array.
        @param startByte
        @param endByte
        @return a map of all the bytes read in (index 0 is first chunk, 1 is next, etc...).
        @throws IOException
        """
        ...

    def readLastChunk(self) -> List[unicode]:
        """
        Reads one chunk from the end of the file. This is useful when scrolling to the bottom of
         the viewport.
        @return the last chunk, or an empty list
        @throws IOException
        """
        ...

    def readNextChunk(self) -> List[unicode]:
        """
        Reads the next chunk in the file past the last one specified in the {@link ChunkModel}.
        @return the lines of text read
        @throws FileNotFoundException
        @throws IOException
        """
        ...

    def readNextChunkFrom(self, startByte: long) -> List[unicode]:
        """
        Reads a chunk of data from the given location in the file.  To ensure we're always reading
         full lines, take the given start position and move forward to the next full line before
         reading.
        @param startByte the position to start reading from
        @return the lines of text read
        @throws IOException
        """
        ...

    def readPreviousChunk(self) -> List[unicode]:
        """
        Reads the chunk immediately before the first visible one.
        @return the previous chunk, or an empty list
        @throws IOException
        """
        ...

    def reload(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def file(self) -> java.io.File: ...

    @property
    def fileSize(self) -> long: ...
