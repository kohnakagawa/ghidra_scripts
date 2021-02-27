from typing import List
import ghidra.app.util.bin.format.macho
import java.lang


class RelocationTypeX86_64(java.lang.Enum):
    X86_64_RELOC_BRANCH: ghidra.app.util.bin.format.macho.RelocationTypeX86_64 = X86_64_RELOC_BRANCH
    X86_64_RELOC_GOT: ghidra.app.util.bin.format.macho.RelocationTypeX86_64 = X86_64_RELOC_GOT
    X86_64_RELOC_GOT_LOAD: ghidra.app.util.bin.format.macho.RelocationTypeX86_64 = X86_64_RELOC_GOT_LOAD
    X86_64_RELOC_SIGNED: ghidra.app.util.bin.format.macho.RelocationTypeX86_64 = X86_64_RELOC_SIGNED
    X86_64_RELOC_SIGNED_1: ghidra.app.util.bin.format.macho.RelocationTypeX86_64 = X86_64_RELOC_SIGNED_1
    X86_64_RELOC_SIGNED_2: ghidra.app.util.bin.format.macho.RelocationTypeX86_64 = X86_64_RELOC_SIGNED_2
    X86_64_RELOC_SIGNED_4: ghidra.app.util.bin.format.macho.RelocationTypeX86_64 = X86_64_RELOC_SIGNED_4
    X86_64_RELOC_SUBTRACTOR: ghidra.app.util.bin.format.macho.RelocationTypeX86_64 = X86_64_RELOC_SUBTRACTOR
    X86_64_RELOC_TLV: ghidra.app.util.bin.format.macho.RelocationTypeX86_64 = X86_64_RELOC_TLV
    X86_64_RELOC_UNSIGNED: ghidra.app.util.bin.format.macho.RelocationTypeX86_64 = X86_64_RELOC_UNSIGNED







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
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.macho.RelocationTypeX86_64: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.macho.RelocationTypeX86_64]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
