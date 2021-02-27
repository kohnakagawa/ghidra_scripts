from typing import List
import ghidra.app.util
import ghidra.program.model.symbol
import java.lang


class SymbolPath(object, java.lang.Comparable):
    """
    A convenience object for parsing a namespace path to a symbol.

     For example, if a SymbolPath is constructed with "foo::bar::baz", then "baz" is the
     name of a symbol in the "bar" namespace, which is in the "foo" namespace.


     #getName() will return "baz".
     #getParentPath() will return "foo:bar".
     #getPath() will return "foo::bar::baz".

    """





    @overload
    def __init__(self, symbolPathString: unicode):
        """
        Construct a SymbolPath from a string containing NAMESPACE_DELIMITER ("::") sequences to
         separate the namespace names.  This is the only constructor that employs special
         string-based namespace parsing.
        @param symbolPathString the string to parse as a sequence of namespace names separated by
         "::".
        """
        ...

    @overload
    def __init__(self, symbolPath: List[unicode]):
        """
        Construct a SymbolPath from an array of strings where each string is the name of a namespace
         in the symbol path.
        @param symbolPath the array of names of namespaces.
        """
        ...

    @overload
    def __init__(self, symbol: ghidra.program.model.symbol.Symbol):
        """
        Constructs a new SymbolPath for the given symbol.
        @param symbol the symbol to get a SymbolPath for.
        """
        ...

    @overload
    def __init__(self, __a0: List[object]): ...

    @overload
    def __init__(self, symbol: ghidra.program.model.symbol.Symbol, excludeLibrary: bool):
        """
        Constructs a new SymbolPath for the given symbol with the option to exclude a beginning
         library name.
        @param symbol the symbol to get a SymbolPath for.
        @param excludeLibrary if true, any library name at the front of the path will be removed.
        """
        ...

    @overload
    def __init__(self, parent: ghidra.app.util.SymbolPath, name: unicode):
        """
        Creates a Symbol from a parent SymbolPath and a symbol name.
        @param parent the parent SymbolPath. Can be null if the name is in the global space.
        @param name the name of the symbol. This can't be null;
        """
        ...



    def append(self, path: ghidra.app.util.SymbolPath) -> ghidra.app.util.SymbolPath:
        """
        Creates a new SymbolPath composed of the list of names in this path followed by the
         list of names in the given path.
        @param path the path of names to append to this path.
        @return a new SymbolPath that appends the given path to this path.
        """
        ...

    def asArray(self) -> List[unicode]:
        """
        Returns an array of names of the symbols in the symbol path, starting with the name just
         below the global namespace.
        @return an array of names of the symbols in the symbol path.
        """
        ...

    def asList(self) -> List[unicode]:
        """
        Returns a list of names of the symbols in the symbol path, starting with the name just
         below the global namespace.
        @return a list of names of the symbols in the symbol path.
        """
        ...

    @overload
    def compareTo(self, o: ghidra.app.util.SymbolPath) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def containsPathEntry(self, text: unicode) -> bool:
        """
        Returns true if this path contains any path entry matching the given text
        @param text the text for which to search
        @return true if any path entry matches the given text
        """
        ...

    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode:
        """
        Returns the name of the symbol;
        @return the symbol name as string without any path information.
        """
        ...

    def getParent(self) -> ghidra.app.util.SymbolPath:
        """
        Returns the SymbolPath for the parent namespace or null if the parent is the global space.
        @return the SymbolPath for the parent namespace or null if the parent is the global space.
        """
        ...

    def getParentPath(self) -> unicode:
        """
        Returns null if the parent is null or global; otherwise returns the path as a string of the
         parent namespace path.
        @return the path of the parent namespace as string. Returns null if the parent is null or global.
        """
        ...

    def getPath(self) -> unicode:
        """
        Returns the full symbol path as a string.
        @return the SymbolPath for the complete name as string, including namespace.
        """
        ...

    def hashCode(self) -> int: ...

    def matchesPathOf(self, s: ghidra.program.model.symbol.Symbol) -> bool:
        """
        A convenience method to check if the given symbol's symbol path matches this path
        @param s the symbol to check
        @return true if the symbol paths match
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def replaceInvalidChars(self) -> ghidra.app.util.SymbolPath:
        """
        Returns a new SymbolPath in which invalid characters are replaced
         with underscores.
        @return the new SymbolPath with replaced characters.
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
    def name(self) -> unicode: ...

    @property
    def parent(self) -> ghidra.app.util.SymbolPath: ...

    @property
    def parentPath(self) -> unicode: ...

    @property
    def path(self) -> unicode: ...
