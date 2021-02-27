import ghidra.app.util.bin.format.macho.threadcommand
import ghidra.program.model.data
import java.lang


class ThreadStateARM_64(ghidra.app.util.bin.format.macho.threadcommand.ThreadState):
    """
    Represents a _STRUCT_ARM_THREAD_STATE64 structure.
    """

    ARM64_THREAD_STATE: int = 6
    cpsr: int
    fp: long
    lr: long
    pad: int
    pc: long
    sp: long
    x0: long
    x1: long
    x10: long
    x11: long
    x12: long
    x13: long
    x14: long
    x15: long
    x16: long
    x17: long
    x18: long
    x19: long
    x2: long
    x20: long
    x21: long
    x22: long
    x23: long
    x24: long
    x25: long
    x26: long
    x27: long
    x28: long
    x3: long
    x4: long
    x5: long
    x6: long
    x7: long
    x8: long
    x9: long



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
