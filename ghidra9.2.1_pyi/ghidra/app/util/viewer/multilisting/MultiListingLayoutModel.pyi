import ghidra.app.util.viewer.format
import ghidra.app.util.viewer.listingpanel
import ghidra.app.util.viewer.multilisting
import ghidra.program.model.address
import java.lang


class MultiListingLayoutModel(object, ghidra.app.util.viewer.listingpanel.ListingModelListener, ghidra.app.util.viewer.format.FormatModelListener):
    """
    Class for creating multiple coordinated ListingModels for multiple programs.
    """





    def __init__(self, formatMgr: ghidra.app.util.viewer.format.FormatManager, programs: List[ghidra.program.model.listing.Program], primaryAddrSet: ghidra.program.model.address.AddressSetView):
        """
        Constructs a new MultiListingLayoutModel.
        @param formatMgr the FormatManager used to layout the fields.
        @param programs the list of programs that will be coordinated using listing models.
         The first program in the array will be used as the primary program.
        @param primaryAddrSet the addressSet to use for the view.
         This is compatible with the primary program, which is program[0].
        """
        ...



    def dataChanged(self, updateImmediately: bool) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def formatModelAdded(self, model: ghidra.app.util.viewer.format.FieldFormatModel) -> None:
        """
        @see ghidra.app.util.viewer.format.FormatModelListener#formatModelAdded(ghidra.app.util.viewer.format.FieldFormatModel)
        """
        ...

    def formatModelChanged(self, model: ghidra.app.util.viewer.format.FieldFormatModel) -> None:
        """
        @see ghidra.app.util.viewer.format.FormatModelListener#formatModelChanged(ghidra.app.util.viewer.format.FieldFormatModel)
        """
        ...

    def formatModelRemoved(self, model: ghidra.app.util.viewer.format.FieldFormatModel) -> None:
        """
        @see ghidra.app.util.viewer.format.FormatModelListener#formatModelRemoved(ghidra.app.util.viewer.format.FieldFormatModel)
        """
        ...

    def getAlignedModel(self, index: int) -> ghidra.app.util.viewer.listingpanel.ListingModel:
        """
        Returns the the ListingLayoutModel for the i'th program.
        @param index the index of program for which to return a listing model
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getModel(self, index: int) -> ghidra.app.util.viewer.listingpanel.ListingModel:
        """
        Returns the ListingModel for the program with the indicated index.
        @param index the index indicating which program's model to get.
        @return the program's ListingModel.
        """
        ...

    def hashCode(self) -> int: ...

    def modelSizeChanged(self) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setAddressSet(self, view: ghidra.program.model.address.AddressSetView) -> None:
        """
        Sets the address set for this MultiListingLayoutModel
        @param view the current address set, which must be compatible with the
         primary program and listingModel
        """
        ...

    def setAddressTranslator(self, translator: ghidra.app.util.viewer.multilisting.AddressTranslator) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addressSet(self) -> None: ...  # No getter available.

    @addressSet.setter
    def addressSet(self, value: ghidra.program.model.address.AddressSetView) -> None: ...

    @property
    def addressTranslator(self) -> None: ...  # No getter available.

    @addressTranslator.setter
    def addressTranslator(self, value: ghidra.app.util.viewer.multilisting.AddressTranslator) -> None: ...
