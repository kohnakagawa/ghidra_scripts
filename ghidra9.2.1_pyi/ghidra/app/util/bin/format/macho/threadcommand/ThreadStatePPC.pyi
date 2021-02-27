import ghidra.app.util.bin.format.macho.threadcommand
import ghidra.program.model.data
import java.lang


class ThreadStatePPC(ghidra.app.util.bin.format.macho.threadcommand.ThreadState):
    PPC_EXCEPTION_STATE: int = 3
    PPC_EXCEPTION_STATE64: int = 6
    PPC_FLOAT_STATE: int = 2
    PPC_THREAD_STATE: int = 1
    PPC_THREAD_STATE64: int = 5
    PPC_VECTOR_STATE: int = 4
    THREAD_STATE_NONE: int = 7
    cr: int
    ctr: long
    lr: long
    mq: long
    r0: long
    r1: long
    r10: long
    r11: long
    r12: long
    r13: long
    r14: long
    r15: long
    r16: long
    r17: long
    r18: long
    r19: long
    r2: long
    r20: long
    r21: long
    r22: long
    r23: long
    r24: long
    r25: long
    r26: long
    r27: long
    r28: long
    r29: long
    r3: long
    r30: long
    r31: long
    r4: long
    r5: long
    r6: long
    r7: long
    r8: long
    r9: long
    srr0: long
    srr1: long
    vrsave: long
    xer: long



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
