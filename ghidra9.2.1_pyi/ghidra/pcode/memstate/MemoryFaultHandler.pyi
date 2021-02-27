from typing import List
import ghidra.program.model.address
import java.lang


class MemoryFaultHandler(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    def uninitializedRead(self, address: ghidra.program.model.address.Address, size: int, buf: List[int], bufOffset: int) -> bool:
        """
        An attempt has been made to read uninitialized memory at the
         specified address.
        @param address uninitialized storage address (memory, register or unique)
        @param size number of uninitialized bytes
        @param buf storage buffer
        @param bufOffset read offset within buffer
        @return true if data should be treated as initialized
        """
        ...

    def unknownAddress(self, address: ghidra.program.model.address.Address, write: bool) -> bool:
        """
        Unable to translate the specified address
        @param address address which failed to be translated
        @param write true if memory operation was a write vs. read
        @return true if fault was handled
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
