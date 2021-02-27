import java.lang


class TestProcessorConstants(object):
    PROCESSOR_8051: ghidra.program.model.lang.Processor = 8051
    PROCESSOR_ARM: ghidra.program.model.lang.Processor = ARM
    PROCESSOR_DATA: ghidra.program.model.lang.Processor = DATA
    PROCESSOR_POWERPC: ghidra.program.model.lang.Processor = PowerPC
    PROCESSOR_SPARC: ghidra.program.model.lang.Processor = Sparc
    PROCESSOR_TMS320C3x: ghidra.program.model.lang.Processor = TMS320C3x
    PROCESSOR_X86: ghidra.program.model.lang.Processor = x86
    PROCESSOR_Z80: ghidra.program.model.lang.Processor = Z80



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
