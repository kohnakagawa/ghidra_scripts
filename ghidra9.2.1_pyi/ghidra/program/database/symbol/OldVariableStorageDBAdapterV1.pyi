import db
import ghidra.program.database.symbol
import ghidra.util.task
import java.lang


class OldVariableStorageDBAdapterV1(ghidra.program.database.symbol.OldVariableStorageDBAdapter):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @staticmethod
    def upgrade(dbHandle: db.DBHandle, oldAdapter: ghidra.program.database.symbol.OldVariableStorageDBAdapter, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.database.symbol.OldVariableStorageDBAdapter: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
