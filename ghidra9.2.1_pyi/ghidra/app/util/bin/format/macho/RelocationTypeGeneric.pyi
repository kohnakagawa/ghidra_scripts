from typing import List
import ghidra.app.util.bin.format.macho
import java.lang


class RelocationTypeGeneric(java.lang.Enum):
    GENERIC_RELOC_LOCAL_SECTDIFF: ghidra.app.util.bin.format.macho.RelocationTypeGeneric = GENERIC_RELOC_LOCAL_SECTDIFF
    GENERIC_RELOC_PAIR: ghidra.app.util.bin.format.macho.RelocationTypeGeneric = GENERIC_RELOC_PAIR
    GENERIC_RELOC_PB_LA_PTR: ghidra.app.util.bin.format.macho.RelocationTypeGeneric = GENERIC_RELOC_PB_LA_PTR
    GENERIC_RELOC_SECTDIFF: ghidra.app.util.bin.format.macho.RelocationTypeGeneric = GENERIC_RELOC_SECTDIFF
    GENERIC_RELOC_TLV: ghidra.app.util.bin.format.macho.RelocationTypeGeneric = GENERIC_RELOC_TLV
    GENERIC_RELOC_VANILLA: ghidra.app.util.bin.format.macho.RelocationTypeGeneric = GENERIC_RELOC_VANILLA







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
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.macho.RelocationTypeGeneric: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.macho.RelocationTypeGeneric]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
