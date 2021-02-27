import db
import java.lang


class DBFieldAdapter(object):
    """
    Interface to get a field adapter where the Field is the primary
     key in the table.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFields(self, start: long, end: long) -> db.DBFieldIterator:
        """
        Get the iterator over the primary key.
        @param start start of iterator
        @param end end of iterator
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
