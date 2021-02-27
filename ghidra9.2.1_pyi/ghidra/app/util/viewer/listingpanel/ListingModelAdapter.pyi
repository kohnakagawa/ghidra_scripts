import docking.widgets.fieldpanel
import docking.widgets.fieldpanel.field
import docking.widgets.fieldpanel.listener
import docking.widgets.fieldpanel.support
import ghidra.app.util.viewer.listingpanel
import ghidra.app.util.viewer.util
import ghidra.program.model.address
import ghidra.program.util
import java.awt
import java.lang


class ListingModelAdapter(object, docking.widgets.fieldpanel.LayoutModel, ghidra.app.util.viewer.listingpanel.ListingModelListener):




    def __init__(self, bigListingModel: ghidra.app.util.viewer.listingpanel.ListingModel): ...



    def addLayoutModelListener(self, listener: docking.widgets.fieldpanel.listener.LayoutModelListener) -> None: ...

    def dataChanged(self, updateImmediately: bool) -> None: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def flushChanges(self) -> None: ...

    def getAddressIndexMap(self) -> ghidra.app.util.viewer.util.AddressIndexMap: ...

    def getAllProgramSelection(self) -> ghidra.program.util.ProgramSelection: ...

    def getClass(self) -> java.lang.Class: ...

    def getFieldLocation(self, location: ghidra.program.util.ProgramLocation) -> docking.widgets.fieldpanel.support.FieldLocation:
        """
        Translates the given ProgramLocation into a FieldLocation.  Attempts to find a
         field that can exactly find a match for the program location.  Otherwise, it
         will return a fieldLocation to the default field or beginning of the line.
        @param location the ProgramLocation to translate.
        @return a FieldLocation for the ProgramLocation or null if none can be found.
        """
        ...

    def getFieldSelection(self, selection: ghidra.program.util.ProgramSelection) -> docking.widgets.fieldpanel.support.FieldSelection: ...

    def getIndexAfter(self, index: long) -> long: ...

    def getIndexBefore(self, index: long) -> long: ...

    @overload
    def getLayout(self, addr: ghidra.program.model.address.Address) -> docking.widgets.fieldpanel.Layout: ...

    @overload
    def getLayout(self, index: long) -> docking.widgets.fieldpanel.Layout: ...

    def getNumIndexes(self) -> long: ...

    def getPreferredViewSize(self) -> java.awt.Dimension: ...

    @overload
    def getProgramLocation(self, floc: docking.widgets.fieldpanel.support.FieldLocation) -> ghidra.program.util.ProgramLocation: ...

    @overload
    def getProgramLocation(self, location: docking.widgets.fieldpanel.support.FieldLocation, field: docking.widgets.fieldpanel.field.Field) -> ghidra.program.util.ProgramLocation: ...

    def getProgramSelection(self, selection: docking.widgets.fieldpanel.support.FieldSelection) -> ghidra.program.util.ProgramSelection: ...

    def hashCode(self) -> int: ...

    def isUniform(self) -> bool: ...

    @overload
    def iterator(self) -> docking.widgets.fieldpanel.LayoutModelIterator: ...

    @overload
    def iterator(self, __a0: long) -> docking.widgets.fieldpanel.LayoutModelIterator: ...

    def modelSizeChanged(self) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeLayoutModelListener(self, listener: docking.widgets.fieldpanel.listener.LayoutModelListener) -> None: ...

    def setAddressSet(self, view: ghidra.program.model.address.AddressSetView) -> None:
        """
        Sets the addresses displayed by this model's listing.
        @param view the addresses. These must already be compatible with the program
         associated with this model.
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
    def addressIndexMap(self) -> ghidra.app.util.viewer.util.AddressIndexMap: ...

    @property
    def addressSet(self) -> None: ...  # No getter available.

    @addressSet.setter
    def addressSet(self, value: ghidra.program.model.address.AddressSetView) -> None: ...

    @property
    def allProgramSelection(self) -> ghidra.program.util.ProgramSelection: ...

    @property
    def numIndexes(self) -> long: ...

    @property
    def preferredViewSize(self) -> java.awt.Dimension: ...

    @property
    def uniform(self) -> bool: ...
