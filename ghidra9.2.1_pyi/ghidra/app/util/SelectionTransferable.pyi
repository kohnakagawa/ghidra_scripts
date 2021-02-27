from typing import List
import java.awt.datatransfer
import java.lang


class SelectionTransferable(object, java.awt.datatransfer.Transferable, java.awt.datatransfer.ClipboardOwner):
    """
    Defines data that is available for drag/drop and clipboard transfers.
     The data is an AddressSetView.
    """

    localProgramSelectionFlavor: java.awt.datatransfer.DataFlavor



    def __init__(self, selectionData: ghidra.app.util.SelectionTransferData):
        """
        Construct a new SelectionTransferable.
        @param selectionData the data indicating the selection for the selection transferable
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getTransferData(self, f: java.awt.datatransfer.DataFlavor) -> object:
        """
        Return the transfer data with the given data flavor.
        """
        ...

    def getTransferDataFlavors(self) -> List[java.awt.datatransfer.DataFlavor]:
        """
        Return all data flavors that this class supports.
        """
        ...

    def hashCode(self) -> int: ...

    def isDataFlavorSupported(self, f: java.awt.datatransfer.DataFlavor) -> bool:
        """
        Return whether the specifed data flavor is supported.
        """
        ...

    def lostOwnership(self, clipboard: java.awt.datatransfer.Clipboard, contents: java.awt.datatransfer.Transferable) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def transferDataFlavors(self) -> List[java.awt.datatransfer.DataFlavor]: ...
