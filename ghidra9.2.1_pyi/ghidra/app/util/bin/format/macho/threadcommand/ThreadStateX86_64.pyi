import ghidra.app.util.bin.format.macho.threadcommand
import ghidra.program.model.data
import java.lang


class ThreadStateX86_64(ghidra.app.util.bin.format.macho.threadcommand.ThreadStateX86):
    """
    Represents a _STRUCT_X86_THREAD_STATE64 structure.
    """

    cs: long
    fs: long
    gs: long
    r10: long
    r11: long
    r12: long
    r13: long
    r14: long
    r15: long
    r8: long
    r9: long
    rax: long
    rbp: long
    rbx: long
    rcx: long
    rdi: long
    rdx: long
    rflags: long
    rip: long
    rsi: long
    rsp: long



    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getInstructionPointer(self) -> long: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def instructionPointer(self) -> long: ...
