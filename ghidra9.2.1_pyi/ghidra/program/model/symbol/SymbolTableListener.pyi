import ghidra.program.model.address
import ghidra.program.model.symbol
import java.lang


class SymbolTableListener(object):
    """
    Listener methods that are called when changes to symbols are made.
    """









    def associationAdded(self, symbol: ghidra.program.model.symbol.SourceType, ref: ghidra.program.model.symbol.Reference) -> None:
        """
        Notification that the association between a reference and a
         specific symbol has changed.
        @param symbol affected symbol
        @param ref affected reference
        """
        ...

    def associationRemoved(self, ref: ghidra.program.model.symbol.Reference) -> None:
        """
        Notification that the association between the given reference and
         any symbol was removed.
        @param ref the reference that had a symbol association removed.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def externalEntryPointAdded(self, addr: ghidra.program.model.address.Address) -> None:
        """
        Notification that an external entry point was added at the
         given address.
        @param addr the address that made an external entry point.
        """
        ...

    def externalEntryPointRemoved(self, addr: ghidra.program.model.address.Address) -> None:
        """
        Notification that an external entry point was removed from the given
         address.
        @param addr the address the removed as an external entry point.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def primarySymbolSet(self, symbol: ghidra.program.model.symbol.SourceType) -> None:
        """
        Notification the the given symbol was set as the primary symbol.
        @param symbol the symbol that is now primary.
        """
        ...

    def symbolAdded(self, symbol: ghidra.program.model.symbol.SourceType) -> None:
        """
        Notification that the given symbol has been added.
        @param symbol the symbol that was added.
        """
        ...

    def symbolRemoved(self, addr: ghidra.program.model.address.Address, name: unicode, isLocal: bool) -> None:
        """
        Notification that a symbol was removed.
        @param addr address where the symbol was
        @param name name of symbol
        @param isLocal true if the symbol was in the scope
         of a function
        """
        ...

    def symbolRenamed(self, symbol: ghidra.program.model.symbol.SourceType, oldName: unicode) -> None:
        """
        Notification that the given symbol was renamed.
        @param symbol symbol that was renamed
        @param oldName old name of the symbol
        """
        ...

    def symbolScopeChanged(self, symbol: ghidra.program.model.symbol.SourceType) -> None:
        """
        Notification that the scope on a symbol changed.
        @param symbol the symbol whose scope has changed.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
