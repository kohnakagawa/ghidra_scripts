import ghidra.app.util.bin.format.macho.threadcommand
import ghidra.program.model.data
import java.lang


class ThreadStateARM(ghidra.app.util.bin.format.macho.threadcommand.ThreadState):
    """
    Represents a _STRUCT_ARM_THREAD_STATE structure.
    """

    ARM_DEBUG_STATE: int = 4
    ARM_EXCEPTION_STATE: int = 3
    ARM_THREAD_STATE: int = 1
    ARM_VFP_STATE: int = 2
    THREAD_STATE_NONE: int = 5
    cpsr: int
    lr: int
    pc: int
    r0: int
    r1: int
    r10: int
    r11: int
    r12: int
    r2: int
    r3: int
    r4: int
    r5: int
    r6: int
    r7: int
    r8: int
    r9: int
    sp: int



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
