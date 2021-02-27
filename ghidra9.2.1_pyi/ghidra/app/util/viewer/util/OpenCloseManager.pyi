from typing import List
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.task
import java.lang
import javax.swing.event


class OpenCloseManager(object):
    """
    Manages the open/close state of structures and arrays at specific addresses.
    """





    def __init__(self): ...



    def addChangeListener(self, l: javax.swing.event.ChangeListener) -> None:
        """
        Adds a change listener to be notified when a location is open or closed.
        @param l the listener to be notified.
        """
        ...

    @overload
    def closeAllData(self, data: ghidra.program.model.listing.Data, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    @overload
    def closeAllData(self, program: ghidra.program.model.listing.Program, addresses: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def closeData(self, data: ghidra.program.model.listing.Data) -> None:
        """
        Marks the given data as open.  This method notifies listeners of changes.
        @param data The data to open.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getOpenIndex(self, address: ghidra.program.model.address.Address, path: List[int]) -> int:
        """
        Returns the index of the component that is open at the given address.
        @param address the address to find the open index.
        @param path the component path.
        """
        ...

    def hashCode(self) -> int: ...

    @overload
    def isOpen(self, address: ghidra.program.model.address.Address) -> bool:
        """
        Tests if the data at the given address is open
        @param address the address to test if open
        """
        ...

    @overload
    def isOpen(self, data: ghidra.program.model.listing.Data) -> bool: ...

    @overload
    def isOpen(self, address: ghidra.program.model.address.Address, path: List[int]) -> bool:
        """
        Test is the data at the given address and component path is open
        @param address the address to test
        @param path the component path to test.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def openAllData(self, data: ghidra.program.model.listing.Data, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    @overload
    def openAllData(self, program: ghidra.program.model.listing.Program, addresses: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def openData(self, data: ghidra.program.model.listing.Data) -> bool:
        """
        Marks the given data as open.  This method notifies listeners of changes.
        @param data The data to open.
        @return true if the data location was opened (false if already open or can't be opened)
        """
        ...

    def removeChangeListener(self, l: javax.swing.event.ChangeListener) -> None:
        """
        Removes the listener.
        @param l the listener to remove.
        """
        ...

    def toString(self) -> unicode: ...

    def toggleOpen(self, data: ghidra.program.model.listing.Data) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
