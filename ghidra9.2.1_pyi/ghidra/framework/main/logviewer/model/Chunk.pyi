import java.lang


class Chunk(object):
    """
    A chunk represents the basic unit of text that is displayed in the FVTable. This does
     NOT contain the actual text being displayed; rather it contains metadata describing the
     text (start/end byte positions, number of lines in the chunk, etc...).

     It should be noted that chunks are transient - they are created and destroyed as different
     sections of the file are required for display.
    """

    end: long
    linesInChunk: int
    rowToFilePositionMap: java.util.Map
    start: long



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
