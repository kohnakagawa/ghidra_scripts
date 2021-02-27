import db
import ghidra.program.database.util
import java.lang


class NotQuery(object, ghidra.program.database.util.Query):
    """
    Negates the given query such that this query is the logical "NOT" of the given query.
    """





    def __init__(self, q1: ghidra.program.database.util.Query):
        """
        Construct a new query that results in the not of the given query.
        @param q1 the query to logically negate.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def matches(self, record: db.Record) -> bool:
        """
        @see ghidra.program.database.util.Query#matches(db.Record)
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
