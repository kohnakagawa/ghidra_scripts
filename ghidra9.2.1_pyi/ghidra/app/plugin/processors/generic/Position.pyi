import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.mem
import java.lang


class Position(object):
    """
    To change this generated comment edit the template variable "typecomment":

     To enable and disable the creation of type comments go to

    """





    def __init__(self, b: ghidra.program.model.mem.MemBuffer, start: ghidra.program.model.address.Address, next: ghidra.program.model.address.Address, c: ghidra.program.model.lang.ProcessorContext): ...



    def buffer(self) -> ghidra.program.model.mem.MemBuffer: ...

    def context(self) -> ghidra.program.model.lang.ProcessorContext: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def nextAddr(self) -> ghidra.program.model.address.Address: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def startAddr(self) -> ghidra.program.model.address.Address: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
