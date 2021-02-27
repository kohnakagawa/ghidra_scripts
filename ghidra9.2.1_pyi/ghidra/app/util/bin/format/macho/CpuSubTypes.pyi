import java.lang


class CpuSubTypes(object):
    CPU_SUBTYPE_386: int = 3
    CPU_SUBTYPE_486: int = 4
    CPU_SUBTYPE_486SX: int = 132
    CPU_SUBTYPE_586: int = 5
    CPU_SUBTYPE_ARM_ALL: int = 0
    CPU_SUBTYPE_ARM_V4T: int = 5
    CPU_SUBTYPE_ARM_V5: int = 7
    CPU_SUBTYPE_ARM_V5TEJ: int = 7
    CPU_SUBTYPE_ARM_V6: int = 6
    CPU_SUBTYPE_ARM_V6M: int = 14
    CPU_SUBTYPE_ARM_V7: int = 9
    CPU_SUBTYPE_ARM_V7EM: int = 16
    CPU_SUBTYPE_ARM_V7F: int = 10
    CPU_SUBTYPE_ARM_V7K: int = 12
    CPU_SUBTYPE_ARM_V7M: int = 15
    CPU_SUBTYPE_ARM_V7S: int = 11
    CPU_SUBTYPE_ARM_XSCALE: int = 8
    CPU_SUBTYPE_BIG_ENDIAN: int = 1
    CPU_SUBTYPE_CELERON: int = 103
    CPU_SUBTYPE_CELERON_MOBILE: int = 119
    CPU_SUBTYPE_HPPA_7100: int = 0
    CPU_SUBTYPE_HPPA_7100LC: int = 1
    CPU_SUBTYPE_HPPA_ALL: int = 0
    CPU_SUBTYPE_I386_ALL: int = 3
    CPU_SUBTYPE_I860_860: int = 1
    CPU_SUBTYPE_I860_ALL: int = 0
    CPU_SUBTYPE_ITANIUM: int = 11
    CPU_SUBTYPE_ITANIUM_2: int = 27
    CPU_SUBTYPE_LITTLE_ENDIAN: int = 0
    CPU_SUBTYPE_MC68030: int = 1
    CPU_SUBTYPE_MC68030_ONLY: int = 3
    CPU_SUBTYPE_MC68040: int = 2
    CPU_SUBTYPE_MC680x0_ALL: int = 1
    CPU_SUBTYPE_MC88000_ALL: int = 0
    CPU_SUBTYPE_MC88100: int = 1
    CPU_SUBTYPE_MC88110: int = 2
    CPU_SUBTYPE_MC98000_ALL: int = 0
    CPU_SUBTYPE_MC98601: int = 1
    CPU_SUBTYPE_MIPS_ALL: int = 0
    CPU_SUBTYPE_MIPS_R2000: int = 5
    CPU_SUBTYPE_MIPS_R2000a: int = 4
    CPU_SUBTYPE_MIPS_R2300: int = 1
    CPU_SUBTYPE_MIPS_R2600: int = 2
    CPU_SUBTYPE_MIPS_R2800: int = 3
    CPU_SUBTYPE_MIPS_R3000: int = 7
    CPU_SUBTYPE_MIPS_R3000a: int = 6
    CPU_SUBTYPE_MULTIPLE: int = -1
    CPU_SUBTYPE_PENT: int = 5
    CPU_SUBTYPE_PENTII_M3: int = 54
    CPU_SUBTYPE_PENTII_M5: int = 86
    CPU_SUBTYPE_PENTIUM_3: int = 8
    CPU_SUBTYPE_PENTIUM_3_M: int = 24
    CPU_SUBTYPE_PENTIUM_3_XEON: int = 40
    CPU_SUBTYPE_PENTIUM_4: int = 10
    CPU_SUBTYPE_PENTIUM_4_M: int = 26
    CPU_SUBTYPE_PENTIUM_M: int = 9
    CPU_SUBTYPE_PENTPRO: int = 22
    CPU_SUBTYPE_POWERPC_601: int = 1
    CPU_SUBTYPE_POWERPC_602: int = 2
    CPU_SUBTYPE_POWERPC_603: int = 3
    CPU_SUBTYPE_POWERPC_603e: int = 4
    CPU_SUBTYPE_POWERPC_603ev: int = 5
    CPU_SUBTYPE_POWERPC_604: int = 6
    CPU_SUBTYPE_POWERPC_604e: int = 7
    CPU_SUBTYPE_POWERPC_620: int = 8
    CPU_SUBTYPE_POWERPC_7400: int = 10
    CPU_SUBTYPE_POWERPC_7450: int = 11
    CPU_SUBTYPE_POWERPC_750: int = 9
    CPU_SUBTYPE_POWERPC_970: int = 100
    CPU_SUBTYPE_POWERPC_ALL: int = 0
    CPU_SUBTYPE_POWERPC_Max: int = 10
    CPU_SUBTYPE_POWERPC_SCVger: int = 11
    CPU_SUBTYPE_SPARC_ALL: int = 0
    CPU_SUBTYPE_UVAXI: int = 5
    CPU_SUBTYPE_UVAXII: int = 6
    CPU_SUBTYPE_UVAXIII: int = 12
    CPU_SUBTYPE_VAX730: int = 4
    CPU_SUBTYPE_VAX750: int = 3
    CPU_SUBTYPE_VAX780: int = 1
    CPU_SUBTYPE_VAX785: int = 2
    CPU_SUBTYPE_VAX8200: int = 7
    CPU_SUBTYPE_VAX8500: int = 8
    CPU_SUBTYPE_VAX8600: int = 9
    CPU_SUBTYPE_VAX8650: int = 10
    CPU_SUBTYPE_VAX8800: int = 11
    CPU_SUBTYPE_VAX_ALL: int = 0
    CPU_SUBTYPE_X86_ALL: int = 3
    CPU_SUBTYPE_X86_ARCH1: int = 4
    CPU_SUBTYPE_XEON: int = 12
    CPU_SUBTYPE_XEON_MP: int = 28
    CPU_THREADTYPE_INTEL_HTT: int = 1



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
