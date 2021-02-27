from typing import Iterator
from typing import List
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.symbol
import java.lang


class SymbolTable(object):
    """
    A SymbolTable manages the Symbols defined in a program.

     A Symbol is an association between an Address,
     a String name. In addition, symbols may have one or more
     References.

     A Reference is a 4-tuple of a source address, destination address, type,
     and either a mnemonic or operand index

     Any address in a program can have more than one symbol associated to it.
     At any given time, one and only one symbol will be designated as the primary.

     A symbol can be either global or local. Local symbols belong to some namespace other than
     the global namespace.

     Label and Function symbols do not have to have unique names with a namespace. All other symbols
     must be unique within a namespace and be unique with all other symbols that must be unique.
     In other words you can have a several functions named "foo" and several labels named "foo"
     in the same namespace.  But you can't have a class named "foo" and a namespace named "foo".
     But you can have a class named "foo" and and many functions and labels named "foo" all
     in the same namespace.

     A symbol can also be designated as dynamic. Which means the name is
     generated on-the-fly by the system based on its context.
    """









    def addExternalEntryPoint(self, addr: ghidra.program.model.address.Address) -> None:
        """
        Sets the given address to be an external entry point.
        @param addr the address to set as an external entry point.
        """
        ...

    def createClass(self, parent: ghidra.program.model.symbol.Namespace, name: unicode, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.listing.GhidraClass:
        """
        Create a class namespace in the given parent namespace.
        @param parent parent namespace
        @param name name of the namespace
        @param source the source of this class namespace's symbol
        @return new class namespace
        @throws DuplicateNameException thrown if another non function or lable symbol exists with the given name
        @throws InvalidInputException throw if the name has invalid characters or is null
        @throws IllegalArgumentException if you try to set the source to 'Symbol.DEFAULT'.
        """
        ...

    def createExternalLibrary(self, name: unicode, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.listing.Library:
        """
        Creates a Library namespace with the given name.
        @param name the name of the new Library namespace
        @param source the source of this external library's symbol
        @return the new Library namespace.
        @throws IllegalArgumentException if you try to set the source to 'Symbol.DEFAULT'.
        @throws DuplicateNameException thrown if another non function or lable symbol exists with the given name
        """
        ...

    @overload
    def createLabel(self, addr: ghidra.program.model.address.Address, name: unicode, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.Symbol:
        """
        Create a label symbol with the given name associated to the given
         Address. The symbol will be global and be of type SymbolType.CODE. Label
         Symbols do not have to have unique names.
         If this is the first symbol defined for the address it becomes
         the primary.
        @param addr the address at which to create a symbol
        @param name the name of the symbol.
        @param source the source of this symbol
         <br>Some symbol types, such as function symbols, can set the source to Symbol.DEFAULT.
        @throws InvalidInputException thrown if names contains white space, is zero length, or is
                     null.  Also thrown if invalid parentNamespace is specified.
        @throws IllegalArgumentException if you try to set the source to DEFAULT for a symbol type
         that doesn't allow it, or an improper addr if specified
        """
        ...

    @overload
    def createLabel(self, addr: ghidra.program.model.address.Address, name: unicode, namespace: ghidra.program.model.symbol.Namespace, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.Symbol:
        """
        Create a label symbol with the given name associated to the given
         Address and namespace. The symbol will be of type SymbolType.CODE.
         If this is the first symbol defined for the address it becomes
         the primary symbol.  If a symbol with that name already exists at the
         address, it will be returned instead with its namespace changed to the new
         namespace unless the new symbol is in the global space, in which case the namespace
         will remain as is.
        @param addr the address at which to create a symbol
        @param name the name of the symbol.
        @param namespace the namespace of the symbol.
        @param source the source of this symbol
         <br>Some symbol types, such as function symbols, can set the source to Symbol.DEFAULT.
        @return new code or function symbol
        @throws IllegalArgumentException if you try to set the source to DEFAULT for a symbol type
         that doesn't allow it, or an improper addr if specified
        """
        ...

    def createNameSpace(self, parent: ghidra.program.model.symbol.Namespace, name: unicode, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.Namespace:
        """
        Creates a new namespace.
        @param parent the parent namespace for the new namespace
        @param name the name of the new namespace
        @param source the source of this namespace's symbol
        @return the new Namespace object.
        @throws DuplicateNameException thrown if another non function or lable symbol exists with the given name
        @throws InvalidInputException if the name is invalid.
        @throws IllegalArgumentException if you try to set the source to 'Symbol.DEFAULT'.
        """
        ...

    @overload
    def createSymbol(self, addr: ghidra.program.model.address.Address, name: unicode, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.Symbol:
        """
        @deprecated use {@link #createLabel(Address, String, SourceType)} instead.
         Deprecated in version 7.5, will be removed a few versions later.
        """
        ...

    @overload
    def createSymbol(self, addr: ghidra.program.model.address.Address, name: unicode, namespace: ghidra.program.model.symbol.Namespace, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.Symbol:
        """
        @deprecated use {@link #createLabel(Address, String, Namespace, SourceType)} instead.
         Deprecated in version 7.5, will be removed a few versions later.
        """
        ...

    def createSymbolPlaceholder(self, address: ghidra.program.model.address.Address, id: long) -> ghidra.program.model.symbol.Symbol:
        """
        Creates a Symbol that is just a placeholder for use when trying to find symbols by using
         {@link Symbol#getID()}.   This is useful for locating symbols in Java collections when
         a symbol has been deleted and the only remaining information is that symbol's ID.
        @param address the address of the symbol
        @param id the id of the symbol
        @return the fake symbol
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAllSymbols(self, includeDynamicSymbols: bool) -> ghidra.program.model.symbol.SymbolIterator:
        """
        Returns an iterator over all symbols, including Dynamic symbols if
         includeDynamicSymbols is true.
        @param includeDynamicSymbols if true, the iterator will include dynamicSymbols
        """
        ...

    def getChildren(self, parentSymbol: ghidra.program.model.symbol.Symbol) -> ghidra.program.model.symbol.SymbolIterator:
        """
        Returns an iterator over all symbols that have the given symbol as its parent..
        @param parentSymbol the parent symbol
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getClassNamespaces(self) -> Iterator[ghidra.program.model.listing.GhidraClass]:
        """
        Returns all Class Namespaces defined within the program.
        """
        ...

    def getClassSymbol(self, name: unicode, namespace: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the class symbol with the given name in the given namespace.
        @param name the name of the class.
        @param namespace the namespace to search for the class.
        @return the class symbol with the given name in the given namespace.
        """
        ...

    def getDefinedSymbols(self) -> ghidra.program.model.symbol.SymbolIterator:
        """
        Returns an iterator over all defined symbols in no particular order.
        """
        ...

    def getDynamicSymbolID(self, addr: ghidra.program.model.address.Address) -> long:
        """
        Get the unique symbol ID for a dynamic symbol associated with the speified addr.
         The generation of this symbol ID does not reflect the presence of a dyanmic symbol
         at the specified addr.  This symbol ID should not be permanently stored since the encoding
         may change between software releases.
        @param addr dynamic symbol address
        @return unique symbol ID
        """
        ...

    def getExternalEntryPointIterator(self) -> ghidra.program.model.address.AddressIterator:
        """
        Get forward/back iterator over addresses that are entry points.
        """
        ...

    def getExternalSymbol(self, name: unicode) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the external symbol with the given name.
        @param name the name of the symbol to be retrieved.
        @return symbol, or null if no external symbol has that name
        """
        ...

    @overload
    def getExternalSymbols(self) -> ghidra.program.model.symbol.SymbolIterator:
        """
        Returns an iterator over all defined external symbols in no particular order.
        """
        ...

    @overload
    def getExternalSymbols(self, name: unicode) -> ghidra.program.model.symbol.SymbolIterator:
        """
        Returns all the external symbols with the given name.
        @param name the name of symbols to search for.
        @return array of external symbols with the given name
        """
        ...

    def getGlobalSymbol(self, name: unicode, addr: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Symbol:
        """
        Get the global symbol with the given name and address.  Note that this results in a single
         Symbol because of an additional restriction that allows only one symbol with a given name
         at the same address and namespace (in this case the global namespace).

         <P>This is just a convenience method for {@link #getSymbol(String, Address, Namespace)} where
         the namespace is the global namespace.</P>
        @param name the name of the symbol to retrieve
        @param addr the address of the symbol to retrieve
        @see #getSymbol(String, Address, Namespace)
        """
        ...

    def getGlobalSymbols(self, name: unicode) -> List[ghidra.program.model.symbol.Symbol]:
        """
        Returns a list of all global symbols with the given name.
        @param name the name of the symbols to retrieve.
        @return a list of all global symbols with the given name.
        """
        ...

    @overload
    def getLabelHistory(self) -> Iterator[ghidra.program.model.symbol.LabelHistory]:
        """
        Get an iterator over all the label history objects.
        """
        ...

    @overload
    def getLabelHistory(self, addr: ghidra.program.model.address.Address) -> List[ghidra.program.model.symbol.LabelHistory]:
        """
        Get the label history objects for the given address. The history
         object records changes made to labels at some address.
        @param addr address of the label change
        @return array of history objects
        """
        ...

    def getLabelOrFunctionSymbols(self, name: unicode, namespace: ghidra.program.model.symbol.Namespace) -> List[ghidra.program.model.symbol.Symbol]:
        """
        Returns all the label or function symbols that have the given name in the given namespace.
        @param name the name of the symbols to search for.
        @param namespace the namespace to search.  If null, then the global namespace is assumed.
        @return a list of all the label or function symbols with the given name in the given namespace.
        """
        ...

    def getLibrarySymbol(self, name: unicode) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the library symbol with the given name.
        @param name the name of the library symbol to retrieve.
        @return the library symbol with the given name.
        """
        ...

    def getLocalVariableSymbol(self, name: unicode, namespace: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the local variable symbol with the given name in the given namespace.
        @param name the name of the local variable.
        @param namespace the namespace (function) to search for the class.
        @return the local variable symbol with the given name in the given namespace.
        """
        ...

    @overload
    def getNamespace(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Namespace:
        """
        Returns the lowest level Namespace within which the specified address is contained.
        @param addr the address for which to finds its enclosing namespace.
        """
        ...

    @overload
    def getNamespace(self, name: unicode, namespace: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.symbol.Namespace:
        """
        Returns the namespace with the given name in the given parent namespace.  The namespace
         returned can be either a generic namespace or a class or library.  It does not include
         functions.
        @param name the name of the namespace to be retrieved.
        @param namespace the parent namespace of the namespace to be retrieved.
        @return the namespace with the given name in the given parent namespace.
        """
        ...

    def getNamespaceSymbol(self, name: unicode, namespace: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.symbol.Symbol:
        """
        Returns a generic namespace symbol with the given name in the given namespace.
        @param name the name of the namespace symbol to retrieve.
        @param namespace the namespace containing the symbol to retrieve.
        @return a generic namespace symbol with the given name in the given namespace.
        """
        ...

    def getNumSymbols(self) -> int:
        """
        Returns the total number of symbols in the table.
        """
        ...

    def getParameterSymbol(self, name: unicode, namespace: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the parameter symbol with the given name in the given namespace.
        @param name the name of the parameter.
        @param namespace the namespace (function) to search for the class.
        @return the parameter symbol with the given name in the given namespace.
        """
        ...

    def getPrimarySymbol(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the primary symbol at the specified
         address.  This method will always return null if the address specified
         is neither a Memory address nor an External address.
        @param addr the address at which to retrieve the primary symbol
        @return symbol, or null if no symbol at that address
        """
        ...

    @overload
    def getPrimarySymbolIterator(self, forward: bool) -> ghidra.program.model.symbol.SymbolIterator:
        """
        Get iterator over all primary symbols.
        @param forward true means the iterator is in the forward direction
        """
        ...

    @overload
    def getPrimarySymbolIterator(self, startAddr: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.symbol.SymbolIterator:
        """
        Get iterator over only primary symbols starting at
         the specified <code>startAddr</code>
        @param startAddr the address at which to begin the iteration.
        @param forward true means the iterator is in the forward direction
        """
        ...

    @overload
    def getPrimarySymbolIterator(self, asv: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.symbol.SymbolIterator:
        """
        Get an iterator over symbols at addresses in the given addressSet
        @param asv the set of address over which to iterate symbols.
        @param forward true means the iterator is in the forward direction
        """
        ...

    @overload
    def getSymbol(self, symbolID: long) -> ghidra.program.model.symbol.Symbol:
        """
        Get the symbol for the given symbol ID.
        @param symbolID the id of the symbol to be retrieved.
        @return null if there is no symbol with the given ID.
        """
        ...

    @overload
    def getSymbol(self, name: unicode) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the first global symbol that it finds with the given name.  Now that Ghidra
         allows duplicate symbol names, this method is practically useless.
        @param name the name of the symbol to be retrieved.
        @return symbol, or null if no global symbol has that name
        @deprecated Use {@link #getGlobalSymbols(String)} instead.  Ghidra now allows
         multiple symbols in any namespace to have the same name.  Deprecated in Ghidra 7.5
         Deprecated in version 7.5, will be removed a few versions later.
        """
        ...

    @overload
    def getSymbol(self, ref: ghidra.program.model.symbol.Reference) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the symbol that this reference is associated with.
        @param ref the reference to find the associated symbol for.
        """
        ...

    @overload
    def getSymbol(self, name: unicode, namespace: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the first symbol with the given name found in the given namespace. Ghidra now
         allows multiple symbols with the same name in the same namespace, so using this method
         is likely to produce unintended results. Use {@link #getSymbols(String, Namespace)} instead.
        @param name the name of the symbol to retreive
        @param namespace the namespace of the symbol to retrieve (null assumes global namespace)
        @deprecated This method is no longer useful as Ghidra allows duplicate symbol names in
         the same namespace. Use {@link #getSymbols(String, Namespace)} instead.
         Deprecated in version 7.5, will be removed a few versions later.
        """
        ...

    @overload
    def getSymbol(self, name: unicode, addr: ghidra.program.model.address.Address, namespace: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.symbol.Symbol:
        """
        Get the symbol with the given name, address, and namespace.
         <P>
         Note that for a symbol to be uniquely specified, all these parameters are required. Any method
         that queries for symbols using just one or two of these parameters will return a list of symbols.
         </P>
        @param name the name of the symbol to retrieve
        @param addr the address of the symbol to retrieve
        @param namespace the namespace of the symbol to retrieve. May be null which indicates global namespace.
        @see #getGlobalSymbol(String, Address) for a convenience method if the namespace is the global namespace.
        """
        ...

    @overload
    def getSymbolIterator(self) -> ghidra.program.model.symbol.SymbolIterator:
        """
        Get iterator over all label symbols. Labels are defined on memory locations.
        """
        ...

    @overload
    def getSymbolIterator(self, forward: bool) -> ghidra.program.model.symbol.SymbolIterator:
        """
        Returns an iterator over all symbols.
        @param forward true means the iterator is in the forward direction
        """
        ...

    @overload
    def getSymbolIterator(self, searchStr: unicode, caseSensitive: bool) -> ghidra.program.model.symbol.SymbolIterator:
        """
        Returns a an iterator over all symbols that match the given search string.
         NOTE: The iterator is in the forward direction only.
        @param searchStr the string to search for (may contain * to match any sequence
         or ? to match a single char)
        @param caseSensitive flag to determine if the search is case sensitive or not.
        """
        ...

    @overload
    def getSymbolIterator(self, startAddr: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.symbol.SymbolIterator:
        """
        Get iterator over all symbols starting at
         the specified <code>startAddr</code>
        @param startAddr the address at which to begin the iteration.
        @param forward true means the iterator is in the forward direction
        """
        ...

    @overload
    def getSymbols(self, namespaceID: long) -> ghidra.program.model.symbol.SymbolIterator:
        """
        Returns an iterator over all the symbols in the given namespace
        @param namespaceID the namespace ID to search for symbols.
        """
        ...

    @overload
    def getSymbols(self, name: unicode) -> ghidra.program.model.symbol.SymbolIterator:
        """
        Returns all the symbols with the given name.
        @param name the name of symbols to search for.
        @return array of symbols with the given name
        """
        ...

    @overload
    def getSymbols(self, addr: ghidra.program.model.address.Address) -> List[ghidra.program.model.symbol.Symbol]:
        """
        Returns all the symbols at the given address.  When addr is a memory address
         the primary symbol will be returned in array slot 0.
         WARNING! Use of this method with a Variable address is highly discouraged since
         a single Variable address could be used multiple times by many functions.
        @param addr the address at which to retrieve all symbols.
        @return a zero-length array when no symbols are defined at address.
        """
        ...

    @overload
    def getSymbols(self, namespace: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.symbol.SymbolIterator:
        """
        Returns an iterator over all the symbols in the given namespace
        @param namespace the namespace to search for symbols.
        """
        ...

    @overload
    def getSymbols(self, name: unicode, namespace: ghidra.program.model.symbol.Namespace) -> List[ghidra.program.model.symbol.Symbol]:
        """
        Returns a list of all symbols with the given name in the given namespace.
        @param name the name of the symbols to retrieve.
        @param namespace the namespace to search for symbols.
        @return
        """
        ...

    @overload
    def getSymbols(self, set: ghidra.program.model.address.AddressSetView, type: ghidra.program.model.symbol.SymbolType, forward: bool) -> ghidra.program.model.symbol.SymbolIterator:
        """
        Returns all the symbols of the given type within the given address set.
        @param set the address set in which to look for symbols of the given type
        @param type the SymbolType to look for.
        @param forward the direction within the addressSet to search
        """
        ...

    def getUserSymbols(self, addr: ghidra.program.model.address.Address) -> List[ghidra.program.model.symbol.Symbol]:
        """
        Returns an array of all user defined symbols at the given address
        @param addr the address at which to retrieve all user defined symbols.
        """
        ...

    def getVariableSymbol(self, name: unicode, function: ghidra.program.model.listing.Function) -> ghidra.program.model.symbol.Symbol:
        """
        Returns a symbol that is either a parameter or local variable.  There can be only
         one because these symbol types have a unique name requirement.
        @param name the naem of the variable.
        @param function the function to search.
        @return a parameter or local variable symbol with the given name.
        """
        ...

    def hasLabelHistory(self, addr: ghidra.program.model.address.Address) -> bool:
        """
        Return true if there is a history of label changes at the given address.
        @param addr the address to check for symbol history.
        """
        ...

    def hasSymbol(self, addr: ghidra.program.model.address.Address) -> bool:
        """
        Return true if there exists a symbol at the given address.
        @param addr address to check for an existing symbol
        @return true if any symbol exists
        """
        ...

    def hashCode(self) -> int: ...

    def isExternalEntryPoint(self, addr: ghidra.program.model.address.Address) -> bool:
        """
        Returns true if the given address has been set as an external entry point.
        @param addr address to test for external entry point.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeExternalEntryPoint(self, addr: ghidra.program.model.address.Address) -> None:
        """
        Removes the given address as an external entry point.
        @param addr the address to remove as an external entry point.
        """
        ...

    def removeSymbolSpecial(self, sym: ghidra.program.model.symbol.Symbol) -> bool:
        """
        Removes the specified symbol from the symbol table.  If removing any <b>non-function</b>
         symbol the behavior will be the same as invoking {@link Symbol#delete()} on the
         symbol.  Use of this method for non-function symbols is discouraged.
         <p>
         <b>WARNING!</b> If removing a function symbol the behavior differs from directly
         invoking {@link Symbol#delete()} on the function symbol.
         <p>
         When removing a function symbol this method has the following behavior:
         <ul>
         <li>If the function is a default symbol (e.g., FUN_12345678) this method
         has no affect and will return null</li>
         <li>otherwise if another label exists at the function entry point, that
         label will be removed and the function will be renamed with that labels name</li>
         <li>If no other labels exist at the function entry, the function will
         be renamed to the default function name</li>
         </ul>
         Any reference bound to a symbol removed will loose that
         symbol specific binding.
        @param sym the symbol to be removed.
        @return false, if removal of the symbol fails
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
    def classNamespaces(self) -> java.util.Iterator: ...

    @property
    def definedSymbols(self) -> ghidra.program.model.symbol.SymbolIterator: ...

    @property
    def externalEntryPointIterator(self) -> ghidra.program.model.address.AddressIterator: ...

    @property
    def externalSymbols(self) -> ghidra.program.model.symbol.SymbolIterator: ...

    @property
    def labelHistory(self) -> java.util.Iterator: ...

    @property
    def numSymbols(self) -> int: ...

    @property
    def symbolIterator(self) -> ghidra.program.model.symbol.SymbolIterator: ...
