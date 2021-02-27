from typing import List
import ghidra.app.plugin.core.datamgr
import ghidra.app.plugin.core.datamgr.archive
import ghidra.program.model.data
import java.lang


class DataTypeSynchronizer(object):




    def __init__(self, __a0: ghidra.app.plugin.core.datamgr.archive.DataTypeManagerHandler, __a1: ghidra.program.model.data.DataTypeManager, __a2: ghidra.program.model.data.SourceArchive): ...



    def closeTransactions(self) -> None: ...

    @overload
    @staticmethod
    def commit(__a0: ghidra.app.plugin.core.datamgr.archive.DataTypeManagerHandler, __a1: ghidra.program.model.data.DataType) -> bool: ...

    @overload
    @staticmethod
    def commit(__a0: ghidra.program.model.data.DataTypeManager, __a1: ghidra.program.model.data.DataType) -> None: ...

    @staticmethod
    def commitAssumingTransactionsOpen(__a0: ghidra.program.model.data.DataTypeManager, __a1: ghidra.program.model.data.DataType) -> None: ...

    @staticmethod
    def disassociate(__a0: ghidra.program.model.data.DataType) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def findAssociatedDataTypes(self) -> List[object]: ...

    def findOutOfSynchDataTypes(self) -> List[object]: ...

    def getArchiveName(self) -> unicode: ...

    def getClass(self) -> java.lang.Class: ...

    def getClientName(self) -> unicode: ...

    def getClientType(self) -> unicode: ...

    @staticmethod
    def getDiffToolTip(__a0: ghidra.app.plugin.core.datamgr.archive.DataTypeManagerHandler, __a1: ghidra.program.model.data.DataType) -> unicode: ...

    def getSourceName(self) -> unicode: ...

    @staticmethod
    def getSyncStatus(__a0: ghidra.app.plugin.core.datamgr.archive.DataTypeManagerHandler, __a1: ghidra.program.model.data.DataType) -> ghidra.app.plugin.core.datamgr.DataTypeSyncState: ...

    def hashCode(self) -> int: ...

    def markSynchronized(self) -> None: ...

    @staticmethod
    def namesAreEquivalent(__a0: ghidra.program.model.data.DataType, __a1: ghidra.program.model.data.DataType) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def openTransactions(self) -> None: ...

    def reSyncDataTypes(self) -> None: ...

    def reSyncOutOfSyncInTimeOnlyDataTypes(self) -> None: ...

    def removeSourceArchive(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def update(__a0: ghidra.app.plugin.core.datamgr.archive.DataTypeManagerHandler, __a1: ghidra.program.model.data.DataType) -> bool: ...

    @overload
    @staticmethod
    def update(__a0: ghidra.program.model.data.DataTypeManager, __a1: ghidra.program.model.data.DataType) -> None: ...

    @staticmethod
    def updateAssumingTransactionsOpen(__a0: ghidra.program.model.data.DataTypeManager, __a1: ghidra.program.model.data.DataType) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def archiveName(self) -> unicode: ...

    @property
    def clientName(self) -> unicode: ...

    @property
    def clientType(self) -> unicode: ...

    @property
    def sourceName(self) -> unicode: ...
