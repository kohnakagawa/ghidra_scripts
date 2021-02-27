from typing import List
import ghidra.app.util.bin.format.macho
import java.lang


class RelocationTypePPC(java.lang.Enum):
    PPC_RELOC_BR14: ghidra.app.util.bin.format.macho.RelocationTypePPC = PPC_RELOC_BR14
    PPC_RELOC_BR24: ghidra.app.util.bin.format.macho.RelocationTypePPC = PPC_RELOC_BR24
    PPC_RELOC_HA16: ghidra.app.util.bin.format.macho.RelocationTypePPC = PPC_RELOC_HA16
    PPC_RELOC_HA16_SECTDIFF: ghidra.app.util.bin.format.macho.RelocationTypePPC = PPC_RELOC_HA16_SECTDIFF
    PPC_RELOC_HI16: ghidra.app.util.bin.format.macho.RelocationTypePPC = PPC_RELOC_HI16
    PPC_RELOC_HI16_SECTDIFF: ghidra.app.util.bin.format.macho.RelocationTypePPC = PPC_RELOC_HI16_SECTDIFF
    PPC_RELOC_JBSR: ghidra.app.util.bin.format.macho.RelocationTypePPC = PPC_RELOC_JBSR
    PPC_RELOC_LO14: ghidra.app.util.bin.format.macho.RelocationTypePPC = PPC_RELOC_LO14
    PPC_RELOC_LO14_SECTDIFF: ghidra.app.util.bin.format.macho.RelocationTypePPC = PPC_RELOC_LO14_SECTDIFF
    PPC_RELOC_LO16: ghidra.app.util.bin.format.macho.RelocationTypePPC = PPC_RELOC_LO16
    PPC_RELOC_LO16_SECTDIFF: ghidra.app.util.bin.format.macho.RelocationTypePPC = PPC_RELOC_LO16_SECTDIFF
    PPC_RELOC_LOCAL_SECTDIFF: ghidra.app.util.bin.format.macho.RelocationTypePPC = PPC_RELOC_LOCAL_SECTDIFF
    PPC_RELOC_PAIR: ghidra.app.util.bin.format.macho.RelocationTypePPC = PPC_RELOC_PAIR
    PPC_RELOC_PB_LA_PTR: ghidra.app.util.bin.format.macho.RelocationTypePPC = PPC_RELOC_PB_LA_PTR
    PPC_RELOC_SECTDIFF: ghidra.app.util.bin.format.macho.RelocationTypePPC = PPC_RELOC_SECTDIFF
    PPC_RELOC_VANILLA: ghidra.app.util.bin.format.macho.RelocationTypePPC = PPC_RELOC_VANILLA







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
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.macho.RelocationTypePPC: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.macho.RelocationTypePPC]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
