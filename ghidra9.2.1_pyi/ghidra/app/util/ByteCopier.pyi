from typing import List
import java.awt.datatransfer
import java.lang


class ByteCopier(object):
    """
    Base class that can copy bytes into a Transferable object, and paste
     bytes into a program.
    """

    BYTE_STRING_FLAVOR: java.awt.datatransfer.DataFlavor
    BYTE_STRING_NO_SPACES_FLAVOR: java.awt.datatransfer.DataFlavor
    BYTE_STRING_NO_SPACE_TYPE: ghidra.app.util.ClipboardType = Byte String (No Spaces)
    BYTE_STRING_TYPE: ghidra.app.util.ClipboardType = Byte String




    class ByteViewerTransferable(object, java.awt.datatransfer.Transferable):




        @overload
        def __init__(self, __a0: unicode): ...

        @overload
        def __init__(self, __a0: unicode, __a1: unicode): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getTransferData(self, __a0: java.awt.datatransfer.DataFlavor) -> object: ...

        def getTransferDataFlavors(self) -> List[java.awt.datatransfer.DataFlavor]: ...

        def hashCode(self) -> int: ...

        def isDataFlavorSupported(self, __a0: java.awt.datatransfer.DataFlavor) -> bool: ...

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





    @staticmethod
    def createStringTransferable(text: unicode) -> java.awt.datatransfer.Transferable:
        """
        Create a Transferable from the given text.
        @param text text used to create a Transferable
        @return a Transferable
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
