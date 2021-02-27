import java.lang


class PowerPC_ElfRelocationConstants(object):
    PPC_HALF16: int = 65535
    PPC_LOW14: int = 2162684
    PPC_LOW24: int = 67108860
    PPC_WORD30: int = -4
    PPC_WORD32: int = -1
    R_PPC_ADDR14: int = 7
    R_PPC_ADDR14_BRNTAKEN: int = 9
    R_PPC_ADDR14_BRTAKEN: int = 8
    R_PPC_ADDR16: int = 3
    R_PPC_ADDR16_HA: int = 6
    R_PPC_ADDR16_HI: int = 5
    R_PPC_ADDR16_LO: int = 4
    R_PPC_ADDR24: int = 2
    R_PPC_ADDR30: int = 37
    R_PPC_ADDR32: int = 1
    R_PPC_COPY: int = 19
    R_PPC_GLOB_DAT: int = 20
    R_PPC_GOT16: int = 14
    R_PPC_GOT16_HA: int = 17
    R_PPC_GOT16_HI: int = 16
    R_PPC_GOT16_LO: int = 15
    R_PPC_JMP_SLOT: int = 21
    R_PPC_LOCAL24PC: int = 23
    R_PPC_NONE: int = 0
    R_PPC_PLT16_HA: int = 31
    R_PPC_PLT16_HI: int = 30
    R_PPC_PLT16_LO: int = 29
    R_PPC_PLT32: int = 27
    R_PPC_PLTREL24: int = 18
    R_PPC_PLTREL32: int = 28
    R_PPC_REL14: int = 11
    R_PPC_REL14_BRNTAKEN: int = 13
    R_PPC_REL14_BRTAKEN: int = 12
    R_PPC_REL24: int = 10
    R_PPC_REL32: int = 26
    R_PPC_RELATIVE: int = 22
    R_PPC_SDAREL16: int = 32
    R_PPC_SECTOFF: int = 33
    R_PPC_SECTOFF_HA: int = 36
    R_PPC_SECTOFF_HI: int = 35
    R_PPC_SECTOFF_LO: int = 34
    R_PPC_UADDR16: int = 25
    R_PPC_UADDR32: int = 24







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
