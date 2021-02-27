import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.symbol
import java.lang


class SymbolType(object):
    """
    Class to represent the various types of Symbols.
    """

    CLASS: ghidra.program.model.symbol.SymbolType = Class
    CODE: ghidra.program.model.symbol.SymbolType = Label
    FUNCTION: ghidra.program.model.symbol.SymbolType = Function
    GLOBAL: ghidra.program.model.symbol.SymbolType = Global
    GLOBAL_VAR: ghidra.program.model.symbol.SymbolType = Global Register Var
    LABEL: ghidra.program.model.symbol.SymbolType = Label
    LIBRARY: ghidra.program.model.symbol.SymbolType = Library
    LOCAL_VAR: ghidra.program.model.symbol.SymbolType = Local Var
    NAMESPACE: ghidra.program.model.symbol.SymbolType = Namespace
    PARAMETER: ghidra.program.model.symbol.SymbolType = Parameter







    def allowsDuplicates(self) -> bool:
        """
        Returns true of this symbol type allows duplicate names.
        @return true of this symbol type allows duplicate names.
        """
        ...

    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getID(self) -> int:
        """
        Returns the id of this symbol type.
        """
        ...

    @staticmethod
    def getSymbolType(id: int) -> ghidra.program.model.symbol.SymbolType:
        """
        Returns the SymbolType for the given id.
        @param id the id for the SymbolType to find.
        """
        ...

    def hashCode(self) -> int: ...

    def isNamespace(self) -> bool:
        """
        Returns true if this symbol represents a namespace.
        """
        ...

    def isValidAddress(self, program: ghidra.program.model.listing.Program, symbolAddress: ghidra.program.model.address.Address) -> bool:
        """
        Returns true if the given address is valid for this symbol type.
        @param program the program to test for a valid address.
        @param symbolAddress the address of the symbol to be tested.
        @return true if the given address is valid within the given program.
        """
        ...

    def isValidParent(self, program: ghidra.program.model.listing.Program, parent: ghidra.program.model.symbol.Namespace, symbolAddr: ghidra.program.model.address.Address, isExternalSymbol: bool) -> bool:
        """
        Returns true if the given namespace is a valid parent for a symbol of this type
         if it has the given address and whether or not it is external.
        @param program the program to contain the symbol
        @param parent the namespace where a symbol will potentially be parented.
        @param symbolAddr the address of they symbol to be parented.
        @param isExternalSymbol true if the symbol is external.
        @return true if the given namespace is a valid parent for a symbol if it has the
         given address and whether or not it is external.
        """
        ...

    def isValidSourceType(self, sourceType: ghidra.program.model.symbol.SourceType, symbolAddress: ghidra.program.model.address.Address) -> bool:
        """
        Returns true if the given SourceType is valid for this symbol type. (For example, Some symbols
         don't support the SymbolType.DEFAULT)
        @param sourceType the sourceType to test.
        @param symbolAddress the address of the symbol to be tested.
        @return true if the given SourceType is valid for this symbol type.
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
    def ID(self) -> int: ...

    @property
    def namespace(self) -> bool: ...
