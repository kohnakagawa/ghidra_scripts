import ghidra.app.plugin.processors.generic
import ghidra.program.model.mem
import java.io
import java.lang
import java.util


class OperandValue(java.io.Serializable, object):








    def equals(self, __a0: object) -> bool: ...

    def getAllHandles(self, __a0: java.util.ArrayList, __a1: ghidra.app.plugin.processors.generic.Position, __a2: int) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getHandle(self, position: ghidra.app.plugin.processors.generic.Position, off: int) -> ghidra.app.plugin.processors.generic.Handle:
        """
        @param position
        @param off
        @return Handle
        """
        ...

    @overload
    def getHandle(self, __a0: java.util.ArrayList, __a1: ghidra.app.plugin.processors.generic.Position, __a2: int) -> ghidra.app.plugin.processors.generic.Handle: ...

    def getInfo(self, buf: ghidra.program.model.mem.MemBuffer, offset: int) -> ghidra.app.plugin.processors.generic.ConstructorInfo: ...

    def getSize(self) -> int:
        """
        Get the size in bits of the value used in the instruction to create this value.
        """
        ...

    def hashCode(self) -> int: ...

    def length(self, buf: ghidra.program.model.mem.MemBuffer, offset: int) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toList(self, __a0: java.util.ArrayList, __a1: ghidra.app.plugin.processors.generic.Position, __a2: int) -> None: ...

    def toString(self, buf: ghidra.program.model.mem.MemBuffer, offset: int) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def size(self) -> int: ...
