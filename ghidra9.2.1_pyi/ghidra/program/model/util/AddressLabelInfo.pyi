import ghidra.program.model.address
import ghidra.program.model.symbol
import ghidra.program.model.util
import java.lang


class AddressLabelInfo(object, java.lang.Comparable):
    """
    AddressLabelInfo is a utility class for storing
     an Address and a corresponding label or alias together.
    """





    @overload
    def __init__(self, addr: ghidra.program.model.address.Address):
        """
        Constructs a new AddressLabelInfo object with only address information
        @param addr the address to store in this object
        """
        ...

    @overload
    def __init__(self, s: ghidra.program.model.symbol.Symbol):
        """
        Constructs a new AddressLabelInfo object
        @param s symbol to initialize info from.
        """
        ...

    @overload
    def __init__(self, addr: ghidra.program.model.address.Address, label: unicode, isPrimary: bool, symbolSource: ghidra.program.model.symbol.SourceType): ...

    @overload
    def __init__(self, addr: ghidra.program.model.address.Address, label: unicode, isPrimary: bool, scope: ghidra.program.model.symbol.Namespace, symbolSource: ghidra.program.model.symbol.SourceType, isEntry: bool): ...

    @overload
    def __init__(self, addr: ghidra.program.model.address.Address, label: unicode, isPrimary: bool, scope: ghidra.program.model.symbol.Namespace, symbolSource: ghidra.program.model.symbol.SourceType, isEntry: bool, type: ghidra.program.model.util.ProcessorSymbolType): ...



    @overload
    def compareTo(self, info: ghidra.program.model.util.AddressLabelInfo) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the object's address.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getLabel(self) -> unicode:
        """
        Returns the object's label or alias.
        """
        ...

    def getProcessorSymbolType(self) -> ghidra.program.model.util.ProcessorSymbolType:
        """
        Returns the type of processor symbol (if this was defined by a pspec) or null if this
         is not a processor symbol or it was not specified in the pspec file.  It basically allows
         a pspec file to give more information about a symbol such as if code or a code pointer is
         expected to be at the symbol's address.
        @return the ProcesorSymbolType if it has one.
        """
        ...

    def getScope(self) -> ghidra.program.model.symbol.Namespace:
        """
        Returns the scope for the symbol.
        """
        ...

    def getSource(self) -> ghidra.program.model.symbol.SourceType: ...

    def hashCode(self) -> int: ...

    def isEntry(self) -> bool: ...

    def isPrimary(self) -> bool:
        """
        Returns whether the object is the primary label at the address.
        """
        ...

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
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def entry(self) -> bool: ...

    @property
    def label(self) -> unicode: ...

    @property
    def primary(self) -> bool: ...

    @property
    def processorSymbolType(self) -> ghidra.program.model.util.ProcessorSymbolType: ...

    @property
    def scope(self) -> ghidra.program.model.symbol.Namespace: ...

    @property
    def source(self) -> ghidra.program.model.symbol.SourceType: ...
