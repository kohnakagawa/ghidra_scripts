from typing import List
import ghidra.file.formats.bplist
import java.lang


class NSNumberTypes(java.lang.Enum):
    BOOLEAN: ghidra.file.formats.bplist.NSNumberTypes = BOOLEAN
    BYTE: ghidra.file.formats.bplist.NSNumberTypes = BYTE
    INTEGER: ghidra.file.formats.bplist.NSNumberTypes = INTEGER
    LONG: ghidra.file.formats.bplist.NSNumberTypes = LONG
    REAL: ghidra.file.formats.bplist.NSNumberTypes = REAL
    SHORT: ghidra.file.formats.bplist.NSNumberTypes = SHORT







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

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
    def valueOf(__a0: unicode) -> ghidra.file.formats.bplist.NSNumberTypes: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.file.formats.bplist.NSNumberTypes]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
