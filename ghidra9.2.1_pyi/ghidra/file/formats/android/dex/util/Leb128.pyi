from typing import List
import java.io
import java.lang


class Leb128(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def main(__a0: List[unicode]) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    @staticmethod
    def readSignedLeb128(__a0: List[int]) -> int: ...

    @overload
    @staticmethod
    def readSignedLeb128(__a0: java.io.ByteArrayInputStream) -> int: ...

    @overload
    @staticmethod
    def readUnsignedLeb128(__a0: List[int]) -> int: ...

    @overload
    @staticmethod
    def readUnsignedLeb128(__a0: java.io.ByteArrayInputStream) -> int: ...

    @staticmethod
    def signedLeb128Size(__a0: int) -> int: ...

    def toString(self) -> unicode: ...

    @staticmethod
    def unsignedLeb128Size(__a0: int) -> int: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @staticmethod
    def writeSignedLeb128(__a0: java.io.ByteArrayOutputStream, __a1: int) -> None: ...

    @staticmethod
    def writeUnsignedLeb128(__a0: java.io.ByteArrayOutputStream, __a1: int) -> None: ...
