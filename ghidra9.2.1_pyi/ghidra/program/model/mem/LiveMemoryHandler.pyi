from typing import List
import ghidra.program.model.address
import ghidra.program.model.mem
import java.lang


class LiveMemoryHandler(object):
    """
    Live memory handler interface.
    """









    def addLiveMemoryListener(self, listener: ghidra.program.model.mem.LiveMemoryListener) -> None:
        """
        Adds a LiveMemoryListener to this handler.  The listener will be notified when memory
         bytes change.
        @param listener the listener to be notified of memory byte value changes.
        """
        ...

    def clearCache(self) -> None:
        """
        Called when the memory map is re-initializing. Usually after an undo or redo.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getByte(self, addr: ghidra.program.model.address.Address) -> int:
        """
        Gets the byte at the given address.
        @param addr the address of the byte to be retrieved
        @return the byte at the given address.
        @throws MemoryAccessException if the byte can't be read.
        """
        ...

    def getBytes(self, address: ghidra.program.model.address.Address, buffer: List[int], startIndex: int, size: int) -> int:
        """
        Get the bytes at the given address and size and put them into the destination buffer.
        @param address the address of the first byte to be retrieved.
        @param buffer the byte buffer in which to place the bytes.
        @param startIndex the starting index in the buffer to put the first byte.
        @param size the number of bytes to retrieve and put in the buffer.
        @return the number of bytes placed into the given buffer.
        @throws MemoryAccessException if the bytes can't be read.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def putByte(self, address: ghidra.program.model.address.Address, value: int) -> None:
        """
        Writes the given byte value to the address in memory.
        @param address the address whose byte is to be updated to the new value.
        @param value the value to set at the given address.
        @throws MemoryAccessException if the value can not be written to the memory.
        """
        ...

    def putBytes(self, address: ghidra.program.model.address.Address, source: List[int], startIndex: int, size: int) -> int:
        """
        Writes the given bytes to memory starting at the given address.
        @param address the address in memory to write the bytes.
        @param source the buffer containing the byte values to be written to memory.
        @param startIndex the starting index in the buffer to get byte values.
        @param size the number of bytes to write to memory.
        @return the number of bytes written to memory.
        @throws MemoryAccessException if the bytes can't be written to memory.
        """
        ...

    def removeLiveMemoryListener(self, listener: ghidra.program.model.mem.LiveMemoryListener) -> None:
        """
        Removes the LiveMemoryListener from this handler.
        @param listener the listener to be removed.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
