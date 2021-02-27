from typing import List
import java.lang


class Transaction(object):
    ABORTED: int = 2
    COMMITTED: int = 1
    NOT_DONE: int = 0
    NOT_DONE_BUT_ABORTED: int = 3







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode:
        """
        Returns the description of this transaction.
        @return the description of this transaction
        """
        ...

    def getID(self) -> long: ...

    def getOpenSubTransactions(self) -> List[unicode]:
        """
        Returns the list of open sub-transactions that are contained
         inside this transaction.
        @return the list of open sub-transactions
        """
        ...

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

    @property
    def ID(self) -> long: ...

    @property
    def description(self) -> unicode: ...

    @property
    def openSubTransactions(self) -> java.util.ArrayList: ...

    @property
    def status(self) -> int: ...
