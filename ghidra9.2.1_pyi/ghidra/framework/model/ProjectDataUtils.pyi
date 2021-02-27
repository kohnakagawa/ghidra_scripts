from typing import Iterator
import ghidra.framework.model
import java.lang
import java.util
import java.util.function


class ProjectDataUtils(object):





    class DomainFileIterator(object, java.util.Iterator):




        @overload
        def __init__(self, __a0: ghidra.framework.model.DomainFolder): ...

        @overload
        def __init__(self, __a0: ghidra.framework.model.Project): ...

        def __iter__(self) -> Iterator[object]: ...

        def equals(self, __a0: object) -> bool: ...

        def forEachRemaining(self, __a0: java.util.function.Consumer) -> None: ...

        def getClass(self) -> java.lang.Class: ...

        def hasNext(self) -> bool: ...

        def hashCode(self) -> int: ...

        def next(self) -> object: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def remove(self) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class DomainFolderIterator(object, java.util.Iterator):




        @overload
        def __init__(self, __a0: ghidra.framework.model.DomainFolder): ...

        @overload
        def __init__(self, __a0: ghidra.framework.model.Project): ...

        def __iter__(self) -> Iterator[object]: ...

        def equals(self, __a0: object) -> bool: ...

        def forEachRemaining(self, __a0: java.util.function.Consumer) -> None: ...

        def getClass(self) -> java.lang.Class: ...

        def hasNext(self) -> bool: ...

        def hashCode(self) -> int: ...

        def next(self) -> object: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def remove(self) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self): ...



    @staticmethod
    def createDomainFolderPath(currentFolder: ghidra.framework.model.DomainFolder, path: unicode) -> ghidra.framework.model.DomainFolder:
        """
        Returns a Ghidra {@link DomainFolder} with the matching path, creating
         any missing parent folders as needed.
         <p>
        @param currentFolder starting {@link DomainFolder}.
        @param path relative path to the desired DomainFolder, using forward slashes
         as separators.  Empty string ok, multiple slashes in a row treated as single slash,
         trailing slashes ignored.
        @return {@link DomainFolder} that the path points to.
        @throws InvalidNameException if bad name
        @throws IOException if problem when creating folder
        """
        ...

    @staticmethod
    def descendantFiles(folder: ghidra.framework.model.DomainFolder) -> java.lang.Iterable:
        """
        Returns a {@link Iterable} sequence of all the {@link DomainFile}s that exist under
         the specified {@link DomainFolder folder}.
        @param folder
        @return
        """
        ...

    @staticmethod
    def descendantFolders(folder: ghidra.framework.model.DomainFolder) -> java.lang.Iterable:
        """
        Returns a {@link Iterable} sequence of all the {@link DomainFolder}s that exist under
         the specified {@link DomainFolder folder}.
        @param folder
        @return
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getUniqueName(folder: ghidra.framework.model.DomainFolder, baseName: unicode) -> unicode:
        """
        Returns a unique name in a Ghidra {@link DomainFolder}.
        @param folder {@link DomainFolder} to check for child name collisions.
        @param baseName String base name of the file or folder
        @return "baseName" if no collisions, or "baseNameNNN" (where NNN is an incrementing
         integer value) when collisions are found, or null if there are more than 1000 collisions.
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def lookupDomainPath(currentFolder: ghidra.framework.model.DomainFolder, path: unicode) -> ghidra.framework.model.DomainFolder:
        """
        Returns a Ghidra {@link DomainFolder} with the matching path, or null if not found.
         <p>
        @param currentFolder starting {@link DomainFolder}.
        @param path relative path to the desired DomainFolder, using forward slashes
         as separators.  Empty string ok, multiple slashes in a row treated as single slash,
         trailing slashes ignored.
        @return {@link DomainFolder} that the path points to or null if not found.
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
