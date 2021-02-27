import ghidra.app.decompiler
import ghidra.app.plugin.core.decompile.actions
import java.awt
import java.lang


class SliceHighlightColorProvider(object, ghidra.app.plugin.core.decompile.actions.TokenHighlightColorProvider):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getColor(self, __a0: ghidra.app.decompiler.ClangToken) -> java.awt.Color: ...

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
