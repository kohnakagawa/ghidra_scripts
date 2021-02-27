from typing import Iterator
import ghidra.program.database
import ghidra.program.model.address
import ghidra.program.model.symbol
import ghidra.util.task
import java.lang


class NamespaceManager(object, ghidra.program.database.ManagerDB):
    """
    Class to manage namespaces.
    """





    def __init__(self, handle: db.DBHandle, errHandler: db.util.ErrorHandler, addrMap: ghidra.program.database.map.AddressMap, openMode: int, lock: ghidra.util.Lock, monitor: ghidra.util.task.TaskMonitor):
        """
        Construct a new namespace manager.
        @param handle the database handle.
        @param errHandler the error handler.
        @param addrMap the address map
        @param openMode the open mode
        @param lock the program synchronization lock
        @param monitor the task monitor.
        @throws VersionException if the table version is different from this adapter.
        """
        ...



    def deleteAddressRange(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddressSet(self, namespace: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.address.AddressSetView:
        """
        Gets the body for the given namespace.
        @param namespace the namespace for which to get its body.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getGlobalNamespace(self) -> ghidra.program.model.symbol.Namespace:
        """
        Get the global namespace.
        """
        ...

    def getNamespaceContaining(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Namespace:
        """
        Get the Namespace containing the given address. If the address is not
         in a defined namespace (e.g., Function), the global namespace is
         returned.
        @param addr the address for which to find a namespace.
        """
        ...

    def getNamespacesOverlapping(self, set: ghidra.program.model.address.AddressSetView) -> Iterator[ghidra.program.model.symbol.Namespace]:
        """
        Get all Namespaces whose body overlaps the specified address set.
        @param set the address for which to find namespace's that intersect it.
        @return a LongField function key iterator.
        """
        ...

    def hashCode(self) -> int: ...

    def invalidateCache(self, all: bool) -> None: ...

    def moveAddressRange(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, length: long, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def overlapsNamespace(self, set: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressRange:
        """
        Checks if an existing namespace's address set intersects with
         the given set. If so, return the first overlapping range.
        @returns null if no overlaps, or an address range of the first overlap
        """
        ...

    def programReady(self, openMode: int, currentRevision: int, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def removeBody(self, namespace: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.address.AddressSetView:
        """
        Removes any associated body with the given namespace.
        @param namespace the namespace whose body is to be cleared.
        """
        ...

    def setBody(self, namespace: ghidra.program.model.symbol.Namespace, set: ghidra.program.model.address.AddressSetView) -> None:
        """
        Sets the body of a namespace.
        @param namespace the namespace whose body is to be modified.
        @param set the address set for the new body.
        """
        ...

    def setProgram(self, program: ghidra.program.database.ProgramDB) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def globalNamespace(self) -> ghidra.program.model.symbol.Namespace: ...

    @property
    def program(self) -> None: ...  # No getter available.

    @program.setter
    def program(self, value: ghidra.program.database.ProgramDB) -> None: ...
