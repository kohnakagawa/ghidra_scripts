import java.awt.datatransfer
import java.lang


class ClipboardType(object):
    """
    Defines a "type" for items in the Clipboard
    """





    def __init__(self, flavor: java.awt.datatransfer.DataFlavor, typeName: unicode):
        """
        Constructs a new ClipboardType
        @param flavor the DataFlavor of the data in the clipboard
        @param typeName the name for this ClipboardType
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFlavor(self) -> java.awt.datatransfer.DataFlavor:
        """
        Returns the DataFlavor for this ClipboardType
        """
        ...

    def getTypeName(self) -> unicode:
        """
        Returns the name of this Clipboard  Type.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode:
        """
        @see java.lang.Object#toString()
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def flavor(self) -> java.awt.datatransfer.DataFlavor: ...

    @property
    def typeName(self) -> unicode: ...
