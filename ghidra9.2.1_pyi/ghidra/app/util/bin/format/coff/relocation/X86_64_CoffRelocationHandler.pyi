import ghidra.app.util.bin.format.coff
import ghidra.app.util.bin.format.coff.relocation
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.symbol
import java.lang


class X86_64_CoffRelocationHandler(ghidra.app.util.bin.format.coff.relocation.CoffRelocationHandler):
    IMAGE_REL_AMD64_ABSOLUTE: int = 0
    IMAGE_REL_AMD64_ADDR32: int = 2
    IMAGE_REL_AMD64_ADDR32NB: int = 3
    IMAGE_REL_AMD64_ADDR64: int = 1
    IMAGE_REL_AMD64_PAIR: int = 15
    IMAGE_REL_AMD64_REL32: int = 4
    IMAGE_REL_AMD64_REL32_1: int = 5
    IMAGE_REL_AMD64_REL32_2: int = 6
    IMAGE_REL_AMD64_REL32_3: int = 7
    IMAGE_REL_AMD64_REL32_4: int = 8
    IMAGE_REL_AMD64_REL32_5: int = 9
    IMAGE_REL_AMD64_SECREL: int = 11
    IMAGE_REL_AMD64_SECREL7: int = 12
    IMAGE_REL_AMD64_SECTION: int = 10
    IMAGE_REL_AMD64_SREL32: int = 14
    IMAGE_REL_AMD64_SSPAN32: int = 16
    IMAGE_REL_AMD64_TOKEN: int = 13



    def __init__(self): ...



    def canRelocate(self, __a0: ghidra.app.util.bin.format.coff.CoffFileHeader) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def relocate(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address, __a2: ghidra.program.model.symbol.Symbol, __a3: ghidra.app.util.bin.format.coff.CoffRelocation) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
