import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.util
import ghidra.util.task
import java.lang


class RegisterValueStore(object):
    """
    This is a generalized class for storing register values over ranges.  The values include mask bits
     to indicate which bits within the register are being set.  The mask is stored along with the
     value so the getValue method can indicate back which bits in the value are valid.  If existing
     values already exist at an address, the values are combined according to the masks.  Any new value
     bits that have their associated mask bits on will overwrite any existing bits and the new mask will
     be anded to the existing mask.  Other bits will not be affected.

     This class takes a RangeMapAdapter that will adapt to some lower level storage.  There are current
     two implementations - one that uses an ObjectRangeMap for storing register values in memory and
     the other that uses RangeMapDB for storing register values in the database.
    """





    def __init__(self, register: ghidra.program.model.lang.Register, rangeMap: ghidra.program.util.RangeMapAdapter, enableRangeWriteCache: bool):
        """
        Constructs a new RegisterValueStore.
        @param rangeMap the rangeMapAdapter that handles the low level storage of byte arrays
        """
        ...



    def clearAll(self) -> None:
        """
        Delete all stored values and free/delete underlying storage.
        """
        ...

    def clearValue(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, register: ghidra.program.model.lang.Register) -> None:
        """
        Clears the address range of any set bits using the mask from the given register value.
         existing values in the range that have values that are not part of the input mask are
         not changed. If register is null, just clear all the values in range
        @param start the start of the range to clear the register value bits.
        @param end the end of the range(inclusive) to clear the register value bits.
        @param register the register whos mask to use.  If null, clear all values in the given range.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    def getAddressRangeIterator(self) -> ghidra.program.model.address.AddressRangeIterator:
        """
        Returns an AddressRangeIterator that will return address ranges everywhere that register
         values have been set.
        @return an AddressRangeIterator that will return address ranges everywhere that register
         values have been set.
        """
        ...

    @overload
    def getAddressRangeIterator(self, startAddress: ghidra.program.model.address.Address, endAddress: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressRangeIterator:
        """
        Returns an AddressRangeIterator that will return address ranges everywhere that register values
         have been set within the given range.
        @param startAddress the start address to get stored register values.
        @param endAddress the end address to get stored register values.
        @return an AddressRangeIterator that will return address ranges everywhere that register
         values have been set within the given range.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getValue(self, register: ghidra.program.model.lang.Register, address: ghidra.program.model.address.Address) -> ghidra.program.model.lang.RegisterValue:
        """
        Returns the RegisterValue (value and mask) associated with the given address.
        @param address the address at which to get the RegisterValue.
        @return the RegisterValue
        """
        ...

    def getValueRangeContaining(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressRange:
        """
        Returns the bounding address-range containing addr and the the same value throughout.
         This range will be limited by any value change associated with the base register.
        @param addr the contained address
        @return single value address-range containing addr
        """
        ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool:
        """
        Returns true if this store has no associated values for any address.
        @return true if this store has no associated values for any address.
        """
        ...

    def moveAddressRange(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, length: long, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Move all register values within an address range to a new range.
        @param fromAddr the first address of the range to be moved.
        @param toAddr the address where to the range is to be moved.
        @param length the number of addresses to move.
        @param monitor the task monitor.
        @throws CancelledException if the user canceled the operation via the task monitor.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setLanguage(self, translator: ghidra.program.util.LanguageTranslator, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Preserve register values and handle register name/size change.
        @param translator
        @param monitor
        @return true if translated successfully, false if register not mapped
         value storage should be discarded.
        @throws CancelledException
        """
        ...

    def setValue(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, newValue: ghidra.program.model.lang.RegisterValue) -> None:
        """
        Sets the given register value (contains value and mask) across the given address range.  Any
         existing values in the range that have values that are not part of the input mask are
         not changed.
        @param start the start of the range to set the register value.
        @param end the end of the range(inclusive) to set the register value.
        @param newValue the new register value to set.
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
