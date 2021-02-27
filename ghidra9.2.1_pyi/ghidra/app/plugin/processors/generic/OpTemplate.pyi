import ghidra.app.plugin.processors.generic
import ghidra.program.model.pcode
import java.io
import java.lang
import java.util


class OpTemplate(object, java.io.Serializable):




    def __init__(self, opc: int, in_: List[ghidra.app.plugin.processors.generic.VarnodeTemplate], out: ghidra.app.plugin.processors.generic.VarnodeTemplate, af: ghidra.program.model.address.AddressFactory): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getPcode(self, handles: java.util.HashMap, position: ghidra.app.plugin.processors.generic.Position, opSequenceNumber: int, off: int) -> ghidra.program.model.pcode.PcodeOp:
        """
        Method getPcode.
        @param handles
        @return PcodeOp
        """
        ...

    def hashCode(self) -> int: ...

    def input(self, i: int) -> ghidra.app.plugin.processors.generic.VarnodeTemplate: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def omit(self) -> bool: ...

    def opcode(self) -> int: ...

    def output(self) -> ghidra.app.plugin.processors.generic.VarnodeTemplate: ...

    def setOmit(self, ref: ghidra.app.plugin.processors.generic.Operand) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
