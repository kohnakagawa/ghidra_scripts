import ghidra.app.plugin.processors.generic
import ghidra.program.model.address
import ghidra.program.model.mem
import java.io
import java.lang
import java.util


class ExpressionTerm(object, java.io.Serializable):




    def __init__(self, v: ghidra.app.plugin.processors.generic.ExpressionValue, off: ghidra.app.plugin.processors.generic.Offset): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getValue(self) -> ghidra.app.plugin.processors.generic.ExpressionValue: ...

    def hashCode(self) -> int: ...

    def length(self, buf: ghidra.program.model.mem.MemBuffer, off: int) -> int: ...

    def linkRelativeOffsets(self, opHash: java.util.Hashtable) -> None:
        """
        Method linkRelativeOffsets.
        @param opHash
        """
        ...

    def longValue(self, buf: ghidra.program.model.mem.MemBuffer, off: int) -> long: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setSpace(self, space: ghidra.program.model.address.AddressSpace) -> None:
        """
        Sets the address space of the expression value
        @param space the address space to set
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def space(self) -> None: ...  # No getter available.

    @space.setter
    def space(self, value: ghidra.program.model.address.AddressSpace) -> None: ...

    @property
    def value(self) -> ghidra.app.plugin.processors.generic.ExpressionValue: ...
