from typing import List
import ghidra.app.util.bin.format.pef
import java.lang


class SectionKind(java.lang.Enum):
    Code: ghidra.app.util.bin.format.pef.SectionKind = Code
    Constant: ghidra.app.util.bin.format.pef.SectionKind = Constant
    Debug: ghidra.app.util.bin.format.pef.SectionKind = Debug
    Exception: ghidra.app.util.bin.format.pef.SectionKind = Exception
    ExecutableData: ghidra.app.util.bin.format.pef.SectionKind = ExecutableData
    Loader: ghidra.app.util.bin.format.pef.SectionKind = Loader
    PackedData: ghidra.app.util.bin.format.pef.SectionKind = PackedData
    Traceback: ghidra.app.util.bin.format.pef.SectionKind = Traceback
    UnpackedData: ghidra.app.util.bin.format.pef.SectionKind = UnpackedData







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def get(__a0: int) -> ghidra.app.util.bin.format.pef.SectionKind: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def getValue(self) -> int: ...

    def hashCode(self) -> int: ...

    def isInstantiated(self) -> bool: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pef.SectionKind: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.pef.SectionKind]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def instantiated(self) -> bool: ...

    @property
    def value(self) -> int: ...
