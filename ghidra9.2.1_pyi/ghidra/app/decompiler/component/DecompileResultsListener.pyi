import ghidra.app.decompiler.component
import java.lang


class DecompileResultsListener(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setDecompileData(self, decompileData: ghidra.app.decompiler.component.DecompileData) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def decompileData(self) -> None: ...  # No getter available.

    @decompileData.setter
    def decompileData(self, value: ghidra.app.decompiler.component.DecompileData) -> None: ...
