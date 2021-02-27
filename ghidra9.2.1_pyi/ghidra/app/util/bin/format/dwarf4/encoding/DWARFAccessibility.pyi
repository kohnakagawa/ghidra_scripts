from typing import List
import ghidra.app.util.bin.format.dwarf4.encoding
import java.lang


class DWARFAccessibility(java.lang.Enum):
    DW_ACCESS_private: ghidra.app.util.bin.format.dwarf4.encoding.DWARFAccessibility = DW_ACCESS_private
    DW_ACCESS_protected: ghidra.app.util.bin.format.dwarf4.encoding.DWARFAccessibility = DW_ACCESS_protected
    DW_ACCESS_public: ghidra.app.util.bin.format.dwarf4.encoding.DWARFAccessibility = DW_ACCESS_public







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def find(__a0: java.lang.Number) -> ghidra.app.util.bin.format.dwarf4.encoding.DWARFAccessibility: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def getValue(self) -> int: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.dwarf4.encoding.DWARFAccessibility: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.dwarf4.encoding.DWARFAccessibility]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def value(self) -> int: ...
