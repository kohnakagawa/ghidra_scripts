from typing import List
import ghidra.framework.model
import java.lang


class DomainFileContext(object):
    """
    A context that provides information to actions about domain files that are selected in the tool
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFileCount(self) -> int:
        """
        Returns the count of selected files
        @return the count of selected files
        """
        ...

    def getSelectedFiles(self) -> List[ghidra.framework.model.DomainFile]:
        """
        The selected files or empty if no files are selected
        @return the files
        """
        ...

    def hashCode(self) -> int: ...

    def isInActiveProject(self) -> bool:
        """
        True if the current set of files is in the active project (false implies a non-active,
         read-only project)
        @return true if in the active project
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
    def fileCount(self) -> int: ...

    @property
    def inActiveProject(self) -> bool: ...

    @property
    def selectedFiles(self) -> List[object]: ...
