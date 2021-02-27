import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.program.model.symbol
import java.lang


class ExternalLocationDB(object, ghidra.program.model.symbol.ExternalLocation):








    def createFunction(self) -> ghidra.program.model.listing.Function: ...

    def equals(self, obj: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.symbol.ExternalLocation#getAddress()
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDataType(self) -> ghidra.program.model.data.DataType:
        """
        @see ghidra.program.model.symbol.ExternalLocation#getDataType()
        """
        ...

    def getExternalSpaceAddress(self) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.symbol.ExternalLocation#getExternalSpaceAddress()
        """
        ...

    def getFunction(self) -> ghidra.program.model.listing.Function: ...

    def getLabel(self) -> unicode:
        """
        @see ghidra.program.model.symbol.ExternalLocation#getLabel()
        """
        ...

    def getLibraryName(self) -> unicode:
        """
        @see ghidra.program.model.symbol.ExternalLocation#getLibraryName()
        """
        ...

    def getOriginalImportedName(self) -> unicode: ...

    def getParentName(self) -> unicode:
        """
        @see ghidra.program.model.symbol.ExternalLocation#getParentName()
        """
        ...

    def getParentNameSpace(self) -> ghidra.program.model.symbol.Namespace:
        """
        @see ghidra.program.model.symbol.ExternalLocation#getParentNameSpace()
        """
        ...

    def getSource(self) -> ghidra.program.model.symbol.SourceType: ...

    def getSymbol(self) -> ghidra.program.model.symbol.Symbol: ...

    def hashCode(self) -> int: ...

    def isEquivalent(self, other: ghidra.program.model.symbol.ExternalLocation) -> bool: ...

    def isFunction(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreOriginalName(self) -> None: ...

    def saveOriginalNameIfNeeded(self, oldNamespace: ghidra.program.model.symbol.Namespace, oldName: unicode, oldSource: ghidra.program.model.symbol.SourceType) -> None: ...

    def setAddress(self, address: ghidra.program.model.address.Address) -> None: ...

    def setDataType(self, dt: ghidra.program.model.data.DataType) -> None:
        """
        @see ghidra.program.model.symbol.ExternalLocation#setDataType(ghidra.program.model.data.DataType)
        """
        ...

    def setLocation(self, label: unicode, addr: ghidra.program.model.address.Address, source: ghidra.program.model.symbol.SourceType) -> None: ...

    def setName(self, namespace: ghidra.program.model.symbol.Namespace, newName: unicode, sourceType: ghidra.program.model.symbol.SourceType) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def address(self) -> ghidra.program.model.address.Address: ...

    @address.setter
    def address(self, value: ghidra.program.model.address.Address) -> None: ...

    @property
    def dataType(self) -> ghidra.program.model.data.DataType: ...

    @dataType.setter
    def dataType(self, value: ghidra.program.model.data.DataType) -> None: ...

    @property
    def externalSpaceAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def function(self) -> bool: ...

    @property
    def label(self) -> unicode: ...

    @property
    def libraryName(self) -> unicode: ...

    @property
    def originalImportedName(self) -> unicode: ...

    @property
    def parentName(self) -> unicode: ...

    @property
    def parentNameSpace(self) -> ghidra.program.model.symbol.Namespace: ...

    @property
    def source(self) -> ghidra.program.model.symbol.SourceType: ...

    @property
    def symbol(self) -> ghidra.program.model.symbol.Symbol: ...
