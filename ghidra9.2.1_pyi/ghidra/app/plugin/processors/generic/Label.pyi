import ghidra.app.plugin.processors.generic
import ghidra.program.model.mem
import java.lang


class Label(object, ghidra.app.plugin.processors.generic.ExpressionValue):
    """
    To change this generated comment edit the template variable "typecomment":

     To enable and disable the creation of type comments go to

    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def length(self, buf: ghidra.program.model.mem.MemBuffer, off: int) -> int: ...

    def longValue(self, buf: ghidra.program.model.mem.MemBuffer, off: int) -> long: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
