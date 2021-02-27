from typing import List
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.util
import ghidra.util.task
import java.lang


class RangeMapAdapter(object):








    def checkWritableState(self) -> None:
        """
        Verify that adapter is in a writable state (i.e., valid transaction has been started).
        @throws IllegalStateException if not in a writable state
        """
        ...

    def clearAll(self) -> None:
        """
        Clears all values.
        """
        ...

    def clearRange(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> None:
        """
        Clears all associated values in the given range.
        @param start the first address in the range to clear.
        @param end the end address in the range to clear.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    def getAddressRangeIterator(self) -> ghidra.program.model.address.AddressRangeIterator:
        """
        Returns an {@link IndexRangeIterator} over all stored values.
        @return an {@link IndexRangeIterator} over all stored values.
        """
        ...

    @overload
    def getAddressRangeIterator(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressRangeIterator:
        """
        Returns an {@link IndexRangeIterator} over all stored values in the given range.  If the
         given range intersects an actual stored range either at the beginning or end, the iterator
         will return those ranges truncated to fit within the given range.
        @param start the first Address in the range.
        @param end the last Address (inclusive) index in the range.
        @return an {@link IndexRangeIterator} over all stored values.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getValue(self, address: ghidra.program.model.address.Address) -> List[int]:
        """
        Returns the byte array that has been associated with the given index.
        @param address the address at which to retrieve a byte array.
        @return the byte array that has been associated with the given index or null if no such
         association exists.
        """
        ...

    def getValueRangeContaining(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressRange:
        """
        Returns the bounding address-range containing addr and the the same value throughout.
         This range will be limited by any value change associated with the base register.
        @param addr the containing address
        @return single value address-range containing addr
        """
        ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool:
        """
        Returns true if this storage has no associated values for any address
        @return true if this storage has no associated values for any address
        """
        ...

    def moveAddressRange(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, length: long, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Move all values within an address range to a new range.
        @param fromAddr the first address of the range to be moved.
        @param toAddr the address where to the range is to be moved.
        @param length the number of addresses to move.
        @param monitor the task monitor.
        @throws CancelledException if the user canceled the operation via the task monitor.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def set(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, bytes: List[int]) -> None:
        """
        Associates the given byte array with all indexes in the given range.  Any existing values
         will be over written.
        @param start the first address in the range.
        @param end the last Address(inclusive) in the range.
        @param bytes the bytes to associate with the range.
        """
        ...

    def setLanguage(self, translator: ghidra.program.util.LanguageTranslator, mapReg: ghidra.program.model.lang.Register, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Update table name and values to reflect new base register
        @param translator
        @param mapReg
        @param monitor
        @throws CancelledException
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addressRangeIterator(self) -> ghidra.program.model.address.AddressRangeIterator: ...

    @property
    def empty(self) -> bool: ...
