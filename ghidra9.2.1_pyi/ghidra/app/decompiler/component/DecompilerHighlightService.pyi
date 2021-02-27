import ghidra.app.decompiler.component
import java.lang


class DecompilerHighlightService(object):
    """
    A poorly designed interface that does not correctly allow for modifying highlights
    """









    def clearHighlights(self) -> None:
        """
        Clears the <b>primary</b> highlights in the Decompiler
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLayoutModel(self) -> ghidra.app.decompiler.component.ClangLayoutController:
        """
        Returns the layout model of the Decompiler
        @return the layout model
        """
        ...

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

    @property
    def layoutModel(self) -> ghidra.app.decompiler.component.ClangLayoutController: ...
