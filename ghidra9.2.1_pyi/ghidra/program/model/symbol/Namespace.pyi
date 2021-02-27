import ghidra.program.model.address
import ghidra.program.model.symbol
import java.lang


class Namespace(object):
    """
    The Namespace interface
    """

    DELIMITER: unicode = u'::'
    GLOBAL_NAMESPACE_ID: long = 0x0L
    NAMESPACE_DELIMITER: unicode = u'::'







    def equals(self, __a0: object) -> bool: ...

    def getBody(self) -> ghidra.program.model.address.AddressSetView:
        """
        Get the address set for this namespace.  Note: The body of a namespace (currently
         only used by the function namespace) is restricted it Integer.MAX_VALUE.
        @return the address set for this namespace
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getID(self) -> long:
        """
        Return the namespace id
        @return the namespace id
        """
        ...

    @overload
    def getName(self) -> unicode:
        """
        Get the name of the symbol for this scope
        @return the name of the symbol for this scope
        """
        ...

    @overload
    def getName(self, includeNamespacePath: bool) -> unicode:
        """
        Returns the fully qualified name
        @param includeNamespacePath true to include the namespace in the returned name
        @return the fully qualified name
        """
        ...

    def getParentNamespace(self) -> ghidra.program.model.symbol.Namespace:
        """
        Get the parent scope.
        @return null if this scope is the global scope.
        """
        ...

    def getSymbol(self) -> ghidra.program.model.symbol.Symbol:
        """
        Get the symbol for this namespace; Note: The global namespace will return null
        @return the symbol for this namespace; Note: The global namespace will return null
        """
        ...

    def hashCode(self) -> int: ...

    def isExternal(self) -> bool:
        """
        Returns true if this namespace is external (i.e., associated with a Library)
        @return true if this namespace is external (i.e., associated with a Library)
        """
        ...

    def isGlobal(self) -> bool:
        """
        Return true if this is the global namespace;
        @return true if this is the global namespace;
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setParentNamespace(self, parentNamespace: ghidra.program.model.symbol.Namespace) -> None:
        """
        Set the parent namespace for this namespace. Restrictions may apply.
        @param parentNamespace the namespace to use as this namespace's parent.
        @throws InvalidInputException if the parent namespace is not applicable for
         this namespace.
        @throws DuplicateNameException if another symbol exists in the parent namespace with
         the same name as this namespace
        @throws CircularDependencyException if the parent namespace is a descendent of this
         namespace.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def ID(self) -> long: ...

    @property
    def body(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def external(self) -> bool: ...

    @property
    def global(self) -> bool: ...

    @property
    def name(self) -> unicode: ...

    @property
    def parentNamespace(self) -> ghidra.program.model.symbol.Namespace: ...

    @parentNamespace.setter
    def parentNamespace(self, value: ghidra.program.model.symbol.Namespace) -> None: ...

    @property
    def symbol(self) -> ghidra.program.model.symbol.Symbol: ...
