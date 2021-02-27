from typing import List
import ghidra.app.util.bin.format.macho
import java.lang


class RelocationTypeARM64(java.lang.Enum):
    ARM64_RELOC_ADDEND: ghidra.app.util.bin.format.macho.RelocationTypeARM64 = ARM64_RELOC_ADDEND
    ARM64_RELOC_BRANCH26: ghidra.app.util.bin.format.macho.RelocationTypeARM64 = ARM64_RELOC_BRANCH26
    ARM64_RELOC_GOT_LOAD_PAGE21: ghidra.app.util.bin.format.macho.RelocationTypeARM64 = ARM64_RELOC_GOT_LOAD_PAGE21
    ARM64_RELOC_GOT_LOAD_PAGEOFF12: ghidra.app.util.bin.format.macho.RelocationTypeARM64 = ARM64_RELOC_GOT_LOAD_PAGEOFF12
    ARM64_RELOC_PAGE21: ghidra.app.util.bin.format.macho.RelocationTypeARM64 = ARM64_RELOC_PAGE21
    ARM64_RELOC_PAGEOFF12: ghidra.app.util.bin.format.macho.RelocationTypeARM64 = ARM64_RELOC_PAGEOFF12
    ARM64_RELOC_POINTER_TO_GOT: ghidra.app.util.bin.format.macho.RelocationTypeARM64 = ARM64_RELOC_POINTER_TO_GOT
    ARM64_RELOC_SUBTRACTOR: ghidra.app.util.bin.format.macho.RelocationTypeARM64 = ARM64_RELOC_SUBTRACTOR
    ARM64_RELOC_TLVP_LOAD_PAGE21: ghidra.app.util.bin.format.macho.RelocationTypeARM64 = ARM64_RELOC_TLVP_LOAD_PAGE21
    ARM64_RELOC_TLVP_LOAD_PAGEOFF12: ghidra.app.util.bin.format.macho.RelocationTypeARM64 = ARM64_RELOC_TLVP_LOAD_PAGEOFF12
    ARM64_RELOC_UNSIGNED: ghidra.app.util.bin.format.macho.RelocationTypeARM64 = ARM64_RELOC_UNSIGNED







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
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.macho.RelocationTypeARM64: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.macho.RelocationTypeARM64]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
