import java.io
import java.lang


class RemoteBlockStreamHandle(object, java.io.Serializable):
    HEADER_LENGTH: int = 41
    HEADER_PREFIX: unicode = u'@stream:'
    HEADER_SUFFIX: unicode = u'@'
    TERM_LENGTH: int = 22
    TERM_PREFIX: unicode = u'@end:'
    TERM_SUFFIX: unicode = u'@'
    enableCompressedSerializationOutput: bool
    serialVersionUID: long = 0x1L



    def __init__(self, __a0: ghidra.server.stream.BlockStreamServer, __a1: int, __a2: int): ...



    def equals(self, __a0: object) -> bool: ...

    def getBlockCount(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isPending(self) -> bool: ...

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
    def blockCount(self) -> int: ...

    @property
    def pending(self) -> bool: ...
