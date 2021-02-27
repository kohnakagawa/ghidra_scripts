import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.pcode
import ghidra.xml
import java.lang


class MappedDataEntry(ghidra.program.model.pcode.MappedEntry):
    """
    A normal address based HighSymbol mapping with an associated Data object
    """





    @overload
    def __init__(self, sym: ghidra.program.model.pcode.HighSymbol):
        """
        Constructor for use with restoreXML
        @param sym is the owning HighSymbol
        """
        ...

    @overload
    def __init__(self, sym: ghidra.program.model.pcode.HighSymbol, store: ghidra.program.model.listing.VariableStorage, d: ghidra.program.model.listing.Data):
        """
        Construct given a symbol, storage, and a backing Data object
        @param sym the given symbol
        @param store the given storage
        @param d the backing Data object
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getData(self) -> ghidra.program.model.listing.Data:
        """
        @return the backing Data object
        """
        ...

    def getPCAdress(self) -> ghidra.program.model.address.Address:
        """
        The storage used to hold this Symbol may be used for other purposes at different points in
         the code.  This returns the earliest address in the code where this storage is used for this symbol
        @return the starting address where the Symbol uses this storage
        """
        ...

    def getSize(self) -> int: ...

    def getStorage(self) -> ghidra.program.model.listing.VariableStorage: ...

    def hashCode(self) -> int: ...

    def isReadOnly(self) -> bool: ...

    def isVolatile(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreXML(self, parser: ghidra.xml.XmlPullParser) -> None: ...

    def saveXml(self, buf: java.lang.StringBuilder) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def data(self) -> ghidra.program.model.listing.Data: ...

    @property
    def readOnly(self) -> bool: ...

    @property
    def volatile(self) -> bool: ...
