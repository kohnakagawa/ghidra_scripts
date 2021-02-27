import ghidra.framework.model
import java.lang


class Undoable(object):
    """
    Objects that implement Undoable have the ability to "remember" some number
     of stable states that are created as operations are performed upon them.  The
     object then provides methods for "undoing" to a previous state or "redoing" to
     a later state.
    """









    def addTransactionListener(self, listener: ghidra.framework.model.TransactionListener) -> None:
        """
        Adds the given transaction listener to this domain object
        @param listener the new transaction listener to add
        """
        ...

    def canRedo(self) -> bool:
        """
        Returns true if there is a later state to "redo" to.
        """
        ...

    def canUndo(self) -> bool:
        """
        Returns true if there is a previous state to "undo" to.
        """
        ...

    def clearUndo(self) -> None:
        """
        Clear all undoable/redoable transactions
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getRedoName(self) -> unicode:
        """
        Returns a description of the change that would be "redone".
        """
        ...

    def getUndoName(self) -> unicode:
        """
        Returns a description of the chanage that would be "undone".
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def redo(self) -> None:
        """
        Returns to a latter state that exists because of an undo.  Normally, this
         will cause the current state to appear on the "undo" stack.  This method
         will do nothing if there are no latter states to "redo".
        @throws IOException if an IO error occurs
        """
        ...

    def removeTransactionListener(self, listener: ghidra.framework.model.TransactionListener) -> None:
        """
        Removes the given transaction listener from this domain object.
        @param listener the transaction listener to remove
        """
        ...

    def toString(self) -> unicode: ...

    def undo(self) -> None:
        """
        Returns to the previous state.  Normally, this will cause the current state
         to appear on the "redo" stack.  This method will do nothing if there are
         no previous states to "undo".
        @throws IOException if an IO error occurs
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def redoName(self) -> unicode: ...

    @property
    def undoName(self) -> unicode: ...
