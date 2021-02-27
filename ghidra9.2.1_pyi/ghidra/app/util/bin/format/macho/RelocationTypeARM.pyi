from typing import List
import ghidra.app.util.bin.format.macho
import java.lang


class RelocationTypeARM(java.lang.Enum):
    ARM_RELOC_BR24: ghidra.app.util.bin.format.macho.RelocationTypeARM = ARM_RELOC_BR24
    ARM_RELOC_HALF: ghidra.app.util.bin.format.macho.RelocationTypeARM = ARM_RELOC_HALF
    ARM_RELOC_HALF_SECTDIFF: ghidra.app.util.bin.format.macho.RelocationTypeARM = ARM_RELOC_HALF_SECTDIFF
    ARM_RELOC_LOCAL_SECTDIFF: ghidra.app.util.bin.format.macho.RelocationTypeARM = ARM_RELOC_LOCAL_SECTDIFF
    ARM_RELOC_PAIR: ghidra.app.util.bin.format.macho.RelocationTypeARM = ARM_RELOC_PAIR
    ARM_RELOC_PB_LA_PTR: ghidra.app.util.bin.format.macho.RelocationTypeARM = ARM_RELOC_PB_LA_PTR
    ARM_RELOC_SECTDIFF: ghidra.app.util.bin.format.macho.RelocationTypeARM = ARM_RELOC_SECTDIFF
    ARM_RELOC_VANILLA: ghidra.app.util.bin.format.macho.RelocationTypeARM = ARM_RELOC_VANILLA
    ARM_THUMB_32_BRANCH: ghidra.app.util.bin.format.macho.RelocationTypeARM = ARM_THUMB_32_BRANCH
    ARM_THUMB_RELOC_BR22: ghidra.app.util.bin.format.macho.RelocationTypeARM = ARM_THUMB_RELOC_BR22







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
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.macho.RelocationTypeARM: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.macho.RelocationTypeARM]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
