from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.macos.cfm
import java.lang


class CFragUsage(java.lang.Enum):
    kApplicationCFrag: ghidra.app.util.bin.format.macos.cfm.CFragUsage = kApplicationCFrag
    kDropInAdditionCFrag: ghidra.app.util.bin.format.macos.cfm.CFragUsage = kDropInAdditionCFrag
    kImportLibraryCFrag: ghidra.app.util.bin.format.macos.cfm.CFragUsage = kImportLibraryCFrag
    kStubLibraryCFrag: ghidra.app.util.bin.format.macos.cfm.CFragUsage = kStubLibraryCFrag
    kWeakStubLibraryCFrag: ghidra.app.util.bin.format.macos.cfm.CFragUsage = kWeakStubLibraryCFrag







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def get(__a0: ghidra.app.util.bin.BinaryReader) -> ghidra.app.util.bin.format.macos.cfm.CFragUsage: ...

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
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.macos.cfm.CFragUsage: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.macos.cfm.CFragUsage]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
