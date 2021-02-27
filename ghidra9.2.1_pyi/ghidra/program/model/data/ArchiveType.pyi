from typing import List
import ghidra.program.model.data
import java.lang


class ArchiveType(java.lang.Enum):
    BUILT_IN: ghidra.program.model.data.ArchiveType = BUILT_IN
    FILE: ghidra.program.model.data.ArchiveType = FILE
    PROGRAM: ghidra.program.model.data.ArchiveType = PROGRAM
    PROJECT: ghidra.program.model.data.ArchiveType = PROJECT
    TEST: ghidra.program.model.data.ArchiveType = TEST







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isBuiltIn(self) -> bool: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.program.model.data.ArchiveType: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.program.model.data.ArchiveType]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def builtIn(self) -> bool: ...
