import java.lang


class PowerPC64_ElfRelocationConstants(object):
    PPC64_HALF16: int = 65535
    PPC64_LOW14: int = 2162684
    PPC64_LOW24: int = 67108860
    PPC64_WORD30: int = -4
    PPC64_WORD32: int = -1
    R_PPC64_ADDR14: int = 7
    R_PPC64_ADDR14_BRNTAKEN: int = 9
    R_PPC64_ADDR14_BRTAKEN: int = 8
    R_PPC64_ADDR16: int = 3
    R_PPC64_ADDR16_DS: int = 56
    R_PPC64_ADDR16_HA: int = 6
    R_PPC64_ADDR16_HI: int = 5
    R_PPC64_ADDR16_HIGHER: int = 39
    R_PPC64_ADDR16_HIGHERA: int = 40
    R_PPC64_ADDR16_HIGHEST: int = 41
    R_PPC64_ADDR16_HIGHESTA: int = 42
    R_PPC64_ADDR16_LO: int = 4
    R_PPC64_ADDR16_LO_DS: int = 57
    R_PPC64_ADDR24: int = 2
    R_PPC64_ADDR30: int = 37
    R_PPC64_ADDR32: int = 1
    R_PPC64_ADDR64: int = 38
    R_PPC64_COPY: int = 19
    R_PPC64_DTPMOD64: int = 68
    R_PPC64_DTPREL16: int = 74
    R_PPC64_DTPREL16_DS: int = 101
    R_PPC64_DTPREL16_HA: int = 77
    R_PPC64_DTPREL16_HI: int = 76
    R_PPC64_DTPREL16_HIGHER: int = 103
    R_PPC64_DTPREL16_HIGHERA: int = 104
    R_PPC64_DTPREL16_HIGHEST: int = 105
    R_PPC64_DTPREL16_HIGHESTA: int = 106
    R_PPC64_DTPREL16_LO: int = 75
    R_PPC64_DTPREL16_LO_DS: int = 102
    R_PPC64_DTPREL64: int = 78
    R_PPC64_GLOB_DAT: int = 20
    R_PPC64_GOT16: int = 14
    R_PPC64_GOT16_DS: int = 58
    R_PPC64_GOT16_HA: int = 17
    R_PPC64_GOT16_HI: int = 16
    R_PPC64_GOT16_LO: int = 15
    R_PPC64_GOT16_LO_DS: int = 59
    R_PPC64_GOT_DTPREL16_DS: int = 91
    R_PPC64_GOT_DTPREL16_HA: int = 94
    R_PPC64_GOT_DTPREL16_HI: int = 93
    R_PPC64_GOT_DTPREL16_LO_DS: int = 92
    R_PPC64_GOT_TLSGD16: int = 79
    R_PPC64_GOT_TLSGD16_HA: int = 82
    R_PPC64_GOT_TLSGD16_HI: int = 81
    R_PPC64_GOT_TLSGD16_LO: int = 80
    R_PPC64_GOT_TLSLD16: int = 83
    R_PPC64_GOT_TLSLD16_HA: int = 86
    R_PPC64_GOT_TLSLD16_HI: int = 85
    R_PPC64_GOT_TLSLD16_LO: int = 84
    R_PPC64_GOT_TPREL16_DS: int = 87
    R_PPC64_GOT_TPREL16_HA: int = 90
    R_PPC64_GOT_TPREL16_HI: int = 89
    R_PPC64_GOT_TPREL16_LO_DS: int = 88
    R_PPC64_JMP_SLOT: int = 21
    R_PPC64_NONE: int = 0
    R_PPC64_PLT16_HA: int = 31
    R_PPC64_PLT16_HI: int = 30
    R_PPC64_PLT16_LO: int = 29
    R_PPC64_PLT16_LO_DS: int = 60
    R_PPC64_PLT32: int = 27
    R_PPC64_PLT64: int = 45
    R_PPC64_PLTGOT16: int = 52
    R_PPC64_PLTGOT16_DS: int = 65
    R_PPC64_PLTGOT16_HA: int = 55
    R_PPC64_PLTGOT16_HI: int = 54
    R_PPC64_PLTGOT16_LO: int = 53
    R_PPC64_PLTGOT16_LO_DS: int = 66
    R_PPC64_PLTREL32: int = 28
    R_PPC64_PLTREL64: int = 46
    R_PPC64_REL14: int = 11
    R_PPC64_REL14_BRNTAKEN: int = 13
    R_PPC64_REL14_BRTAKEN: int = 12
    R_PPC64_REL24: int = 10
    R_PPC64_REL32: int = 26
    R_PPC64_REL64: int = 44
    R_PPC64_RELATIVE: int = 22
    R_PPC64_SECTOFF: int = 33
    R_PPC64_SECTOFF_DS: int = 61
    R_PPC64_SECTOFF_HA: int = 36
    R_PPC64_SECTOFF_HI: int = 35
    R_PPC64_SECTOFF_LO: int = 34
    R_PPC64_SECTOFF_LO_DS: int = 62
    R_PPC64_TLS: int = 67
    R_PPC64_TOC: int = 51
    R_PPC64_TOC16: int = 47
    R_PPC64_TOC16_DS: int = 63
    R_PPC64_TOC16_HA: int = 50
    R_PPC64_TOC16_HI: int = 49
    R_PPC64_TOC16_LO: int = 48
    R_PPC64_TOC16_LO_DS: int = 64
    R_PPC64_TPREL16: int = 69
    R_PPC64_TPREL16_DS: int = 95
    R_PPC64_TPREL16_HA: int = 72
    R_PPC64_TPREL16_HI: int = 71
    R_PPC64_TPREL16_HIGHER: int = 97
    R_PPC64_TPREL16_HIGHERA: int = 98
    R_PPC64_TPREL16_HIGHEST: int = 99
    R_PPC64_TPREL16_HIGHESTA: int = 100
    R_PPC64_TPREL16_LO: int = 60
    R_PPC64_TPREL16_LO_DS: int = 96
    R_PPC64_TPREL64: int = 73
    R_PPC64_UADDR16: int = 25
    R_PPC64_UADDR32: int = 24
    R_PPC64_UADDR64: int = 43







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
