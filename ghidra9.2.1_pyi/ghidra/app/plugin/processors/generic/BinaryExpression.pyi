import ghidra.app.plugin.processors.generic
import ghidra.program.model.address
import ghidra.program.model.mem
import java.lang
import java.util


class BinaryExpression(object, ghidra.app.plugin.processors.generic.OperandValue, ghidra.app.plugin.processors.generic.ExpressionValue):
    ADD: int = 0
    AND: int = 5
    DIV: int = 3
    EQ: int = 4
    INVALID_OP: int = -1
    MUL: int = 2
    SUB: int = 1



    def __init__(self, op: int, l: ghidra.app.plugin.processors.generic.ExpressionTerm, r: ghidra.app.plugin.processors.generic.ExpressionTerm, c: ghidra.program.model.address.AddressSpace): ...



    def equals(self, __a0: object) -> bool: ...

    def getAllHandles(self, __a0: java.util.ArrayList, __a1: ghidra.app.plugin.processors.generic.Position, __a2: int) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getHandle(self, position: ghidra.app.plugin.processors.generic.Position, off: int) -> ghidra.app.plugin.processors.generic.Handle: ...

    @overload
    def getHandle(self, __a0: java.util.ArrayList, __a1: ghidra.app.plugin.processors.generic.Position, __a2: int) -> ghidra.app.plugin.processors.generic.Handle: ...

    def getInfo(self, buf: ghidra.program.model.mem.MemBuffer, off: int) -> ghidra.app.plugin.processors.generic.ConstructorInfo: ...

    def getSize(self) -> int: ...

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

    def setSpace(self, space: ghidra.program.model.address.AddressSpace) -> None: ...

    def toList(self, __a0: java.util.ArrayList, __a1: ghidra.app.plugin.processors.generic.Position, __a2: int) -> None: ...

    @overload
    def toString(self) -> unicode: ...

    @overload
    def toString(self, buf: ghidra.program.model.mem.MemBuffer, off: int) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def size(self) -> int: ...

    @property
    def space(self) -> None: ...  # No getter available.

    @space.setter
    def space(self, value: ghidra.program.model.address.AddressSpace) -> None: ...
