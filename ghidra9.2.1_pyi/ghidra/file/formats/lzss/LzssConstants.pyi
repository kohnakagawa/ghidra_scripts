import java.lang


class LzssConstants(object):
    HEADER_LENGTH: int = 384
    PADDING_LENGTH: int = 364
    SIGNATURE_COMPRESSION: int = 1668246896
    SIGNATURE_COMPRESSION_BYTES: List[int] = array('b', [99, 111, 109, 112])
    SIGNATURE_LZSS: int = 1819964275
    SIGNATURE_LZSS_BYTES: List[int] = array('b', [108, 122, 115, 115])



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
