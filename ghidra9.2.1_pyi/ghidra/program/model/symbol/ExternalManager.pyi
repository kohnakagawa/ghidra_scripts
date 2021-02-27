from typing import List
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.symbol
import java.lang


class ExternalManager(object):
    """
    External manager interface. Defines methods for dealing with external programs and locations
     within those programs.
    """









    @overload
    def addExtFunction(self, extName: unicode, extLabel: unicode, extAddr: ghidra.program.model.address.Address, sourceType: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.ExternalLocation:
        """
        Get or create an external location associated with an library/file named extName
         and the label within that file specified by extLabel
        @param extName the external name
        @param extLabel the external label
        @param extAddr the external address
        @param sourceType the source type of this external library's symbol
        @return external location
        @throws InvalidInputException
        @throws DuplicateNameException
        """
        ...

    @overload
    def addExtFunction(self, extNamespace: ghidra.program.model.symbol.Namespace, extLabel: unicode, extAddr: ghidra.program.model.address.Address, sourceType: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.ExternalLocation:
        """
        Get or create an external function location associated with an library/file named extName
         and the label within that file specified by extLabel
        @param extNamespace the external namespace
        @param extLabel the external label
        @param extAddr the external address
        @param sourceType the source type of this external library's symbol
        @return external location
        @throws InvalidInputException
        @throws DuplicateNameException if another non-Library namespace has the same name
        """
        ...

    @overload
    def addExtFunction(self, extNamespace: ghidra.program.model.symbol.Namespace, extLabel: unicode, extAddr: ghidra.program.model.address.Address, sourceType: ghidra.program.model.symbol.SourceType, reuseExisting: bool) -> ghidra.program.model.symbol.ExternalLocation:
        """
        Get or create an external function location associated with an library/file named extName
         and the label within that file specified by extLabel
        @param extNamespace the external namespace
        @param extLabel the external label
        @param sourceType the source type of this external library's symbol
        @param reuseExisting if true, will return any existing matching location instead of
         creating a new one. If false, will prefer to create a new one as long as the specified
         address is not null and not used in an existing location.
        @return external location
        @throws InvalidInputException
        @throws DuplicateNameException if another non-Library namespace has the same name
        """
        ...

    @overload
    def addExtLocation(self, extName: unicode, extLabel: unicode, extAddr: ghidra.program.model.address.Address, sourceType: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.ExternalLocation:
        """
        Get or create an external location associated with an library/file named extName
         and the label within that file specified by extLabel
        @param extName the external name
        @param extLabel the external label
        @param extAddr the external address
        @param sourceType the source type of this external library's symbol
        @return external location
        @throws InvalidInputException
        @throws DuplicateNameException
        """
        ...

    @overload
    def addExtLocation(self, extNamespace: ghidra.program.model.symbol.Namespace, extLabel: unicode, extAddr: ghidra.program.model.address.Address, sourceType: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.ExternalLocation:
        """
        Get or create an external location in the indicated parent namespace with the specified name.
        @param extNamespace the external namespace
        @param extLabel the external label
        @param extAddr the external address
        @param sourceType the source type of this external library's symbol
        @return external location
        @throws InvalidInputException
        @throws DuplicateNameException
        """
        ...

    @overload
    def addExtLocation(self, extNamespace: ghidra.program.model.symbol.Namespace, extLabel: unicode, extAddr: ghidra.program.model.address.Address, sourceType: ghidra.program.model.symbol.SourceType, reuseExisting: bool) -> ghidra.program.model.symbol.ExternalLocation:
        """
        Get or create an external location in the indicated parent namespace with the specified name.
        @param extNamespace the external namespace
        @param extLabel the external label
        @param extAddr the external address
        @param sourceType the source type of this external library's symbol
        @param reuseExisting if true, this will return an existing matching external
         location instead of creating a new one.
        @return external location
        @throws InvalidInputException
        @throws DuplicateNameException
        """
        ...

    def addExternalLibraryName(self, name: unicode, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.listing.Library:
        """
        Adds a new external library name
        @param name the new library name to add.
        @param source the source of this external library
        @return library
        """
        ...

    def contains(self, libraryName: unicode) -> bool:
        """
        Determines if the indicated external library name is being managed (exists).
        @param libraryName the external library name
        @return true if the name is defined (whether it has a path or not).
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getExternalLibrary(self, name: unicode) -> ghidra.program.model.listing.Library:
        """
        Get the Library which corresponds to the specified name
        @param name name of library
        @return library or null if not found
        """
        ...

    def getExternalLibraryNames(self) -> List[unicode]:
        """
        Returns a list of all external names for which locations have been defined.
        """
        ...

    def getExternalLibraryPath(self, libraryName: unicode) -> unicode:
        """
        Returns the file pathname associated with an external name.
         Null is returned if either the external name does not exist or
         a pathname has not been set.
        @param libraryName external name
        """
        ...

    @overload
    def getExternalLocation(self, symbol: ghidra.program.model.symbol.Symbol) -> ghidra.program.model.symbol.ExternalLocation:
        """
        Returns the external location associated with the given external symbol
        @param symbol the external symbol.
        @return the external location or null
        """
        ...

    @overload
    def getExternalLocation(self, libraryName: unicode, label: unicode) -> ghidra.program.model.symbol.ExternalLocation:
        """
        Get an external location.
        @param libraryName the name of the library for which to get an external location
        @param label the name of the external location.
        @deprecated Use  {@link #getExternalLocations(String, String)} instead
        """
        ...

    @overload
    def getExternalLocation(self, namespace: ghidra.program.model.symbol.Namespace, label: unicode) -> ghidra.program.model.symbol.ExternalLocation:
        """
        Get an external location.
        @param namespace the namespace containing the external label.
        @param label the name of the external location.
        @deprecated Use {@link #getExternalLocations(Namespace, String)}
        """
        ...

    @overload
    def getExternalLocations(self, libraryName: unicode) -> ghidra.program.model.symbol.ExternalLocationIterator:
        """
        Get an iterator over all external locations associated with the specified
         externalName.
        @param libraryName the name of the library to get locations for
        @return external location iterator
        """
        ...

    @overload
    def getExternalLocations(self, memoryAddress: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.ExternalLocationIterator:
        """
        Get an iterator over all external locations which have been associated to
         the specified memory address
        @param memoryAddress
        @return external location iterator
        """
        ...

    @overload
    def getExternalLocations(self, libraryName: unicode, label: unicode) -> List[ghidra.program.model.symbol.ExternalLocation]:
        """
        Returns a list of External Locations matching the given label name in the given Library.
        @param libraryName the name of the library
        @param label the name of the label
        @return a list of External Locations matching the given label name in the given Library.
        """
        ...

    @overload
    def getExternalLocations(self, namespace: ghidra.program.model.symbol.Namespace, label: unicode) -> List[ghidra.program.model.symbol.ExternalLocation]:
        """
        Returns a list of External Locations matching the given label name in the given Namespace.
        @param namespace the Namespace to search
        @param label the name of the labels to search for.
        @return a list of External Locations matching the given label name in the given Namespace.
        """
        ...

    @overload
    def getUniqueExternalLocation(self, libraryName: unicode, label: unicode) -> ghidra.program.model.symbol.ExternalLocation:
        """
        Returns the unique external location associated with the given library name and label
        @param libraryName the library name
        @param label the label of the external location
        @return the unique external location or null
        """
        ...

    @overload
    def getUniqueExternalLocation(self, namespace: ghidra.program.model.symbol.Namespace, label: unicode) -> ghidra.program.model.symbol.ExternalLocation:
        """
        Returns the unique external location associated with the given namespace and label
        @param namespace the namespace
        @param label the label of the external location
        @return the unique external location or null
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeExternalLibrary(self, name: unicode) -> bool:
        """
        Removes external name if no associated ExternalLocation's exist
        @param name external name
        @return true if removed, false if unable to due to associated locations/references
        """
        ...

    def setExternalPath(self, libraryName: unicode, pathname: unicode, userDefined: bool) -> None:
        """
        Sets the file pathname associated with an existing external name.
        @param libraryName the name of the library to associate with a file.
        @param pathname the path to the program to be associated with the library name.
        @param userDefined true if the external path is being specified by the user
        """
        ...

    def toString(self) -> unicode: ...

    def updateExternalLibraryName(self, oldName: unicode, newName: unicode, source: ghidra.program.model.symbol.SourceType) -> None:
        """
        Change the name of an existing external name.
        @param oldName the old name of the external library name.
        @param newName the new name of the external library name.
        @param source the source of this external library
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def externalLibraryNames(self) -> List[unicode]: ...
