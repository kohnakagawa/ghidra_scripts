import ghidra.program.database.map
import ghidra.program.model.address
import ghidra.program.model.util
import ghidra.util.prop
import java.lang


class PropertyMapDB(object, ghidra.program.model.util.PropertyMap):
    """
    Abstract class which defines a map containing properties over a set of addresses.
     The map is stored within a database table.
    """









    def applyValue(self, __a0: ghidra.util.prop.PropertyVisitor, __a1: ghidra.program.model.address.Address) -> None: ...

    def delete(self) -> None:
        """
        Delete this property map and all underlying tables.
         This method should be overidden if any table other than the
         default propertyTable is used.
        @throws IOException
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    def getAddressKeyIterator(self, start: ghidra.program.model.address.Address, before: bool) -> ghidra.program.database.map.AddressKeyIterator:
        """
        Get an iterator over the long address keys which contain a property value.
        @param start
        @param before true if the iterator should be positioned before the start address
        @return long address iterator.
        @throws IOException
        """
        ...

    @overload
    def getAddressKeyIterator(self, set: ghidra.program.model.address.AddressSetView, atStart: bool) -> ghidra.program.database.map.AddressKeyIterator:
        """
        Get an iterator over the long address keys which contain a property value.
        @param set
        @param atStart true if the iterator should be positioned at the start
         of the range
        @return long address iterator.
        @throws IOException
        """
        ...

    @overload
    def getAddressKeyIterator(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, atStart: bool) -> ghidra.program.database.map.AddressKeyIterator:
        """
        Get an iterator over the long address keys which contain a property value.
        @param start
        @param end
        @param atStart true if the iterator should be positioned at the start
         of the range
        @return long address iterator.
        @throws IOException
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFirstPropertyAddress(self) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.util.PropertyMap#getFirstPropertyAddress()
        """
        ...

    def getLastPropertyAddress(self) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.util.PropertyMap#getLastPropertyAddress()
        """
        ...

    def getName(self) -> unicode:
        """
        @see ghidra.program.model.util.PropertyMap#getName()
        """
        ...

    def getNextPropertyAddress(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.util.PropertyMap#getNextPropertyAddress(ghidra.program.model.address.Address)
        """
        ...

    def getObject(self, __a0: ghidra.program.model.address.Address) -> object: ...

    def getPreviousPropertyAddress(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.util.PropertyMap#getPreviousPropertyAddress(ghidra.program.model.address.Address)
        """
        ...

    @overload
    def getPropertyIterator(self) -> ghidra.program.model.address.AddressIterator:
        """
        @see ghidra.program.model.util.PropertyMap#getPropertyIterator()
        """
        ...

    @overload
    def getPropertyIterator(self, asv: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressIterator:
        """
        @see ghidra.program.model.util.PropertyMap#getPropertyIterator(ghidra.program.model.address.AddressSetView)
        """
        ...

    @overload
    def getPropertyIterator(self, start: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.address.AddressIterator:
        """
        @see ghidra.program.model.util.PropertyMap#getPropertyIterator(ghidra.program.model.address.Address, boolean)
        """
        ...

    @overload
    def getPropertyIterator(self, asv: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.address.AddressIterator:
        """
        @see ghidra.program.model.util.PropertyMap#getPropertyIterator(ghidra.program.model.address.AddressSetView, boolean)
        """
        ...

    @overload
    def getPropertyIterator(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressIterator:
        """
        @see ghidra.program.model.util.PropertyMap#getPropertyIterator(ghidra.program.model.address.Address, ghidra.program.model.address.Address)
        """
        ...

    @overload
    def getPropertyIterator(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.address.AddressIterator:
        """
        @see ghidra.program.model.util.PropertyMap#getPropertyIterator(ghidra.program.model.address.Address, ghidra.program.model.address.Address, boolean)
        """
        ...

    def getSize(self) -> int:
        """
        @see ghidra.program.model.util.PropertyMap#getSize()
        """
        ...

    @staticmethod
    def getTableName(propertyName: unicode) -> unicode: ...

    def hasProperty(self, addr: ghidra.program.model.address.Address) -> bool:
        """
        @see ghidra.program.model.util.PropertyMap#hasProperty(ghidra.program.model.address.Address)
        """
        ...

    def hashCode(self) -> int: ...

    @overload
    def intersects(self, set: ghidra.program.model.address.AddressSetView) -> bool:
        """
        @see ghidra.program.model.util.PropertyMap#intersects(ghidra.program.model.address.AddressSetView)
        """
        ...

    @overload
    def intersects(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address) -> bool:
        """
        @see ghidra.program.model.util.PropertyMap#intersects(ghidra.program.model.address.Address, ghidra.program.model.address.Address)
        """
        ...

    def invalidateCache(self) -> None:
        """
        Invalidates the cache.
        """
        ...

    def moveRange(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, newStart: ghidra.program.model.address.Address) -> None:
        """
        @see ghidra.program.model.util.PropertyMap#moveRange(ghidra.program.model.address.Address, ghidra.program.model.address.Address, ghidra.program.model.address.Address)
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, addr: ghidra.program.model.address.Address) -> bool:
        """
        @see ghidra.program.model.util.PropertyMap#remove(ghidra.program.model.address.Address)
        """
        ...

    def removeRange(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address) -> bool:
        """
        @see ghidra.program.model.util.PropertyMap#removeRange(ghidra.program.model.address.Address, ghidra.program.model.address.Address)
        """
        ...

    def setCacheSize(self, size: int) -> None:
        """
        Adjust the size of the underlying read cache.
        @param size the size of the cache.
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
    def cacheSize(self) -> None: ...  # No getter available.

    @cacheSize.setter
    def cacheSize(self, value: int) -> None: ...

    @property
    def firstPropertyAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def lastPropertyAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def name(self) -> unicode: ...

    @property
    def propertyIterator(self) -> ghidra.program.model.address.AddressIterator: ...

    @property
    def size(self) -> int: ...
