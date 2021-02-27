from typing import List
import docking.widgets.fieldpanel.support
import ghidra.app.util
import java.lang


class ByteViewerHighlightProvider(object, ghidra.app.util.HighlightProvider):
    EMPTY_HIGHLIGHT: List[docking.widgets.fieldpanel.support.Highlight] = array(docking.widgets.fieldpanel.support.Highlight)



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getHighlights(self, __a0: unicode, __a1: object, __a2: java.lang.Class, __a3: int) -> List[docking.widgets.fieldpanel.support.Highlight]: ...

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
