import db
import ghidra.program.database.data
import java.lang


class CompositeDBAdapterV1(ghidra.program.database.data.CompositeDBAdapter, db.RecordTranslator):
    """
    Version 1 implementation for accessing the Composite database table.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    def translateRecord(self, oldRec: db.Record) -> db.Record: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
