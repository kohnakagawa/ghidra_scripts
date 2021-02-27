import java.lang


class GIFResource(object):
    """
    Class for determining the size of a GIF image. It loads just enough of the GIF information to
     follow the data block links and read the bytes until the terminator is hit.  The amount of
     bytes read indicate the number of bytes the GIF data type is consume.
    """





    def __init__(self, buf: ghidra.program.model.mem.MemBuffer): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLength(self) -> int: ...

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

    @property
    def length(self) -> int: ...
