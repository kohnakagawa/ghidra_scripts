import ghidra.program.model.lang
import java.lang


class CpuTypes(object):
    CPU_ARCH_ABI64: int = 16777216
    CPU_ARCH_MASK: int = -16777216
    CPU_TYPE_ANY: int = -1
    CPU_TYPE_ARM: int = 12
    CPU_TYPE_ARM_64: int = 16777228
    CPU_TYPE_HPPA: int = 11
    CPU_TYPE_I386: int = 7
    CPU_TYPE_I860: int = 15
    CPU_TYPE_MC680x0: int = 6
    CPU_TYPE_MC88000: int = 13
    CPU_TYPE_MC98000: int = 10
    CPU_TYPE_POWERPC: int = 18
    CPU_TYPE_POWERPC64: int = 16777234
    CPU_TYPE_SPARC: int = 14
    CPU_TYPE_VAX: int = 1
    CPU_TYPE_X86: int = 7
    CPU_TYPE_X86_64: int = 16777223



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getMagicString(cpuType: int, cpuSubtype: int) -> unicode: ...

    @staticmethod
    def getProcessor(cpuType: int, cpuSubtype: int) -> ghidra.program.model.lang.Processor:
        """
        Returns the processor name of the given CPU type value.
        @param cpuType the CPU type value
        @param cpuSubtype the CPU subtype value
        @return the processor name of the given CPU type value
        """
        ...

    @staticmethod
    def getProcessorBitSize(cpuType: int) -> int: ...

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
