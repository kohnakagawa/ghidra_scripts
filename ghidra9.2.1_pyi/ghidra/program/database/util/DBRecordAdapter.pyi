import db
import ghidra.program.model.address
import java.lang


class DBRecordAdapter(object):
    """
    Interface to get a record iterator.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getRecords(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, colIndex: int) -> db.RecordIterator:
        """
        Get a record iterator.
        @param start start of iterator
        @param end end of iterator
        @param colIndex index column
        @throws IOException if there was a problem accessing the database
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
