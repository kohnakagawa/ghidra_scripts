from typing import List
import ghidra.app.plugin.core.datamgr.archive
import java.lang


class ArchiveProvider(object):
    """
    An interface to be implemented by any class that can return a list of Archives.
     For example, the tool's data type manager can return a list of archives within the project.
    """









    def equals(self, __a0: object) -> bool: ...

    def getArchives(self) -> List[ghidra.app.plugin.core.datamgr.archive.Archive]: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

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
    def archives(self) -> List[object]: ...
