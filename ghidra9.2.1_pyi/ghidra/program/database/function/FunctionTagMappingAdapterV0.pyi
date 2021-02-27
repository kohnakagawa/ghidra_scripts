import db
import ghidra.program.database.function
import java.lang


class FunctionTagMappingAdapterV0(ghidra.program.database.function.FunctionTagMappingAdapter, db.DBListener):
    """
    Initial version of the FunctionTagMappingAdapter.
    """









    def dbClosed(self, dbh: db.DBHandle) -> None: ...

    def dbRestored(self, dbh: db.DBHandle) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def tableAdded(self, dbh: db.DBHandle, table: db.Table) -> None: ...

    def tableDeleted(self, dbh: db.DBHandle, table: db.Table) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
