from typing import List
import ghidra.framework.model
import java.lang


class DomainObjectDBTransaction(object, ghidra.framework.model.Transaction):
    """
    DomainObjectDBTransaction represents an atomic undoable operation performed
     on a single domain object.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def getID(self) -> long: ...

    def getOpenSubTransactions(self) -> List[unicode]: ...

    def getStatus(self) -> int: ...

    def hasCommittedDBTransaction(self) -> bool:
        """
        Returns true if this fully committed transaction has a corresponding
         database transaction/checkpoint.
        """
        ...

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
