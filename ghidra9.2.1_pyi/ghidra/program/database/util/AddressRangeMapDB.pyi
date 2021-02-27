import db
import ghidra.program.model.address
import ghidra.util.task
import java.lang


class AddressRangeMapDB(object, db.DBListener):
    """
    RangeMapDB provides a generic value range map backed by a database table.
     A given range may be occupied by at most a single value which is painted over
     that range.
    """

    RANGE_MAP_TABLE_PREFIX: unicode = u'Range Map - '



    def __init__(self, dbHandle: db.DBHandle, addrMap: ghidra.program.database.map.AddressMap, lock: ghidra.util.Lock, name: unicode, errHandler: db.util.ErrorHandler, valueFieldClass: java.lang.Class, indexed: bool):
        """
        Construct a generic range map.
        @param dbHandle database handle.
        @param name map name used in naming the underlying database table.
         This name must be unique across all range maps.
        @param errHandler database error handler.
        @param valueFieldClass Field class to be used for stored values.
        @param indexed if true, values will be indexed allowing use of the
         getValueRangeIterator method.
        """
        ...



    def clearRange(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address) -> None:
        """
        Remove values from the given range.
        @param startAddr the start address.
        @param endAddr the end address.
        """
        ...

    def dbClosed(self, dbh: db.DBHandle) -> None: ...

    def dbRestored(self, dbh: db.DBHandle) -> None: ...

    def dispose(self) -> None:
        """
        Deletes the database table used to store this range map.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def exists(dbHandle: db.DBHandle, name: unicode) -> bool: ...

    def getAddressRangeContaining(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressRange:
        """
        Returns the bounding address-range containing addr and the the same value throughout.
        @param addr the contained address
        @return single value address-range containing addr
        """
        ...

    @overload
    def getAddressRanges(self) -> ghidra.program.model.address.AddressRangeIterator:
        """
        Returns an address range iterator over all occupied ranges in the map.
        @return AddressRangeIterator that iterates over all occupied ranges in th
         map.
        """
        ...

    @overload
    def getAddressRanges(self, startAddr: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressRangeIterator:
        """
        Returns an address range iterator over all occupied ranges in the map.
         The first range must have a FROM address at or after
         the specified startAddr.
        @param startAddr the address to start the iterator.
        @return AddressRangeIterator that iterates over all occupied ranges in th
         map.
        """
        ...

    @overload
    def getAddressRanges(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressRangeIterator:
        """
        Returns an address range iterator over all occupied ranges whose
         FROM address falls within the range startAddr to endAddr.
        @param startAddr start of range
        @param endAddr end of range
        @return AddressRangeIterator
        """
        ...

    @overload
    def getAddressSet(self) -> ghidra.program.model.address.AddressSet:
        """
        Returns a complete address set where any value has been set.
        @return address set
        """
        ...

    @overload
    def getAddressSet(self, value: db.Field) -> ghidra.program.model.address.AddressSet:
        """
        Returns a complete address set where the specified value has been set.
        @param value field value
        @return address set
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getRecordCount(self) -> int:
        """
        Returns the number of records contained within this map.
         NOTE: This number will be greater or equal to the number of
         address ranges contained within the map.
        @return record count
        """
        ...

    def getValue(self, addr: ghidra.program.model.address.Address) -> db.Field:
        """
        Returns the value associated with the given address.
        @param addr the address of the value
        @return value or null no value exists
        """
        ...

    def getValueRanges(self, value: db.Field) -> ghidra.program.model.address.AddressRangeIterator:
        """
        Returns an address range iterator for those ranges which contain the
         specified value.  This method may only be invoked for indexed maps.
        @param value
        @return AddressRangeIterator
        """
        ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool:
        """
        Returns true if this map is empty
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

    def paintRange(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address, value: db.Field) -> None:
        """
        Associates the given value with every index from start to end (inclusive)
         Any previous associates are overwritten.
        @param startAddr the start address.
        @param endAddr the end address.
        @param value value to be painted, or null for value removal.
        """
        ...

    def setName(self, newName: unicode) -> bool:
        """
        Set the name associated with this range map.
        @param newName
        @return true if successful, else false
        @throws DuplicateNameException
        """
        ...

    def tableAdded(self, dbh: db.DBHandle, table: db.Table) -> None: ...

    def tableDeleted(self, dbh: db.DBHandle, table: db.Table) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addressRanges(self) -> ghidra.program.model.address.AddressRangeIterator: ...

    @property
    def addressSet(self) -> ghidra.program.model.address.AddressSet: ...

    @property
    def empty(self) -> bool: ...

    @property
    def name(self) -> None: ...  # No getter available.

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def recordCount(self) -> int: ...
