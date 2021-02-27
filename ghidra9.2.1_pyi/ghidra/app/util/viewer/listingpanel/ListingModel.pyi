import docking.widgets.fieldpanel
import ghidra.app.util.viewer.format
import ghidra.app.util.viewer.listingpanel
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class ListingModel(object):
    DISPLAY_EXTERNAL_FUNCTION_POINTER_OPTION_NAME: unicode = u'Function Pointers.Display External Function Pointer Header'
    DISPLAY_NONEXTERNAL_FUNCTION_POINTER_OPTION_NAME: unicode = u'Function Pointers.Display Non-External Function Pointer Header'
    FUNCTION_POINTER_OPTION_GROUP_NAME: unicode = u'Function Pointers'







    def addListener(self, listener: ghidra.app.util.viewer.listingpanel.ListingModelListener) -> None: ...

    def adjustAddressSetToCodeUnitBoundaries(self, addressSet: ghidra.program.model.address.AddressSet) -> ghidra.program.model.address.AddressSet: ...

    @overload
    def closeAllData(self, addresses: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Closes all data found within the given addresses.  Each data is fully closed.
        @param addresses the range of addresses to search for data
        @param monitor the task monitor
        """
        ...

    @overload
    def closeAllData(self, data: ghidra.program.model.listing.Data, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Recursively close the given data and its sub-components.
        @param data the data to close
        @param monitor the task monitor
        """
        ...

    def closeData(self, data: ghidra.program.model.listing.Data) -> None:
        """
        Closes the given data, but not any sub-components.
        @param data the data to close
        """
        ...

    def copy(self) -> ghidra.app.util.viewer.listingpanel.ListingModel:
        """
        Makes a copy of this model.
        @return a copy of this model.
        """
        ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddressAfter(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address: ...

    def getAddressBefore(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address: ...

    def getAddressSet(self) -> ghidra.program.model.address.AddressSetView: ...

    def getClass(self) -> java.lang.Class: ...

    def getLayout(self, address: ghidra.program.model.address.Address, isGapAddress: bool) -> docking.widgets.fieldpanel.Layout: ...

    def getMaxWidth(self) -> int: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def hashCode(self) -> int: ...

    def isClosed(self) -> bool: ...

    def isOpen(self, data: ghidra.program.model.listing.Data) -> bool:
        """
        Returns true if the data is open
        @param data the data to check
        @return true if the data is open
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def openAllData(self, addresses: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Opens all data found within the given addresses.  Each data is fully opened.
        @param addresses the range of addresses to search for data
        @param monitor the task monitor
        """
        ...

    @overload
    def openAllData(self, data: ghidra.program.model.listing.Data, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Recursively open the given data and its sub-components.
        @param data the data to open
        @param monitor the task monitor
        """
        ...

    def openData(self, data: ghidra.program.model.listing.Data) -> bool:
        """
        Opens the given data, but not any sub-components.
        @param data the data to open
        @return true if the data was opened (will return false if the data is already open or has no children)
        """
        ...

    def removeListener(self, listener: ghidra.app.util.viewer.listingpanel.ListingModelListener) -> None: ...

    def setFormatManager(self, formatManager: ghidra.app.util.viewer.format.FormatManager) -> None: ...

    def toString(self) -> unicode: ...

    def toggleOpen(self, data: ghidra.program.model.listing.Data) -> None:
        """
        Changes the open state of the given data (open -&gt; closes; closed-&gt; open).
        @param data the data to open
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addressSet(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def closed(self) -> bool: ...

    @property
    def formatManager(self) -> None: ...  # No getter available.

    @formatManager.setter
    def formatManager(self, value: ghidra.app.util.viewer.format.FormatManager) -> None: ...

    @property
    def maxWidth(self) -> int: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...
