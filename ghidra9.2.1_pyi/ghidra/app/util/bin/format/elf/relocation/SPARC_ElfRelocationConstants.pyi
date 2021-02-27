import java.lang


class SPARC_ElfRelocationConstants(object):
    R_SPARC_10: int = 30
    R_SPARC_11: int = 31
    R_SPARC_13: int = 11
    R_SPARC_16: int = 2
    R_SPARC_22: int = 10
    R_SPARC_32: int = 3
    R_SPARC_5: int = 44
    R_SPARC_6: int = 45
    R_SPARC_7: int = 43
    R_SPARC_8: int = 1
    R_SPARC_COPY: int = 19
    R_SPARC_DISP16: int = 5
    R_SPARC_DISP32: int = 6
    R_SPARC_DISP8: int = 4
    R_SPARC_GLOB_DAT: int = 20
    R_SPARC_GOT10: int = 13
    R_SPARC_GOT13: int = 14
    R_SPARC_GOT22: int = 15
    R_SPARC_HI22: int = 9
    R_SPARC_HIPLT22: int = 25
    R_SPARC_JMP_SLOT: int = 21
    R_SPARC_LO10: int = 12
    R_SPARC_LOPLT10: int = 26
    R_SPARC_NONE: int = 0
    R_SPARC_PC10: int = 16
    R_SPARC_PC22: int = 17
    R_SPARC_PCPLT10: int = 29
    R_SPARC_PCPLT22: int = 28
    R_SPARC_PCPLT32: int = 27
    R_SPARC_PLT32: int = 24
    R_SPARC_RELATIVE: int = 22
    R_SPARC_UA32: int = 23
    R_SPARC_WDISP16: int = 40
    R_SPARC_WDISP19: int = 41
    R_SPARC_WDISP22: int = 8
    R_SPARC_WDISP30: int = 7
    R_SPARC_WPLT30: int = 18







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
