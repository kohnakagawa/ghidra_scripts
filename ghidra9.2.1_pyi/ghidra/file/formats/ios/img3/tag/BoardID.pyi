from typing import List
import ghidra.file.formats.ios.img3.tag
import java.lang


class BoardID(java.lang.Enum):
    iPhone2G: ghidra.file.formats.ios.img3.tag.BoardID = iPhone2G
    iPhone3G: ghidra.file.formats.ios.img3.tag.BoardID = iPhone3G
    iPhone3GS: ghidra.file.formats.ios.img3.tag.BoardID = iPhone3GS
    iPodTouch1stGen: ghidra.file.formats.ios.img3.tag.BoardID = iPodTouch1stGen
    iPodTouch2ndGen: ghidra.file.formats.ios.img3.tag.BoardID = iPodTouch2ndGen
    iPodTouch3rdGen: ghidra.file.formats.ios.img3.tag.BoardID = iPodTouch3rdGen







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getBoardID(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.file.formats.ios.img3.tag.BoardID: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.file.formats.ios.img3.tag.BoardID]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def boardID(self) -> int: ...
