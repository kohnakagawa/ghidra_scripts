import java.io
import java.lang


class LzssCodec(object):
    F: int = 18
    N: int = 4096
    NIL: int = 4096
    THRESHOLD: int = 2



    def __init__(self): ...



    @staticmethod
    def compress(__a0: java.io.OutputStream, __a1: java.io.InputStream) -> None: ...

    @staticmethod
    def decompress(__a0: java.io.OutputStream, __a1: java.io.InputStream) -> None: ...

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
