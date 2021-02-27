from typing import List
import ghidra.app.plugin.core.compositeeditor
import java.lang


class EditorActionListener(object):








    def actionsAdded(self, __a0: List[ghidra.app.plugin.core.compositeeditor.CompositeEditorTableAction]) -> None: ...

    def actionsRemoved(self, __a0: List[ghidra.app.plugin.core.compositeeditor.CompositeEditorTableAction]) -> None: ...

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
