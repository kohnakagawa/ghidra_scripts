import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class Ext4GroupDescriptor(object, ghidra.app.util.bin.StructConverter):
    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    @overload
    def __init__(self, __a0: ghidra.app.util.bin.BinaryReader, __a1: bool): ...

    @overload
    def __init__(self, __a0: ghidra.app.util.bin.ByteProvider, __a1: bool): ...



    def equals(self, __a0: object) -> bool: ...

    def getBg_block_bitmap_csum_hi(self) -> int: ...

    def getBg_block_bitmap_csum_lo(self) -> int: ...

    def getBg_block_bitmap_hi(self) -> int: ...

    def getBg_block_bitmap_lo(self) -> int: ...

    def getBg_checksum(self) -> int: ...

    def getBg_exclude_bitmap_hi(self) -> int: ...

    def getBg_exclude_bitmap_lo(self) -> int: ...

    def getBg_flags(self) -> int: ...

    def getBg_free_blocks_count_hi(self) -> int: ...

    def getBg_free_blocks_count_lo(self) -> int: ...

    def getBg_free_inodes_count_hi(self) -> int: ...

    def getBg_free_inodes_count_lo(self) -> int: ...

    def getBg_inode_bitmap_csum_hi(self) -> int: ...

    def getBg_inode_bitmap_csum_lo(self) -> int: ...

    def getBg_inode_bitmap_hi(self) -> int: ...

    def getBg_inode_bitmap_lo(self) -> int: ...

    def getBg_inode_table_hi(self) -> int: ...

    def getBg_inode_table_lo(self) -> int: ...

    def getBg_itable_unused_hi(self) -> int: ...

    def getBg_itable_unused_lo(self) -> int: ...

    def getBg_reserved(self) -> int: ...

    def getBg_used_dirs_count_hi(self) -> int: ...

    def getBg_used_dirs_count_lo(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def bg_block_bitmap_csum_hi(self) -> int: ...

    @property
    def bg_block_bitmap_csum_lo(self) -> int: ...

    @property
    def bg_block_bitmap_hi(self) -> int: ...

    @property
    def bg_block_bitmap_lo(self) -> int: ...

    @property
    def bg_checksum(self) -> int: ...

    @property
    def bg_exclude_bitmap_hi(self) -> int: ...

    @property
    def bg_exclude_bitmap_lo(self) -> int: ...

    @property
    def bg_flags(self) -> int: ...

    @property
    def bg_free_blocks_count_hi(self) -> int: ...

    @property
    def bg_free_blocks_count_lo(self) -> int: ...

    @property
    def bg_free_inodes_count_hi(self) -> int: ...

    @property
    def bg_free_inodes_count_lo(self) -> int: ...

    @property
    def bg_inode_bitmap_csum_hi(self) -> int: ...

    @property
    def bg_inode_bitmap_csum_lo(self) -> int: ...

    @property
    def bg_inode_bitmap_hi(self) -> int: ...

    @property
    def bg_inode_bitmap_lo(self) -> int: ...

    @property
    def bg_inode_table_hi(self) -> int: ...

    @property
    def bg_inode_table_lo(self) -> int: ...

    @property
    def bg_itable_unused_hi(self) -> int: ...

    @property
    def bg_itable_unused_lo(self) -> int: ...

    @property
    def bg_reserved(self) -> int: ...

    @property
    def bg_used_dirs_count_hi(self) -> int: ...

    @property
    def bg_used_dirs_count_lo(self) -> int: ...