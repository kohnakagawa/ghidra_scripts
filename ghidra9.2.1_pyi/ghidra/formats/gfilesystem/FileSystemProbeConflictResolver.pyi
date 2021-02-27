from typing import List
import ghidra.formats.gfilesystem.factory
import java.lang


class FileSystemProbeConflictResolver(object):
    """
    A callback interface used to choose which filesystem implementation to use when
     multiple filesystem types indicate that they can open a container file.

    """

    CHOOSEFIRST: ghidra.formats.gfilesystem.FileSystemProbeConflictResolver = ghidra.formats.gfilesystem.FileSystemProbeConflictResolver$1@4fccf8fd
    GUI_PICKER: ghidra.formats.gfilesystem.FileSystemProbeConflictResolver = ghidra.formats.gfilesystem.FileSystemProbeConflictResolver$2@3d18c125







    def chooseFSIR(self, __a0: List[object]) -> ghidra.formats.gfilesystem.factory.FileSystemInfoRec: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def resolveFSIR(self, __a0: List[object]) -> ghidra.formats.gfilesystem.factory.FileSystemInfoRec: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
