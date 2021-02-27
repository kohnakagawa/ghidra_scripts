import ghidra.app.plugin.core.compositeeditor
import java.lang


class EditorAction(ghidra.app.plugin.core.compositeeditor.CompositeEditorModelListener, object):
    BASIC_ACTION_GROUP: unicode = u'1_BASIC_EDITOR_ACTION'
    BITFIELD_ACTION_GROUP: unicode = u'4_COMPONENT_EDITOR_ACTION'
    COMPONENT_ACTION_GROUP: unicode = u'3_COMPONENT_EDITOR_ACTION'
    COMPOSITE_LOADED: int = 3
    COMPOSITE_MODIFIED: int = 1
    COMPOSITE_UNMODIFIED: int = 2
    DATA_ACTION_GROUP: unicode = u'2_DATA_EDITOR_ACTION'
    EDIT_ENDED: int = 6
    EDIT_STARTED: int = 5
    NO_COMPOSITE_LOADED: int = 4







    def adjustEnablement(self) -> None: ...

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
