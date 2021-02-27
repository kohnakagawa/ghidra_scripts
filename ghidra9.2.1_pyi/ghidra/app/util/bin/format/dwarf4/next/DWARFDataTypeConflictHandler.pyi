import ghidra.program.model.data
import ghidra.program.model.data.DataTypeConflictHandler
import java.lang


class DWARFDataTypeConflictHandler(ghidra.program.model.data.DataTypeConflictHandler):
    """
    This DataTypeConflictHandler attempts to match
     conflicting Composite (structure or union) when
     they have compatible data layouts. (Data types that are exactly equiv will
     not be subjected to conflict handling and will never reach here)

     A default/empty sized structure, or structures with the same size are
     candidates for matching.

     Structures that have a subset of the other's field definition are candidates
     for matching.

     When a candidate data type is matched with an existing data type, this
     conflict handler will specify that the new data type is:


     discarded and replaced by the existing data type
     (ConflictResult#USE_EXISTING)
     used to overwrite the existing data type
     (ConflictResult#REPLACE_EXISTING)

     or the candidate data type was NOT matched with an existing data type,
     and the new data type is:


     kept, but renamed with a .conflictNNNN suffix to make it unique
     (ConflictResult#RENAME_AND_ADD)

     NOTE: structures with alignment (instead of being statically laid out)
     are not treated specially and will not match other aligned or non-aligned
     structures.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getSubsequentHandler(self) -> ghidra.program.model.data.DataTypeConflictHandler: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def resolveConflict(self, addedDataType: ghidra.program.model.data.DataType, existingDataType: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataTypeConflictHandler.ConflictResult: ...

    def shouldUpdate(self, sourceDataType: ghidra.program.model.data.DataType, localDataType: ghidra.program.model.data.DataType) -> bool: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
