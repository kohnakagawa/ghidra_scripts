from typing import List
import ghidra.app.util
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.symbol
import java.lang


class NamespaceUtils(object):
    """
    A class to hold utility methods for working with namespaces.


     Example string format:

         globalNamespace#DELIMITERchild1Namespace#DELIMITERchild2
         child1


     Assumptions for creating namespaces from a path string:

         All elements of a namespace path should be namespace symbols and not other
             symbol types.
         Absolute paths can optionally start with the global namespace.
         You can provide a relative path that will start at the given
             parent namespace (or global if there is no parent provided).
         You can provide a path that has as its first entry the name of the
             given parent.  In this case, the first entry will not be created,
             but rather the provided parent will be used.
         If you provide a path and a parent, but the first element of the
             path is the global namespace, then the global namespace will be
             used as the parent namespace and not the one that was provided.
         You cannot embed the global namespace in a path, but it can be at
             the root.

    """









    @staticmethod
    def convertNamespaceToClass(namespace: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.listing.GhidraClass:
        """
        Convert a namespace to a class by copying all namespace children into a newly created class
         and then removing the old namespace
        @param namespace namespace to be converted
        @return new class namespace
        @throws InvalidInputException if namespace was contained within a function and can not be
         			converted to a class
        """
        ...

    @overload
    @staticmethod
    def createNamespaceHierarchy(namespacePath: unicode, rootNamespace: ghidra.program.model.symbol.Namespace, program: ghidra.program.model.listing.Program, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.Namespace:
        """
        Takes a namespace path string and creates a namespace hierarchy to
         match that string.  This method ignores function namespaces so the path
         should not contain any function names.  If you want traverse down through
         functions, then use the version that also takes an address that is used to distinguish
         between multiple functions with the same name.
         <P>
         The root namespace can be a function.
        @param namespacePath The namespace name or path string to be parsed.
                 This value should not include a trailing symbol name, only namespace names.
        @param rootNamespace The parent namespace under which the desired
                 namespace or path resides.  If this value is null, then the
                 global namespace will be used. This namespace can be a function name;
        @param program The current program in which the desired namespace
                 resides.
        @param source the source type of the namespace
        @return The namespace that matches the given path.  This can be either an existing
                 namespace or a newly created one.
        @throws InvalidInputException If a given namespace name is in an
                 invalid format and this method attempts to create that
                 namespace, or if the namespace string contains the global
                 namespace name in a position other than the root.
        @see <a href="#assumptions">assumptions</a>
        """
        ...

    @overload
    @staticmethod
    def createNamespaceHierarchy(namespacePath: unicode, rootNamespace: ghidra.program.model.symbol.Namespace, program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.Namespace:
        """
        Takes a namespace path string and creates a namespace hierarchy to
         match that string.  This method allows function namespaces in the path
         and uses the given address to resolve functions with duplicate names.  When
         resolving down the namespace path, a function that matches a name will only
         be used if the given address is contained in the body of that function.

         <p>The root namespace can be a function.

         <p>If an address is passed, then the path can contain a function name provided the
         address is in the body of the function; otherwise the names must all be namespaces other
         than functions.
        @param namespacePath The namespace name or path string to be parsed
                 This value should not include a trailing symbol name, only namespace names
        @param rootNamespace The parent namespace under which the desired
                 namespace or path resides.  If this value is null, then the
                 global namespace will be used.
        @param program The current program in which the desired namespace
                 resides
        @param address the address used to resolve possible functions with duplicate names; may
                 be null
        @param source the source of the namespace
        @return The namespace that matches the given path.  This can be either an existing
                 namespace or a newly created one.
        @throws InvalidInputException If a given namespace name is in an
                 invalid format and this method attempts to create that
                 namespace, or if the namespace string contains the global
                 namespace name in a position other than the root.
        @see <a href="#assumptions">assumptions</a>
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getFirstNonFunctionNamespace(parent: ghidra.program.model.symbol.Namespace, namespaceName: unicode, program: ghidra.program.model.listing.Program) -> ghidra.program.model.symbol.Namespace:
        """
        Returns the first namespace with the given name and that is NOT a function that
         is within the parent namespace. (ie. the first namespace that is not tied to a program
         address)
        @param parent the parent namespace to search
        @param namespaceName the name of the namespace to find
        @param program the program to search.
        @return the first namespace that matches, or null if no match.
        """
        ...

    @staticmethod
    def getFunctionNamespaceAt(program: ghidra.program.model.listing.Program, symbolPath: ghidra.app.util.SymbolPath, address: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Namespace:
        """
        Returns the existing Function at the given address if its {@link SymbolPath} matches the
         given path
        @param program the program
        @param symbolPath the path of namespace
        @param address the address
        @return the namespace represented by the given path, or null if no such namespace exists
        """
        ...

    @staticmethod
    def getFunctionNamespaceContaining(program: ghidra.program.model.listing.Program, symbolPath: ghidra.app.util.SymbolPath, address: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Namespace:
        """
        Returns the existing Function containing the given address if its
         {@link SymbolPath} matches the given path
        @param program the program
        @param symbolPath the path of namespace
        @param address the address
        @return the namespace represented by the given path, or null if no such namespace exists
        """
        ...

    @staticmethod
    def getLibrary(namespace: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.listing.Library:
        """
        Get the library associated with the specified namespace
        @param namespace namespace
        @return associated library or null if not associated with a library
        """
        ...

    @staticmethod
    def getMatchingNamespaces(__a0: unicode, __a1: List[object], __a2: ghidra.program.model.listing.Program) -> List[object]: ...

    @staticmethod
    def getNamespaceByPath(program: ghidra.program.model.listing.Program, parent: ghidra.program.model.symbol.Namespace, pathString: unicode) -> List[ghidra.program.model.symbol.Namespace]:
        """
        Returns a list of namespaces that match the given path.  The path can be
         relative to the given root namespace or absolute if the path begins with
         the global namespace name.

         <P>Note: this path must only contain Namespace names and no other symbol types.
        @param program the program to search
        @param parent the namespace to use as the root for relative paths. If null, the
         		  global namespace will be used
        @param pathString the path to the desired namespace
        @return a list of namespaces that match the given path
        """
        ...

    @staticmethod
    def getNamespacePathWithoutLibrary(namespace: ghidra.program.model.symbol.Namespace) -> unicode:
        """
        Get the normal namespace path excluding any library name.  Global namespace will be
         returned as empty string, while other namespace paths will be returned with trailing ::
         suffix.
        @param namespace namespace
        @return namespace path excluding any library name
        """
        ...

    @staticmethod
    def getNamespaceQualifiedName(namespace: ghidra.program.model.symbol.Namespace, symbolName: unicode, excludeLibraryName: bool) -> unicode:
        """
        Get namespace qualified symbol name
        @param namespace namespace object
        @param symbolName name of symbol
        @param excludeLibraryName if true any library name will be excluded from path returned,
         otherwise it will be included
        @return namespace qualified symbol name
        """
        ...

    @staticmethod
    def getNamespacesByName(program: ghidra.program.model.listing.Program, parent: ghidra.program.model.symbol.Namespace, namespaceName: unicode) -> List[ghidra.program.model.symbol.Namespace]:
        """
        Returns a list of all namespaces with the given name in the parent namespace
        @param program the program to search
        @param parent the parent namespace from which to find all namespaces with the given name;
                if null, the global namespace will be used
        @param namespaceName the name of the namespaces to retrieve
        @return a list of all namespaces that match the given name in the given parent namespace.
        """
        ...

    @staticmethod
    def getNonFunctionNamespace(program: ghidra.program.model.listing.Program, symbolPath: ghidra.app.util.SymbolPath) -> ghidra.program.model.symbol.Namespace:
        """
        Finds the namespace for the given symbol path <b>that is not a function</b>
        @param program the program from which to get the namespace
        @param symbolPath the path of namespace names including the name of the desired namespace
        @return the namespace represented by the given path, or null if no such namespace exists or
                 the namespace is a function
        """
        ...

    @overload
    @staticmethod
    def getSymbols(symbolPath: unicode, program: ghidra.program.model.listing.Program) -> List[ghidra.program.model.symbol.Symbol]:
        """
        Returns a list of all symbols that match the given path. The path consists of a series
         of namespaces names separated by "::" followed by a label or function name.
        @param symbolPath the names of namespaces and symbol separated by "::".
        @param program the program to search
        @return the list of symbols that match the given
        """
        ...

    @overload
    @staticmethod
    def getSymbols(symbolPath: ghidra.app.util.SymbolPath, program: ghidra.program.model.listing.Program) -> List[ghidra.program.model.symbol.Symbol]:
        """
        Returns a list of Symbol that match the given symbolPath.
        @param symbolPath the symbol path that specifies a series of namespace and symbol names.
        @param program the program to search for symbols with the given path.
        @return a list of Symbol that match the given symbolPath.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def splitNamespacePath(path: unicode) -> List[unicode]:
        """
        Provide a standard method for splitting a symbol path into its
         various namespace and symbol name elements.  While the current implementation
         uses a very simplistic approach, this may be improved upon in the future
         to handle various grouping concepts.
        @param path symbol namespace path (path will be trimmed before parse)
        @return order list of namespace names
        @deprecated use SymbolPath instead
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
