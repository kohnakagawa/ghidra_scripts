import java.lang


class X86_64_ElfRelocationConstants(object):
    R_X86_64_16: int = 12
    R_X86_64_32: int = 10
    R_X86_64_32S: int = 11
    R_X86_64_64: int = 1
    R_X86_64_8: int = 14
    R_X86_64_COPY: int = 5
    R_X86_64_DTPMOD64: int = 16
    R_X86_64_DTPOFF32: int = 21
    R_X86_64_DTPOFF64: int = 17
    R_X86_64_GLOB_DAT: int = 6
    R_X86_64_GNU_VTENTRY: int = 251
    R_X86_64_GNU_VTINHERIT: int = 250
    R_X86_64_GOT32: int = 3
    R_X86_64_GOT64: int = 27
    R_X86_64_GOTOFF64: int = 25
    R_X86_64_GOTPC32: int = 26
    R_X86_64_GOTPC32_TLSDESC: int = 34
    R_X86_64_GOTPC64: int = 29
    R_X86_64_GOTPCREL: int = 9
    R_X86_64_GOTPCREL64: int = 28
    R_X86_64_GOTPCRELX: int = 41
    R_X86_64_GOTPLT64: int = 30
    R_X86_64_GOTTPOFF: int = 22
    R_X86_64_IRELATIVE: int = 37
    R_X86_64_JUMP_SLOT: int = 7
    R_X86_64_NONE: int = 0
    R_X86_64_NUM: int = 43
    R_X86_64_PC16: int = 13
    R_X86_64_PC32: int = 2
    R_X86_64_PC32_BND: int = 39
    R_X86_64_PC64: int = 24
    R_X86_64_PC8: int = 15
    R_X86_64_PLT32: int = 4
    R_X86_64_PLT32_BND: int = 40
    R_X86_64_PLTOFF64: int = 31
    R_X86_64_RELATIVE: int = 8
    R_X86_64_RELATIVE64: int = 38
    R_X86_64_REX_GOTPCRELX: int = 42
    R_X86_64_SIZE32: int = 32
    R_X86_64_SIZE64: int = 33
    R_X86_64_TLSDESC: int = 36
    R_X86_64_TLSDESC_CALL: int = 35
    R_X86_64_TLSGD: int = 19
    R_X86_64_TLSLD: int = 20
    R_X86_64_TPOFF32: int = 23
    R_X86_64_TPOFF64: int = 18







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
