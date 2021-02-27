import ghidra.app.util.bin.format.dwarf4.next
import ghidra.program.model.listing
import ghidra.program.model.symbol
import java.lang


class NamespacePath(object, java.lang.Comparable):
    """
    Represents a hierarchical path of containers that hold names of objects.

     Each container of names (lets call them a namespace for short) can have a type that
     distinguishes it from other containers: classes, functions, c++ namespaces, etc.

     A NamespacePath does not correlate directly to a Ghidra Namespace, as a Ghidra Namespace
     is tied to a Program and has rules about what can be placed inside of it.

     NamespacePath instances can be created without referring to a Ghidra Program and without
     concern as to what will be valid or have collisions.

     Use a NamespacePath to represent and hold forward-engineering namespace nesting information (ie.
     namespace info recovered from debug info), and when a Ghidra Namespace is needed,
     convert to or lookup the live/'real' Ghidra Namespace.
    """

    ROOT: ghidra.app.util.bin.format.dwarf4.next.NamespacePath = ROOT(Namespace)







    def asCategoryPathString(self) -> unicode:
        """
        Converts this namespace path into a {@link CategoryPath} style string.
        @return string path "/namespace1/namespace2"
        """
        ...

    def asFormattedString(self) -> unicode:
        """
        Converts this namespace path into a {@link Namespace} style string without the ROOT namespace
         included.
        @return string path "namespace1::namespace2"
        """
        ...

    def asNamespaceString(self) -> unicode:
        """
        Converts this namespace path into a {@link Namespace} style string.
        @return string path "ROOT::namespace1::namespace2"
        """
        ...

    @overload
    def compareTo(self, otherPath: ghidra.app.util.bin.format.dwarf4.next.NamespacePath) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    @staticmethod
    def create(parent: ghidra.app.util.bin.format.dwarf4.next.NamespacePath, name: unicode, type: ghidra.program.model.symbol.SymbolType) -> ghidra.app.util.bin.format.dwarf4.next.NamespacePath:
        """
        Creates a new {@link NamespacePath} instance.
        @param parent optional - parent {@link NamespacePath} instance, default to {@link #ROOT} if null.
        @param name string name of the new namespace.
        @param type {@link SymbolType} of the named space - ie. a "namespace", a class,
        @return new {@link NamespacePath}
        """
        ...

    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode:
        """
        Returns the name of this namespace element, ie. the last thing on the path.
        @return string name.
        """
        ...

    def getNamespace(self, program: ghidra.program.model.listing.Program) -> ghidra.program.model.symbol.Namespace:
        """
        Converts this NamespacePath into a Ghidra {@link Namespace} in the specified {@link Program},
         creating missing elements on the path as necessary.
        @param program Ghidra {@link Program} where the namespace should be retrieved from or created in.
        @return {@link Namespace} or fallback to the progam's Global root namespace if problem.
        """
        ...

    def getParent(self) -> ghidra.app.util.bin.format.dwarf4.next.NamespacePath:
        """
        Returns a reference to the parent NamespacePath.
        @return parent NamespacePath
        """
        ...

    def getType(self) -> ghidra.program.model.symbol.SymbolType:
        """
        Returns the {@link SymbolType} of this namespace element (ie. the symbol type of the last
         thing on the path).
        @return {@link SymbolType}
        """
        ...

    def hashCode(self) -> int: ...

    def isRoot(self) -> bool:
        """
        Returns true if this namespace path points to the root of the namespace space.
        @return boolean true if ROOT
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
    def name(self) -> unicode: ...

    @property
    def parent(self) -> ghidra.app.util.bin.format.dwarf4.next.NamespacePath: ...

    @property
    def root(self) -> bool: ...

    @property
    def type(self) -> ghidra.program.model.symbol.SymbolType: ...
