import ghidra.program.database.mem
import java.lang


class MemoryMapDBAdapterV3(ghidra.program.database.mem.MemoryMapDBAdapter):
    """
    MemoryMap adapter for version 3.
     This version introduces the concept of sub memory blocks and FileBytes
    """

    SUB_BLOCK_TABLE_NAME: unicode = u'Sub Memory Blocks'
    TABLE_NAME: unicode = u'Memory Blocks'
    V3_COMMENTS_COL: int = 1
    V3_LENGTH_COL: int = 5
    V3_NAME_COL: int = 0
    V3_PERMISSIONS_COL: int = 3
    V3_SEGMENT_COL: int = 6
    V3_SOURCE_COL: int = 2
    V3_START_ADDR_COL: int = 4
    V3_SUB_INT_DATA1_COL: int = 4
    V3_SUB_LENGTH_COL: int = 2
    V3_SUB_LONG_DATA2_COL: int = 5
    V3_SUB_PARENT_ID_COL: int = 0
    V3_SUB_START_OFFSET_COL: int = 3
    V3_SUB_TYPE_BIT_MAPPED: int = 0
    V3_SUB_TYPE_BUFFER: int = 2
    V3_SUB_TYPE_BYTE_MAPPED: int = 1
    V3_SUB_TYPE_COL: int = 1
    V3_SUB_TYPE_FILE_BYTES: int = 4
    V3_SUB_TYPE_UNITIALIZED: int = 3
    V3_VERSION: int = 3



    def __init__(self, handle: db.DBHandle, memMap: ghidra.program.database.mem.MemoryMapDB, maxSubBlockSize: long, create: bool): ...



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
