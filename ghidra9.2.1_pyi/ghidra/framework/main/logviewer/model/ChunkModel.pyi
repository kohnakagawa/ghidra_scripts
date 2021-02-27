from typing import Iterator
import ghidra.framework.main.logviewer.model
import java.lang
import java.util
import java.util.function


class ChunkModel(object, java.lang.Iterable):
    """
    Stores all chunks read-in by the ChunkReader. The model is responsible for handling all
     interaction with the list of chunks.
    """

    MAX_VISIBLE_CHUNKS: int
    NUM_LINES: int
    selectedByteEnd: long
    selectedByteStart: long



    def __init__(self): ...

    def __iter__(self): ...

    @overload
    def add(self, chunk: ghidra.framework.main.logviewer.model.Chunk) -> None:
        """
        Adds the given chunk to the model.
        @param chunk
        """
        ...

    @overload
    def add(self, index: int, chunk: ghidra.framework.main.logviewer.model.Chunk) -> None:
        """
        Adds a chunk at the given index to the model.
        @param index
        @param chunk
        """
        ...

    def clear(self) -> None:
        """
        Clears all chunks from the model.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def get(self, index: int) -> ghidra.framework.main.logviewer.model.Chunk:
        """
        Returns the chunk at the given index.
        @param index
        @return
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFilePositionForRow(self, row: int) -> ghidra.framework.main.logviewer.model.Pair:
        """
        Returns the start/end byte positions within the input file for the given row.

         To do this we have to loop over all chunks in the {@link ChunkModel} and count the number
         of lines in each chunk until we get to the line (row) we're looking for. We then grab the
         correct value from the byteMap for that chunk line, which is the starting byte for it.
        @param row
        @return the byte position in the file this row corresponds to
        """
        ...

    def getNumChunks(self) -> int:
        """
        @return
        """
        ...

    def getRowForBytePos(self, selectedByte: long) -> int:
        """
        Searches the visible chunks to see if any of them contain the given byte. If so, returns
         the row in the table where it resides. Returns -1 otherwise.
        @param selectedByte
        @return
        """
        ...

    def getSize(self) -> int:
        """
        Returns the number of chunks in the model.
        @return
        """
        ...

    def hashCode(self) -> int: ...

    def iterator(self) -> Iterator[ghidra.framework.main.logviewer.model.Chunk]: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, index: int) -> ghidra.framework.main.logviewer.model.Chunk:
        """
        Removes the chunk at the given index from the model.
        @param index
        """
        ...

    def spliterator(self) -> java.util.Spliterator: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def numChunks(self) -> int: ...

    @property
    def size(self) -> int: ...
