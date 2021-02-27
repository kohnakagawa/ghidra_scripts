import db
import ghidra.program.database.util
import java.lang


class FieldMatchQuery(object, ghidra.program.database.util.Query):
    """
    Query implementation used to test a field in a record to match a given value.
    """





    def __init__(self, column: int, value: db.Field):
        """
        Constructs a new FieldMatchQuery that tests a records field against a particular value.
        @param column the field index in the record to test.
        @param value the Field value to test the record's field against.
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
