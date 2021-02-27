import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.pcode
import ghidra.xml
import java.lang


class MappedEntry(ghidra.program.model.pcode.SymbolEntry):
    """
    A normal mapping of a HighSymbol to a particular Address, consuming a set number of bytes
    """





    @overload
    def __init__(self, sym: ghidra.program.model.pcode.HighSymbol):
        """
        For use with restoreXML
        @param sym is the owning symbol
        """
        ...

    @overload
    def __init__(self, sym: ghidra.program.model.pcode.HighSymbol, store: ghidra.program.model.listing.VariableStorage, addr: ghidra.program.model.address.Address):
        """
        Construct given a symbol, storage, and first-use Address
        @param sym is the given symbol
        @param store is the given storage
        @param addr is the first-use Address (or null)
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

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
    def readOnly(self) -> bool: ...

    @property
    def size(self) -> int: ...

    @property
    def storage(self) -> ghidra.program.model.listing.VariableStorage: ...

    @property
    def volatile(self) -> bool: ...
