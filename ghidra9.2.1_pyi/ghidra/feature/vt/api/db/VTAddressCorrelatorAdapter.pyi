from typing import List
import db
import db.util
import ghidra.feature.vt.api.db
import ghidra.util.task
import java.lang


class VTAddressCorrelatorAdapter(object):





    class AddressCorrelationTableDescriptor(db.util.TableDescriptor):
        DESTINATION_ADDRESS_COL: db.util.TableColumn
        INSTANCE: ghidra.feature.vt.api.db.VTAddressCorrelatorAdapter.AddressCorrelationTableDescriptor
        SOURCE_ADDRESS_COL: db.util.TableColumn
        SOURCE_ENTRY_COL: db.util.TableColumn



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







    @staticmethod
    def createAdapter(__a0: db.DBHandle) -> ghidra.feature.vt.api.db.VTAddressCorrelatorAdapter: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getAdapter(__a0: db.DBHandle, __a1: ghidra.util.task.TaskMonitor) -> ghidra.feature.vt.api.db.VTAddressCorrelatorAdapter: ...

    def getClass(self) -> java.lang.Class: ...

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
