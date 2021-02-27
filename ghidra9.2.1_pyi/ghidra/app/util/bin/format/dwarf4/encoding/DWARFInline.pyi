from typing import List
import ghidra.app.util.bin.format.dwarf4.encoding
import java.lang


class DWARFInline(java.lang.Enum):
    DW_INL_declared_inlined: ghidra.app.util.bin.format.dwarf4.encoding.DWARFInline = DW_INL_declared_inlined
    DW_INL_declared_not_inlined: ghidra.app.util.bin.format.dwarf4.encoding.DWARFInline = DW_INL_declared_not_inlined
    DW_INL_inlined: ghidra.app.util.bin.format.dwarf4.encoding.DWARFInline = DW_INL_inlined
    DW_INL_not_inlined: ghidra.app.util.bin.format.dwarf4.encoding.DWARFInline = DW_INL_not_inlined







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def find(__a0: java.lang.Number) -> ghidra.app.util.bin.format.dwarf4.encoding.DWARFInline: ...

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
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.dwarf4.encoding.DWARFInline: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.dwarf4.encoding.DWARFInline]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def value(self) -> int: ...
