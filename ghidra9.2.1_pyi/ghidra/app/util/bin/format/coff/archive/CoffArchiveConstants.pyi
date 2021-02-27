import java.lang


class CoffArchiveConstants(object):
    END_OF_HEADER_MAGIC: unicode = u"'\n"
    MAGIC: unicode = u'!<arch>\n'
    MAGIC_BYTES: List[int] = array('b', [33, 60, 97, 114, 99, 104, 62, 10])
    MAGIC_LEN: int = 8
    MAGIC_LEN_CONST_EXPR: int = 8



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
