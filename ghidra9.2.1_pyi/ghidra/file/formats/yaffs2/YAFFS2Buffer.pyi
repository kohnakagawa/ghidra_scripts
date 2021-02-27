from typing import List
import java.lang


class YAFFS2Buffer(object):




    @overload
    def __init__(self, __a0: java.io.InputStream): ...

    @overload
    def __init__(self, __a0: java.io.InputStream, __a1: int): ...



    def close(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getRecordSize(self) -> int: ...

    def hashCode(self) -> int: ...

    def isEOFRecord(self, __a0: List[int]) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def readRecord(self) -> List[int]: ...

    def skip(self, __a0: long) -> long: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def recordSize(self) -> int: ...
