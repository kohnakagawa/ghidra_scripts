import java.lang


class CrushedPNGConstants(object):
    ADAM7_INTERLACE: int = 1
    COL_INCREMENT: List[int] = array('i', [8, 8, 4, 4, 2, 2, 1])
    GENERIC_CHUNK_SIZE: int = 12
    IDAT_CHUNK: List[int] = array('b', [73, 68, 65, 84])
    IEND_CHUNK: List[int] = array('b', [73, 69, 78, 68])
    IEND_STRING: unicode = u'IEND'
    IHDR_CHUNK: List[int] = array('b', [73, 72, 68, 82])
    IHDR_CHUNK_DATA_SIZE: int = 13
    IHDR_STRING: unicode = u'IHDR'
    INITIAL_REPACK_SIZE: int = 65536
    INSERTED_IOS_CHUNK: List[int] = array('b', [67, 103, 66, 73])
    INTERLACE_NONE: int = 0
    ROW_INCREMENT: List[int] = array('i', [8, 8, 8, 4, 4, 2, 2])
    SIGNATURE_BYTES: List[int] = array('b', [-119, 80, 78, 71, 13, 10, 26, 10])
    STARTING_COL: List[int] = array('i', [0, 4, 0, 2, 0, 1, 0])
    STARTING_ROW: List[int] = array('i', [0, 0, 4, 0, 2, 0, 1])



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
