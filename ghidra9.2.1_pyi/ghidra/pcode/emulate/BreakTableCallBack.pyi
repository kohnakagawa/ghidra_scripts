import ghidra.pcode.emulate
import ghidra.pcode.pcoderaw
import ghidra.program.model.address
import java.lang


class BreakTableCallBack(ghidra.pcode.emulate.BreakTable):
    DEFAULT_NAME: unicode = u'*'



    def __init__(self, language: ghidra.app.plugin.processors.sleigh.SleighLanguage): ...



    def doAddressBreak(self, addr: ghidra.program.model.address.Address) -> bool: ...

    def doPcodeOpBreak(self, curop: ghidra.pcode.pcoderaw.PcodeOpRaw) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def registerAddressCallback(self, addr: ghidra.program.model.address.Address, func: ghidra.pcode.emulate.BreakCallBack) -> None: ...

    def registerPcodeCallback(self, name: unicode, func: ghidra.pcode.emulate.BreakCallBack) -> None: ...

    def setEmulate(self, emu: ghidra.pcode.emulate.Emulate) -> None: ...

    def toString(self) -> unicode: ...

    def unregisterAddressCallback(self, addr: ghidra.program.model.address.Address) -> None: ...

    def unregisterPcodeCallback(self, name: unicode) -> None: ...

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