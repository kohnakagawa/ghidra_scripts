import db
import ghidra.program.database.util
import java.lang


class OrQuery(object, ghidra.program.database.util.Query):
    """
    Combines two queries such that this query is the logical "OR" of the two queries.  If the
     first query matches, then the second query is not executed.
    """





    def __init__(self, q1: ghidra.program.database.util.Query, q2: ghidra.program.database.util.Query):
        """
        Construct a new OrQuery from two other queries.
        @param q1 the first query
        @param q2 the second query
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
