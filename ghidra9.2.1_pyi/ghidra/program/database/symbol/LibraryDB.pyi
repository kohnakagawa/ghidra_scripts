import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.symbol
import java.lang


class LibraryDB(object, ghidra.program.model.listing.Library):
    """
    Object to represent an external library.
    """









    def equals(self, obj: object) -> bool:
        """
        @see java.lang.Object#equals(java.lang.Object)
        """
        ...

    def getAssociatedProgramPath(self) -> unicode: ...

    def getBody(self) -> ghidra.program.model.address.AddressSetView:
        """
        @see ghidra.program.model.symbol.Namespace#getBody()
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getID(self) -> long:
        """
        @see ghidra.program.model.symbol.Namespace#getID()
        """
        ...

    @overload
    def getName(self) -> unicode:
        """
        @see ghidra.program.model.symbol.Namespace#getName()
        """
        ...

    @overload
    def getName(self, includeNamespacePath: bool) -> unicode:
        """
        @see ghidra.program.model.symbol.Namespace#getName(boolean)
        """
        ...

    def getParentNamespace(self) -> ghidra.program.model.symbol.Namespace:
        """
        @see ghidra.program.model.symbol.Namespace#getParentNamespace()
        """
        ...

    def getSymbol(self) -> ghidra.program.model.symbol.Symbol:
        """
        @see ghidra.program.model.symbol.Namespace#getSymbol()
        """
        ...

    def hashCode(self) -> int: ...

    def isExternal(self) -> bool: ...

    def isGlobal(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setParentNamespace(self, parentNamespace: ghidra.program.model.symbol.Namespace) -> None:
        """
        @see ghidra.program.model.symbol.Namespace#setParentNamespace(ghidra.program.model.symbol.Namespace)
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
