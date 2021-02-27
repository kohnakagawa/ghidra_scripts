from typing import List
import java.io
import java.lang


class MemoryBlockInputStream(java.io.InputStream):
    """
    Maps a MemoryBlockDB into an InputStream.
    """





    def __init__(self): ...



    def available(self) -> int:
        """
        @see java.io.InputStream#available()
        """
        ...

    def close(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def mark(self, readlimit: int) -> None:
        """
        @see java.io.InputStream#mark(int)
        """
        ...

    def markSupported(self) -> bool:
        """
        @see java.io.InputStream#markSupported()
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def nullInputStream() -> java.io.InputStream: ...

    @overload
    def read(self) -> int:
        """
        @see java.io.InputStream#read()
        """
        ...

    @overload
    def read(self, __a0: List[int]) -> int: ...

    @overload
    def read(self, b: List[int], off: int, len: int) -> int: ...

    def readAllBytes(self) -> List[int]: ...

    @overload
    def readNBytes(self, __a0: int) -> List[int]: ...

    @overload
    def readNBytes(self, __a0: List[int], __a1: int, __a2: int) -> int: ...

    def reset(self) -> None:
        """
        @see java.io.InputStream#reset()
        """
        ...

    def skip(self, n: long) -> long:
        """
        @see java.io.InputStream#skip(long)
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
