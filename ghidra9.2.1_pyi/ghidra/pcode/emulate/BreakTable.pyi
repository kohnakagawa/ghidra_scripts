import ghidra.pcode.emulate
import ghidra.pcode.pcoderaw
import ghidra.program.model.address
import java.lang


class BreakTable(object):




    def __init__(self): ...



    def doAddressBreak(self, addr: ghidra.program.model.address.Address) -> bool: ...

    def doPcodeOpBreak(self, curop: ghidra.pcode.pcoderaw.PcodeOpRaw) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setEmulate(self, emu: ghidra.pcode.emulate.Emulate) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def emulate(self) -> None: ...  # No getter available.

    @emulate.setter
    def emulate(self, value: ghidra.pcode.emulate.Emulate) -> None: ...
