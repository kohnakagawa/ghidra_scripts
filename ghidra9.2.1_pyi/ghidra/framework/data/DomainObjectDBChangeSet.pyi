import db
import java.lang


class DomainObjectDBChangeSet(db.DBChangeSet, object):
    """
    DomainObjectDBChangeSet extends DBChangeSet
     providing methods which facilitate transaction synchronization with the domain object's DBHandle.
    """









    @overload
    def clearUndo(self) -> None:
        """
        Clears the undo/redo stack.
        """
        ...

    @overload
    def clearUndo(self, isCheckedOut: bool) -> None:
        """
        Resets the change sets after a save.
        """
        ...

    def endTransaction(self, commit: bool) -> None:
        """
        End change data transaction.
        @param commit if true transaction data is committed,
                       otherwise transaction data is discarded
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def read(self, __a0: db.DBHandle) -> None: ...

    def redo(self) -> None:
        """
        Redo the change data transaction associated the last Undo.
        """
        ...

    def setMaxUndos(self, maxUndos: int) -> None:
        """
        Set the undo/redo stack depth
        @param maxUndos the maximum numbder of undo
        """
        ...

    def startTransaction(self) -> None:
        """
        Start change data transaction.
        """
        ...

    def toString(self) -> unicode: ...

    def undo(self) -> None:
        """
        Undo the last change data transaction
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def write(self, __a0: db.DBHandle, __a1: bool) -> None: ...

    @property
    def maxUndos(self) -> None: ...  # No getter available.

    @maxUndos.setter
    def maxUndos(self, value: int) -> None: ...
