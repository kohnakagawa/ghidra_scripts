import db
import java.lang


class QueryRecordIterator(object, db.RecordIterator):
    """
    Iterator that only returns records from another iterator that match the given query.
    """





    @overload
    def __init__(self, iter: db.RecordIterator, query: ghidra.program.database.util.Query):
        """
        Constructs a new QueryRecordIterator that filters the given record iterator with
         the given Query.
        @param iter the record iterator to filter.
        @param query the query used to filter.
        """
        ...

    @overload
    def __init__(self, iter: db.RecordIterator, query: ghidra.program.database.util.Query, forward: bool):
        """
        Constructor
        @param iter record iterator
        @param query query needed to match the record
        @param forward true means iterate in the forward direction
        """
        ...



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
