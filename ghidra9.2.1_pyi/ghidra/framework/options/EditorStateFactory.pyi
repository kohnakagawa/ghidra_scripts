import ghidra.framework.options
import java.beans
import java.lang


class EditorStateFactory(object):




    def __init__(self): ...



    def clear(self, options: ghidra.framework.options.Options, name: unicode) -> None: ...

    def clearAll(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEditorState(self, options: ghidra.framework.options.Options, name: unicode, listener: java.beans.PropertyChangeListener) -> ghidra.framework.options.EditorState: ...

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
