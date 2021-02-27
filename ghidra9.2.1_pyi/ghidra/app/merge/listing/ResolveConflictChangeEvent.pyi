import java.lang
import javax.swing.event


class ResolveConflictChangeEvent(javax.swing.event.ChangeEvent):
    """
    Event that gets passed to a listener to indicate that a user changed
     one of the choices in the row of a table that is part of the
     VerticalChoicesPanel or VariousChoicesPanel.
    """





    def __init__(self, __a0: object): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getSource(self) -> object: ...

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
