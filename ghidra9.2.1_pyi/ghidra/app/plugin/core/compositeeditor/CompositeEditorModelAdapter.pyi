import ghidra.app.plugin.core.compositeeditor
import java.lang


class CompositeEditorModelAdapter(object, ghidra.app.plugin.core.compositeeditor.CompositeEditorModelListener):
    COMPOSITE_LOADED: int = 3
    COMPOSITE_MODIFIED: int = 1
    COMPOSITE_UNMODIFIED: int = 2
    EDIT_ENDED: int = 6
    EDIT_STARTED: int = 5
    NO_COMPOSITE_LOADED: int = 4



    def __init__(self): ...



    def componentDataChanged(self) -> None: ...

    def compositeEditStateChanged(self, __a0: int) -> None: ...

    def compositeInfoChanged(self) -> None: ...

    def endFieldEditing(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def selectionChanged(self) -> None: ...

    def showUndefinedStateChanged(self, __a0: bool) -> None: ...

    def statusChanged(self, __a0: unicode, __a1: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
