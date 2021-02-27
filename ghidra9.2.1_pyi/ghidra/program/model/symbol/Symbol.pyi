from typing import List
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.symbol
import ghidra.program.util
import ghidra.util.task
import java.lang


class Symbol(object):
    """
    Interface for a symbol, which associates a string value with
     an address.
    """









    def checkIsValid(self) -> bool:
        """
        Check whether this symbol is still valid (i.e., deleted).
        @return true if valid or false if deleted.
        """
        ...

    def delete(self) -> bool:
        """
        Delete the symbol and its associated resources.
        @return true if successful
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address:
        """
        @return the address for the symbol.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getID(self) -> long:
        """
        @return this symbol's ID.
        """
        ...

    @overload
    def getName(self) -> unicode:
        """
        @return the name of this symbol.
        """
        ...

    @overload
    def getName(self, includeNamespace: bool) -> unicode:
        """
        Returns the symbol name, optionally prepended with the namespace path.
        @param includeNamespace if true, the namespace path is prepended to the name.
        @return formatted name
        """
        ...

    def getObject(self) -> object:
        """
        @return object associated with this symbol or null if symbol has been deleted
        """
        ...

    def getParentNamespace(self) -> ghidra.program.model.symbol.Namespace:
        """
        @return the namespace that contains this symbol
        """
        ...

    def getParentSymbol(self) -> ghidra.program.model.symbol.Symbol:
        """
        Returns namespace symbol of the namespace containing this symbol
        """
        ...

    def getPath(self) -> List[unicode]:
        """
        Gets the full path name for this symbol as an ordered array of strings ending
         with the symbol name. The global symbol will return an empty array.
        @return the array indicating the full path name for this symbol.
        """
        ...

    def getProgram(self) -> ghidra.program.model.listing.Program:
        """
        @return the program associated with this symbol.
         Null may be returned for global symbols.
        """
        ...

    def getProgramLocation(self) -> ghidra.program.util.ProgramLocation:
        """
        @return a program location corresponding to this symbol
        """
        ...

    def getReferenceCount(self) -> int:
        """
        @return the number of References to this symbol.
        """
        ...

    @overload
    def getReferences(self) -> List[ghidra.program.model.symbol.Reference]:
        """
        Returns all memory references to the address of this symbol.
        @return all memory references to the address of this symbol
        @see #getReferences(TaskMonitor)
        """
        ...

    @overload
    def getReferences(self, monitor: ghidra.util.task.TaskMonitor) -> List[ghidra.program.model.symbol.Reference]:
        """
        Returns all memory references to the address of this symbol.  If you do not have a
         {@link TaskMonitor} instance, then you can pass {@link TaskMonitorAdapter#DUMMY_MONITOR} or
         <code>null</code>.
        @return all memory references to the address of this symbol.
        @param monitor the monitor that is used to report progress and to cancel this
                potentially long-running call
        """
        ...

    def getSource(self) -> ghidra.program.model.symbol.SourceType:
        """
        Gets the source of this symbol.
         {@link SourceType}
        @return the source of this symbol
        """
        ...

    def getSymbolType(self) -> ghidra.program.model.symbol.SymbolType:
        """
        Returns the symbol type
        """
        ...

    def hasMultipleReferences(self) -> bool:
        """
        @return true if this symbol has more than one reference to it.
        """
        ...

    def hasReferences(self) -> bool:
        """
        @return true if this symbol has at least one reference to it.
        """
        ...

    def hashCode(self) -> int: ...

    def isDescendant(self, namespace: ghidra.program.model.symbol.Namespace) -> bool:
        """
        Returns true if the given namespace symbol is a descendant of this symbol.
        @param namespace to test as descendant symbol of this Symbol
        @return true if this symbol is an ancestor of the given namespace symbol
        """
        ...

    def isDynamic(self) -> bool:
        """
        @return true if this symbol is a dynamic symbol (not actually defined in the database).
        """
        ...

    def isExternal(self) -> bool:
        """
        Returns true if this an external symbol.
        @return true if this an external symbol.
        @see Address#isExternalAddress()
        """
        ...

    def isExternalEntryPoint(self) -> bool:
        """
        @return true if the symbol is at an address
         set as a external entry point.
        """
        ...

    def isGlobal(self) -> bool:
        """
        @return true if the symbol is global
        """
        ...

    def isPinned(self) -> bool:
        """
        Returns true if the symbol is pinned to its current address. If it is pinned, then moving
         or removing the memory associated with that address will not affect this symbol.
        @return true if the symbol is pinned to its current address.
        """
        ...

    def isPrimary(self) -> bool:
        """
        @return true if this symbol is primary
        """
        ...

    def isValidParent(self, parent: ghidra.program.model.symbol.Namespace) -> bool:
        """
        Returns whether the given parent is valid for this Symbol.
        @param parent
        @return true if parent is valid
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setName(self, newName: unicode, source: ghidra.program.model.symbol.SourceType) -> None:
        """
        Sets the name this symbol.
         If this symbol is dynamic, then the name is set
         and the symbol is no longer dynamic.
        @param newName the new name for this symbol.
        @param source the source of this symbol
         <br>Some symbol types, such as function symbols, can set the source to Symbol.DEFAULT.
        @throws DuplicateNameException if name already exists as the name of another symbol or alias.
        @throws InvalidInputException if alias contains blank characters, is zero length, or is null
        @throws IllegalArgumentException if you try to set the source to DEFAULT for a symbol type
         that doesn't allow it.
        """
        ...

    def setNameAndNamespace(self, newName: unicode, newNamespace: ghidra.program.model.symbol.Namespace, source: ghidra.program.model.symbol.SourceType) -> None:
        """
        Sets the symbols name and namespace.  This is provided to allow the caller to
         avoid a name conflict by creating an autonomous action.
        @param newName new symbol name
        @param newNamespace new parent namespace
        @param source the source of this symbol
         <br>Some symbol types, such as function symbols, can set the source to Symbol.DEFAULT.
        @throws DuplicateNameException if newNamespace already contains a symbol
         with this symbol's name
        @throws InvalidInputException is newNamespace is not a valid parent for
         this symbol
        @throws CircularDependencyException if this symbol is an ancestor of
         newNamespace
        """
        ...

    def setNamespace(self, newNamespace: ghidra.program.model.symbol.Namespace) -> None:
        """
        Sets the symbols namespace
        @param newNamespace new parent namespace
        @throws DuplicateNameException if newNamespace already contains a symbol
         with this symbol's name
        @throws InvalidInputException is newNamespace is not a valid parent for
         this symbol
        @throws CircularDependencyException if this symbol is an ancestor of
         newNamespace
        """
        ...

    def setPinned(self, pinned: bool) -> None:
        """
        <p>Sets whether or not this symbol is pinned to its associated address.</p>

         <p>If the symbol is pinned then moving or removing the memory associated with its address will
         not cause this symbol to be removed and will not cause its address to change.
         If the symbol is not pinned, then removing the memory at its address will also remove this
         symbol.</p>

         <p>Likewise, moving a memory block containing a symbol that is not anchored will change
         the address for that symbol to keep it associated with the same byte in the memory block.</p>
        @param pinned true indicates this symbol is anchored to its address.
         		false indicates this symbol is not anchored to its address.
        """
        ...

    def setPrimary(self) -> bool:
        """
        Sets this symbol to be primary. All other symbols at the same address will be set to
         !primary.  Only applies to non-function symbols.
        @return returns true if the symbol was not primary and now it is, otherwise false
        """
        ...

    def setSource(self, source: ghidra.program.model.symbol.SourceType) -> None:
        """
        Sets the source of this symbol.
         {@link SourceType}
        @param source the new source of this symbol
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
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def dynamic(self) -> bool: ...

    @property
    def external(self) -> bool: ...

    @property
    def externalEntryPoint(self) -> bool: ...

    @property
    def global(self) -> bool: ...

    @property
    def name(self) -> unicode: ...

    @property
    def namespace(self) -> None: ...  # No getter available.

    @namespace.setter
    def namespace(self, value: ghidra.program.model.symbol.Namespace) -> None: ...

    @property
    def object(self) -> object: ...

    @property
    def parentNamespace(self) -> ghidra.program.model.symbol.Namespace: ...

    @property
    def parentSymbol(self) -> ghidra.program.model.symbol.Symbol: ...

    @property
    def path(self) -> List[unicode]: ...

    @property
    def pinned(self) -> bool: ...

    @pinned.setter
    def pinned(self, value: bool) -> None: ...

    @property
    def primary(self) -> bool: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...

    @property
    def programLocation(self) -> ghidra.program.util.ProgramLocation: ...

    @property
    def referenceCount(self) -> int: ...

    @property
    def references(self) -> List[ghidra.program.model.symbol.Reference]: ...

    @property
    def source(self) -> ghidra.program.model.symbol.SourceType: ...

    @source.setter
    def source(self, value: ghidra.program.model.symbol.SourceType) -> None: ...

    @property
    def symbolType(self) -> ghidra.program.model.symbol.SymbolType: ...
