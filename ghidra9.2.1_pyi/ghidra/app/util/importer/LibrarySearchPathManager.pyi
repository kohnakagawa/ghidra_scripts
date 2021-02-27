from typing import List
import java.lang


class LibrarySearchPathManager(object):
    """
    A simple class for managing the library search path
     and avoiding duplicate directories.
    """

    CURRENT_DIRECTORY: unicode = u'.'



    def __init__(self): ...



    @staticmethod
    def addPath(path: unicode) -> bool:
        """
        Adds the specified path to the end of the path search list.
        @param path the path to add
        @return true if the path was appended, false if the path was a duplicate
        """
        ...

    @staticmethod
    def addPathAt(index: int, path: unicode) -> bool:
        """
        Adds the path at the specified index in path search list.
        @param path the path to add
        @return true if the path was appended, false if the path was a duplicate
        """
        ...

    @staticmethod
    def clear() -> None:
        """
        Clears all paths.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getLibraryPaths() -> List[unicode]:
        """
        Returns an array of directories to search for libraries
        @return an array of directories to search for libraries
        """
        ...

    @staticmethod
    def getLibraryPathsList() -> List[unicode]:
        """
        Returns an array of directories to search for libraries
        @return a list of directories to search for libraries
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def removePath(path: unicode) -> bool:
        """
        Removes the path from the path search list.
        @param path the path the remove
        @return true if the path was removed, false if the path did not exist
        """
        ...

    @staticmethod
    def reset() -> None:
        """
        Resets the library search path to match the system search paths.
        """
        ...

    @staticmethod
    def restoreLibraryPaths(paths: List[unicode]) -> None:
        """
        Call this to restore paths that were previously persisted.  If you really need to change
         the paths <b>for the entire JVM</b>, then call {@link #setLibraryPaths(String[])}.
        @param paths the paths to restore
        """
        ...

    @staticmethod
    def setLibraryPaths(paths: List[unicode]) -> None:
        """
        Sets the directories to search for libraries
        @param paths the new library search paths
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
