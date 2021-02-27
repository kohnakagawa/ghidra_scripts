from typing import List
import ghidra.program.model.address
import ghidra.program.model.mem
import java.lang


class MemoryBlockListener(object):
    """
    Methods for a listener that is called when changes are made to a
     MemoryBlock.
    """









    def commentChanged(self, block: ghidra.program.model.mem.MemoryBlock, oldComment: unicode, newComment: unicode) -> None:
        """
        Notification that the block's comment changed.
        @param block affected block
        @param oldComment old comment; may be null
        @param newComment new comment; may be null
        """
        ...

    def dataChanged(self, block: ghidra.program.model.mem.MemoryBlock, addr: ghidra.program.model.address.Address, oldData: List[int], newData: List[int]) -> None:
        """
        Notification that bytes changed in the block.
        @param block affected block
        @param addr starting address of the change
        @param oldData old byte values
        @param newData new byte values
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def executeStatusChanged(self, block: ghidra.program.model.mem.MemoryBlock, isExecute: bool) -> None:
        """
        Notification that the block's execute attribute has changed.
        @param block affected block
        @param isExecute true means the block is marked as executable
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def nameChanged(self, block: ghidra.program.model.mem.MemoryBlock, oldName: unicode, newName: unicode) -> None:
        """
        Notification the name changed.
        @param block affected block
        @param oldName old name
        @param newName new name
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def readStatusChanged(self, block: ghidra.program.model.mem.MemoryBlock, isRead: bool) -> None:
        """
        Notification the block's read attribute has changed.
        @param block affected block
        @param isRead true means the block is marked as readable
        """
        ...

    def sourceChanged(self, block: ghidra.program.model.mem.MemoryBlock, oldSource: unicode, newSource: unicode) -> None:
        """
        Notification that the source of the block has changed.
        @param block affected block
        @param oldSource old source
        @param newSource new source
        """
        ...

    def sourceOffsetChanged(self, block: ghidra.program.model.mem.MemoryBlock, oldOffset: long, newOffset: long) -> None:
        """
        Notification that the source offset has changed.
        @param block affected block
        @param oldOffset old offset
        @param newOffset new offset
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeStatusChanged(self, block: ghidra.program.model.mem.MemoryBlock, isWrite: bool) -> None:
        """
        Notification that the block's write attribute has changed.
        @param block affected block
        @param isWrite true means the block is marked as writable
        """
        ...
