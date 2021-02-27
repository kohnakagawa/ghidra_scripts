import db
import ghidra.program.database.util
import java.lang


class StringMatchQuery(object, ghidra.program.database.util.Query):
    """
    Query for matching string fields with wildcard string.
    """





    def __init__(self, col: int, searchString: unicode, caseSensitive: bool):
        """
        Construct a new StringMatchQuery
        @param col column index
        @param searchString string to match
        @param caseSensitive true if the match should be case sensitive
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def matches(self, record: db.Record) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
