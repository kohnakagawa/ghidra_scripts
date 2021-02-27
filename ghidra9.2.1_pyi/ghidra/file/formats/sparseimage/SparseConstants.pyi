import java.lang


class SparseConstants(object):
    CHUNK_TYPE_CRC32: int = -13628
    CHUNK_TYPE_DONT_CARE: int = -13629
    CHUNK_TYPE_FILL: int = -13630
    CHUNK_TYPE_RAW: int = -13631
    MAJOR_VERSION_NUMBER: int = 1
    SPARSE_HEADER_MAGIC: int = -316211398



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
