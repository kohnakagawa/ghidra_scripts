from typing import List
import ghidra.app.plugin.processors.generic
import ghidra.program.model.mem
import ghidra.program.model.pcode
import java.io
import java.lang
import java.util


class Operand(object, java.io.Serializable):




    def __init__(self, n: unicode, o: ghidra.app.plugin.processors.generic.OperandValue, off: ghidra.app.plugin.processors.generic.Offset): ...



    def dynamic(self) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getAllHandles(self, __a0: java.util.ArrayList, __a1: ghidra.app.plugin.processors.generic.Position, __a2: int) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getHandle(self) -> ghidra.app.plugin.processors.generic.Handle:
        """
        Returns previously computed handle for this operand.  Should not
         be called before the full version of getHandle, where Position and and
         offset are specified.
        @return Handle
        """
        ...

    @overload
    def getHandle(self, position: ghidra.app.plugin.processors.generic.Position, off: int) -> ghidra.app.plugin.processors.generic.Handle:
        """
        Returns a handle for this operand *without* generating any pcode
        @param position
        @param off
        @return
        @throws Exception
        """
        ...

    @overload
    def getHandle(self, __a0: java.util.ArrayList, __a1: ghidra.app.plugin.processors.generic.Position, __a2: int) -> ghidra.app.plugin.processors.generic.Handle: ...

    def getInfo(self, buf: ghidra.program.model.mem.MemBuffer, off: int) -> ghidra.app.plugin.processors.generic.ConstructorInfo: ...

    def getPcode(self, position: ghidra.app.plugin.processors.generic.Position) -> List[ghidra.program.model.pcode.PcodeOp]:
        """
        Method getPcode
        @param position
        @return array of pcode ops for this operand
        @throws Exception
        """
        ...

    def getSize(self) -> int:
        """
        @return
        """
        ...

    def hashCode(self) -> int: ...

    def length(self, buf: ghidra.program.model.mem.MemBuffer, off: int) -> int: ...

    def linkRelativeOffsets(self, opHash: java.util.Hashtable) -> None: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

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
    def handle(self) -> ghidra.app.plugin.processors.generic.Handle: ...

    @property
    def size(self) -> int: ...
