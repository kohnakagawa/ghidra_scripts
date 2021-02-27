import ghidra.app.decompiler.component
import java.lang


class DualDecompileResultsListener(object):








    def decompileResultsSet(self, leftDecompileData: ghidra.app.decompiler.component.DecompileData, rightDecompileData: ghidra.app.decompiler.component.DecompileData) -> None: ...

    def equals(self, __a0: object) -> bool: ...

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
