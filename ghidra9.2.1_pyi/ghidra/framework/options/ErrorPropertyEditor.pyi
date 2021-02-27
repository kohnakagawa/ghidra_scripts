from typing import List
import java.awt
import java.beans
import java.lang
import javax.swing


class ErrorPropertyEditor(java.beans.PropertyEditorSupport):




    def __init__(self, errorMessage: unicode, value: object): ...



    def addPropertyChangeListener(self, __a0: java.beans.PropertyChangeListener) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def firePropertyChange(self) -> None: ...

    def getAsText(self) -> unicode: ...

    def getClass(self) -> java.lang.Class: ...

    def getCustomEditor(self) -> javax.swing.JComponent: ...

    def getJavaInitializationString(self) -> unicode: ...

    def getSource(self) -> object: ...

    def getTags(self) -> List[unicode]: ...

    def getValue(self) -> object: ...

    def hashCode(self) -> int: ...

    def isPaintable(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def paintValue(self, __a0: java.awt.Graphics, __a1: java.awt.Rectangle) -> None: ...

    def removePropertyChangeListener(self, __a0: java.beans.PropertyChangeListener) -> None: ...

    def setAsText(self, __a0: unicode) -> None: ...

    def setSource(self, __a0: object) -> None: ...

    def setValue(self, __a0: object) -> None: ...

    def supportsCustomEditor(self) -> bool: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def customEditor(self) -> javax.swing.JComponent: ...
