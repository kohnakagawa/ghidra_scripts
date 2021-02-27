import ghidra.app.util.bin.format.macho.threadcommand
import ghidra.program.model.data
import java.lang


class ThreadStateX86_32(ghidra.app.util.bin.format.macho.threadcommand.ThreadStateX86):
    """
    Represents a _STRUCT_X86_THREAD_STATE32 structure.
    """

    cs: int
    ds: int
    eax: int
    ebp: int
    ebx: int
    ecx: int
    edi: int
    edx: int
    eflags: int
    eip: int
    es: int
    esi: int
    esp: int
    fs: int
    gs: int
    ss: int



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
