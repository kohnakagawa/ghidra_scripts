import java.lang


class AVR32_ElfRelocationConstants(object):
    DT_AVR32_GOTSZ: int = 1879048193
    EF_AVR32_LINKRELAX: int = 1
    EF_AVR32_PIC: int = 2
    R_AVR32_10UW_PCREL: int = 24
    R_AVR32_11H_PCREL: int = 23
    R_AVR32_14UW_PCREL: int = 22
    R_AVR32_16: int = 2
    R_AVR32_16B_PCREL: int = 20
    R_AVR32_16N_PCREL: int = 21
    R_AVR32_16S: int = 15
    R_AVR32_16U: int = 14
    R_AVR32_16_CP: int = 38
    R_AVR32_16_PCREL: int = 5
    R_AVR32_18W_PCREL: int = 19
    R_AVR32_21S: int = 13
    R_AVR32_22H_PCREL: int = 18
    R_AVR32_32: int = 1
    R_AVR32_32_CPENT: int = 36
    R_AVR32_32_PCREL: int = 4
    R_AVR32_8: int = 3
    R_AVR32_8S: int = 16
    R_AVR32_8S_EXT: int = 17
    R_AVR32_8_PCREL: int = 6
    R_AVR32_9H_PCREL: int = 25
    R_AVR32_9UW_PCREL: int = 26
    R_AVR32_9W_CP: int = 39
    R_AVR32_ALIGN: int = 43
    R_AVR32_CPCALL: int = 37
    R_AVR32_DIFF16: int = 8
    R_AVR32_DIFF32: int = 7
    R_AVR32_DIFF8: int = 9
    R_AVR32_GLOB_DAT: int = 41
    R_AVR32_GOT16: int = 11
    R_AVR32_GOT16S: int = 34
    R_AVR32_GOT18SW: int = 33
    R_AVR32_GOT21S: int = 32
    R_AVR32_GOT32: int = 10
    R_AVR32_GOT7UW: int = 35
    R_AVR32_GOT8: int = 12
    R_AVR32_GOTCALL: int = 30
    R_AVR32_GOTPC: int = 29
    R_AVR32_HI16: int = 27
    R_AVR32_JMP_SLOT: int = 42
    R_AVR32_LDA_GOT: int = 31
    R_AVR32_LO16: int = 28
    R_AVR32_NONE: int = 0
    R_AVR32_NUM: int = 44
    R_AVR32_RELATIVE: int = 40



    def __init__(self): ...



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
