import ghidra.program.model.pcode
import java.lang


class SequenceRange(object):




    def __init__(self, start: ghidra.program.model.pcode.SequenceNumber, end: ghidra.program.model.pcode.SequenceNumber): ...



    def contains(self, seq: ghidra.program.model.pcode.SequenceNumber) -> bool: ...

    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEnd(self) -> ghidra.program.model.pcode.SequenceNumber: ...

    def getStart(self) -> ghidra.program.model.pcode.SequenceNumber: ...

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

    @property
    def end(self) -> ghidra.program.model.pcode.SequenceNumber: ...

    @property
    def start(self) -> ghidra.program.model.pcode.SequenceNumber: ...