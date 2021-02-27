import db
import java.lang


class EmptyRecordIterator(object, db.RecordIterator):
    """
    Implementation of a RecordIterator that is always empty.
    """





    def __init__(self): ...



    def delete(self) -> bool:
        """
        @see db.RecordIterator#delete()
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool:
        """
        @see db.RecordIterator#hasNext()
        """
        ...

    def hasPrevious(self) -> bool:
        """
        @see db.RecordIterator#hasPrevious()
        """
        ...

    def hashCode(self) -> int: ...

    def next(self) -> db.Record:
        """
        @see db.RecordIterator#next()
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def previous(self) -> db.Record:
        """
        @see db.RecordIterator#previous()
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
