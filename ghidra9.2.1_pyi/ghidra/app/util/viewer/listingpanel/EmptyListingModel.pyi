import docking.widgets.fieldpanel
import ghidra.app.util.viewer.format
import ghidra.app.util.viewer.listingpanel
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class EmptyListingModel(object, ghidra.app.util.viewer.listingpanel.ListingModel):
    DISPLAY_EXTERNAL_FUNCTION_POINTER_OPTION_NAME: unicode = u'Function Pointers.Display External Function Pointer Header'
    DISPLAY_NONEXTERNAL_FUNCTION_POINTER_OPTION_NAME: unicode = u'Function Pointers.Display Non-External Function Pointer Header'
    FUNCTION_POINTER_OPTION_GROUP_NAME: unicode = u'Function Pointers'



    def __init__(self): ...



    def addListener(self, listener: ghidra.app.util.viewer.listingpanel.ListingModelListener) -> None: ...

    def adjustAddressSetToCodeUnitBoundaries(self, addressSet: ghidra.program.model.address.AddressSet) -> ghidra.program.model.address.AddressSet: ...

    @overload
    def closeAllData(self, addresses: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    @overload
    def closeAllData(self, data: ghidra.program.model.listing.Data, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def closeData(self, data: ghidra.program.model.listing.Data) -> None: ...

    def copy(self) -> ghidra.app.util.viewer.listingpanel.ListingModel: ...

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

    def isOpen(self, object: ghidra.program.model.listing.Data) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def openAllData(self, addresses: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    @overload
    def openAllData(self, data: ghidra.program.model.listing.Data, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def openData(self, data: ghidra.program.model.listing.Data) -> bool: ...

    def removeListener(self, listener: ghidra.app.util.viewer.listingpanel.ListingModelListener) -> None: ...

    def setFormatManager(self, formatManager: ghidra.app.util.viewer.format.FormatManager) -> None: ...

    def toString(self) -> unicode: ...

    def toggleOpen(self, object: ghidra.program.model.listing.Data) -> None: ...

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
