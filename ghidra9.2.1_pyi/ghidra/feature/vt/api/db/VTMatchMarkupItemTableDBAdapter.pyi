from typing import List
import db
import db.util
import ghidra.feature.vt.api.db
import ghidra.feature.vt.api.impl
import ghidra.util.task
import java.lang


class VTMatchMarkupItemTableDBAdapter(object):





    class MarkupTableDescriptor(db.util.TableDescriptor):
        ADDRESS_SOURCE_COL: db.util.TableColumn
        ASSOCIATION_KEY_COL: db.util.TableColumn
        DESTINATION_ADDRESS_COL: db.util.TableColumn
        INSTANCE: ghidra.feature.vt.api.db.VTMatchMarkupItemTableDBAdapter.MarkupTableDescriptor
        MARKUP_TYPE_COL: db.util.TableColumn
        ORIGINAL_DESTINATION_VALUE_COL: db.util.TableColumn
        SOURCE_ADDRESS_COL: db.util.TableColumn
        SOURCE_VALUE_COL: db.util.TableColumn
        STATUS_COL: db.util.TableColumn
        STATUS_DESCRIPTION_COL: db.util.TableColumn



        def __init__(self): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getColumnClasses(self) -> List[java.lang.Class]: ...

        def getColumnNames(self) -> List[unicode]: ...

        def getIndexedColumns(self) -> List[int]: ...

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



    def __init__(self): ...



    @staticmethod
    def createAdapter(__a0: db.DBHandle) -> ghidra.feature.vt.api.db.VTMatchMarkupItemTableDBAdapter: ...

    def createMarkupItemRecord(self, __a0: ghidra.feature.vt.api.impl.MarkupItemStorage) -> db.Record: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getAdapter(__a0: db.DBHandle, __a1: db.OpenMode, __a2: ghidra.util.task.TaskMonitor) -> ghidra.feature.vt.api.db.VTMatchMarkupItemTableDBAdapter: ...

    def getClass(self) -> java.lang.Class: ...

    def getRecord(self, __a0: long) -> db.Record: ...

    def getRecordCount(self) -> int: ...

    @overload
    def getRecords(self) -> db.RecordIterator: ...

    @overload
    def getRecords(self, __a0: long) -> db.RecordIterator: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeMatchMarkupItemRecord(self, __a0: long) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def recordCount(self) -> int: ...

    @property
    def records(self) -> db.RecordIterator: ...
