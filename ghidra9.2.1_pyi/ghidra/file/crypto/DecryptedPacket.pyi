import java.lang


class DecryptedPacket(object):
    decryptedFile: java.io.File
    decryptedStream: java.io.InputStream
    decryptedStreamLength: int



    @overload
    def __init__(self, __a0: java.io.File): ...

    @overload
    def __init__(self, __a0: java.io.InputStream, __a1: int): ...



    def dispose(self) -> None: ...

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
