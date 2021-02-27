import db
import ghidra.program.model.address
import java.lang


class DBKeyAdapter(object):
    """
    Adapter to get an iterator over keys in a table.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getKeys(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> db.DBLongIterator:
        """
        Get an iterator over the keys in the given range.
        @param start start of range
        @param end end of range (inclusive)
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
