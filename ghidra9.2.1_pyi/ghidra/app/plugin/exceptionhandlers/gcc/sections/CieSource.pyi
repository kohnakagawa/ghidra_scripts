import ghidra.app.plugin.exceptionhandlers.gcc.structures.ehFrame
import ghidra.program.model.address
import java.lang


class CieSource(object):








    def equals(self, __a0: object) -> bool: ...

    def getCie(self, __a0: ghidra.program.model.address.Address) -> ghidra.app.plugin.exceptionhandlers.gcc.structures.ehFrame.Cie: ...

    def getClass(self) -> java.lang.Class: ...

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
