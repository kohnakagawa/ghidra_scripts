from typing import List
import db
import db.util
import ghidra.feature.vt.api.db
import java.lang


class VTAssociationTableDBAdapter(object):





    class AssociationTableDescriptor(db.util.TableDescriptor):
        APPLIED_STATUS_COL: db.util.TableColumn
        DESTINATION_ADDRESS_COL: db.util.TableColumn
        INSTANCE: ghidra.feature.vt.api.db.VTAssociationTableDBAdapter.AssociationTableDescriptor
        SOURCE_ADDRESS_COL: db.util.TableColumn
        STATUS_COL: db.util.TableColumn
        TYPE_COL: db.util.TableColumn
        VOTE_COUNT_COL: db.util.TableColumn



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
    def createAdapter(__a0: db.DBHandle) -> ghidra.feature.vt.api.db.VTAssociationTableDBAdapter: ...

    def equals(self, __a0: object) -> bool: ...

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
