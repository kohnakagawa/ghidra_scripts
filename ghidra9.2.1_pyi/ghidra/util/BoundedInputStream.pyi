from typing import List
import java.io
import java.lang


class BoundedInputStream(java.io.InputStream):
    """
    InputStream wrapper that limits itself to a portion of the wrapped stream.
    """





    def __init__(self, wrappedInputStream: java.io.InputStream, size: long):
        """
        Creates a new instance.
        @param wrappedInputStream {@link InputStream} to wrap, already positioned to the desired
         starting position.
        @param size number of bytes to allow this wrapper to read.
        """
        ...



    def available(self) -> int: ...

    def close(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def mark(self, __a0: int) -> None: ...

    def markSupported(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def nullInputStream() -> java.io.InputStream: ...

    @overload
    def read(self) -> int: ...

    @overload
    def read(self, __a0: List[int]) -> int: ...

    @overload
    def read(self, b: List[int], off: int, len: int) -> int: ...

    def readAllBytes(self) -> List[int]: ...

    @overload
    def readNBytes(self, __a0: int) -> List[int]: ...

    @overload
    def readNBytes(self, __a0: List[int], __a1: int, __a2: int) -> int: ...

    def reset(self) -> None: ...

    def skip(self, n: long) -> long: ...

    def toString(self) -> unicode: ...

    def transferTo(self, __a0: java.io.OutputStream) -> long: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
