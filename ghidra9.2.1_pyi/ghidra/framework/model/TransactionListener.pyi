import ghidra.framework.data
import ghidra.framework.model
import java.lang


class TransactionListener(object):
    """
    An interface for listening to transactions
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    def transactionEnded(self, domainObj: ghidra.framework.data.DomainObjectAdapterDB) -> None:
        """
        Invoked when a transaction is ended.
        @param domainObj the domain object where the transaction was ended
        """
        ...

    def transactionStarted(self, domainObj: ghidra.framework.data.DomainObjectAdapterDB, tx: ghidra.framework.model.Transaction) -> None:
        """
        Invoked when a transaction is started.
        @param domainObj the domain object where the transaction was started
        @param tx the transaction that was started
        """
        ...

    def undoRedoOccurred(self, domainObj: ghidra.framework.data.DomainObjectAdapterDB) -> None:
        """
        Notification that undo or redo has occurred.
        @param domainObj the affected domain object
        """
        ...

    def undoStackChanged(self, domainObj: ghidra.framework.data.DomainObjectAdapterDB) -> None:
        """
        Invoked when the stack of available undo/redo's has changed.
        @param domainObj the affected domain object
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
