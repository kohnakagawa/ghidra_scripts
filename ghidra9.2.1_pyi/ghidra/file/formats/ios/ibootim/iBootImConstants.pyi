import java.lang


class iBootImConstants(object):
    COMPRESSION_LZSS_BE: int = 1819964275
    COMPRESSION_LZSS_LE: int = 1936947820
    FORMAT_ARGB: int = 1634887522
    FORMAT_GREY: int = 1735550329
    HEADER_LENGTH: int = 64
    PADDING_LENGTH: int = 40
    SIGNATURE: unicode = u'iBootIm'
    SIGNATURE_BYTES: List[int] = array('b', [105, 66, 111, 111, 116, 73, 109, 0])
    SIGNATURE_LENGTH: int = 8



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
