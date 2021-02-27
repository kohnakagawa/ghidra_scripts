from typing import List
import ghidra.app.plugin.core.datamgr
import java.lang


class DataTypeSyncState(java.lang.Enum):
    COMMIT: ghidra.app.plugin.core.datamgr.DataTypeSyncState = COMMIT
    CONFLICT: ghidra.app.plugin.core.datamgr.DataTypeSyncState = CONFLICT
    IN_SYNC: ghidra.app.plugin.core.datamgr.DataTypeSyncState = IN_SYNC
    ORPHAN: ghidra.app.plugin.core.datamgr.DataTypeSyncState = ORPHAN
    UNKNOWN: ghidra.app.plugin.core.datamgr.DataTypeSyncState = UNKNOWN
    UPDATE: ghidra.app.plugin.core.datamgr.DataTypeSyncState = UPDATE







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.app.plugin.core.datamgr.DataTypeSyncState: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.plugin.core.datamgr.DataTypeSyncState]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
