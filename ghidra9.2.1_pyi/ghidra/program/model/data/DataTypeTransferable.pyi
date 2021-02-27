from typing import List
import java.awt.datatransfer
import java.lang


class DataTypeTransferable(object, java.awt.datatransfer.Transferable, java.awt.datatransfer.ClipboardOwner):
    """
    Defines data that is available for drag/drop and clipboard transfers.
     The data is a DataType object.
    """

    localBuiltinDataTypeFlavor: java.awt.datatransfer.DataFlavor = docking.dnd.GenericDataFlavor[mimetype=application/x-java-jvm-local-objectref;representationclass=ghidra.program.model.data.DataTypeImpl]
    localDataTypeFlavor: java.awt.datatransfer.DataFlavor = docking.dnd.GenericDataFlavor[mimetype=application/x-java-jvm-local-objectref;representationclass=ghidra.program.model.data.DataTypeImpl]



    def __init__(self, dt: ghidra.program.model.data.DataType):
        """
        Constructor
        @param dt the dataType being transfered
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

    def lostOwnership(self, clipboard: java.awt.datatransfer.Clipboard, contents: java.awt.datatransfer.Transferable) -> None:
        """
        ClipboardOwner interface method.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode:
        """
        Get the string representation for this transferable.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def transferDataFlavors(self) -> List[java.awt.datatransfer.DataFlavor]: ...
