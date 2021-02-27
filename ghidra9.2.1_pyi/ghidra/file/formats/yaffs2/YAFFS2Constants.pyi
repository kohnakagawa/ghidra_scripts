import java.lang


class YAFFS2Constants(object):
    ALIAS_FILE_NAME_SIZE: int = 160
    DATA_BUFFER_SIZE: int = 2048
    EMPTY_DATA_SIZE: int = 1536
    EXTENDED_TAGS_SIZE: int = 64
    FILE_NAME_SIZE: int = 256
    HEADER_SIZE: int = 512
    MAGIC_SIZE: int = 11
    RECORD_SIZE: int = 2112



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
