from typing import List
import java.awt.event
import java.beans
import java.lang
import javax.swing


class PageDownSelectionAction(javax.swing.AbstractAction):
    """
    Handles the actions required when the user presses the page down key.
    """





    def __init__(self, eventListener: ghidra.framework.main.logviewer.event.FVEventListener): ...



    def accept(self, __a0: object) -> bool: ...

    def actionPerformed(self, e: java.awt.event.ActionEvent) -> None: ...

    def addPropertyChangeListener(self, __a0: java.beans.PropertyChangeListener) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getKeys(self) -> List[object]: ...

    def getPropertyChangeListeners(self) -> List[java.beans.PropertyChangeListener]: ...

    def getValue(self, __a0: unicode) -> object: ...

    def hashCode(self) -> int: ...

    def isEnabled(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def putValue(self, __a0: unicode, __a1: object) -> None: ...

    def removePropertyChangeListener(self, __a0: java.beans.PropertyChangeListener) -> None: ...

    def setEnabled(self, __a0: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...