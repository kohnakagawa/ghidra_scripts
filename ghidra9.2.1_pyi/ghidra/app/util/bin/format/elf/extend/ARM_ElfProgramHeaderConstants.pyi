import java.lang


class ARM_ElfProgramHeaderConstants(object):
    EF_ARM_BE8: int = 8388608
    EF_ARM_EABIMASK: int = -16777216
    PT_ARM_ARCHEXT_ARCHMSK: int = 255
    PT_ARM_ARCHEXT_ARCH_UNKN: int = 0
    PT_ARM_ARCHEXT_ARCHv4: int = 1
    PT_ARM_ARCHEXT_ARCHv4T: int = 2
    PT_ARM_ARCHEXT_ARCHv5T: int = 3
    PT_ARM_ARCHEXT_ARCHv5TE: int = 4
    PT_ARM_ARCHEXT_ARCHv5TEJ: int = 5
    PT_ARM_ARCHEXT_ARCHv6: int = 6
    PT_ARM_ARCHEXT_ARCHv6K: int = 9
    PT_ARM_ARCHEXT_ARCHv6KZ: int = 7
    PT_ARM_ARCHEXT_ARCHv6M: int = 11
    PT_ARM_ARCHEXT_ARCHv6SM: int = 12
    PT_ARM_ARCHEXT_ARCHv6T2: int = 8
    PT_ARM_ARCHEXT_ARCHv7: int = 10
    PT_ARM_ARCHEXT_ARCHv7EM: int = 13
    PT_ARM_ARCHEXT_FMTMSK: int = -16777216
    PT_ARM_ARCHEXT_FMT_ABI: int = 16777216
    PT_ARM_ARCHEXT_FMT_OS: int = 0
    PT_ARM_ARCHEXT_PROFMSK: int = 16711680
    PT_ARM_ARCHEXT_PROF_ARM: int = 4259840
    PT_ARM_ARCHEXT_PROF_CLASSIC: int = 5439488
    PT_ARM_ARCHEXT_PROF_MC: int = 5046272
    PT_ARM_ARCHEXT_PROF_NONE: int = 0
    PT_ARM_ARCHEXT_PROF_RT: int = 5373952



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
