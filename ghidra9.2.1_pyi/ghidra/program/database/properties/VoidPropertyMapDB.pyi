import ghidra.program.database.map
import ghidra.program.database.properties
import ghidra.program.model.address
import ghidra.program.model.util
import ghidra.util.prop
import java.lang


class VoidPropertyMapDB(ghidra.program.database.properties.PropertyMapDB, ghidra.program.model.util.VoidPropertyMap):
    """
    Property manager that deals with properties that are of
     "void" type, which is a marker for whether a property exists.
     Records contain only a address key are stored within the underlying database table.
    """





    def __init__(self, dbHandle: db.DBHandle, openMode: int, errHandler: db.util.ErrorHandler, changeMgr: ghidra.program.util.ChangeManager, addrMap: ghidra.program.database.map.AddressMap, name: unicode, monitor: ghidra.util.task.TaskMonitor):
        """
        Construct an void object property map.
        @param dbHandle database handle.
        @param openMode the mode that the program was openned in.
        @param errHandler database error handler.
        @param changeMgr change manager for event notification
        @param addrMap address map.
        @param name property name.
        @param monitor progress monitor that is only used when upgrading
        @throws VersionException if the database version is not the expected version.
        @throws CancelledException if the user cancels the upgrade operation.
        @throws IOException if a database io error occurs.
        """
        ...



    def add(self, addr: ghidra.program.model.address.Address) -> None:
        """
        @see ghidra.program.model.util.VoidPropertyMap#add(ghidra.program.model.address.Address)
        """
        ...

    def applyValue(self, visitor: ghidra.util.prop.PropertyVisitor, addr: ghidra.program.model.address.Address) -> None:
        """
        @see ghidra.program.model.util.PropertyMap#applyValue(ghidra.util.prop.PropertyVisitor, ghidra.program.model.address.Address)
        """
        ...

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

    def getObject(self, addr: ghidra.program.model.address.Address) -> object:
        """
        @see ghidra.program.model.util.PropertyMap#getObject(ghidra.program.model.address.Address)
        """
        ...

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
