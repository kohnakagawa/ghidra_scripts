from typing import List
import ghidra.app.util.bin.format.omf
import ghidra.formats.gfilesystem
import ghidra.util.task
import java.io
import java.lang
import java.util


class OmfArchiveFileSystem(object, ghidra.formats.gfilesystem.GFileSystem):




    def __init__(self, __a0: ghidra.formats.gfilesystem.FSRLRoot, __a1: ghidra.app.util.bin.ByteProvider): ...



    def close(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def getFSRL(self) -> ghidra.formats.gfilesystem.FSRLRoot: ...

    def getFileCount(self) -> int: ...

    def getInfo(self, __a0: ghidra.formats.gfilesystem.GFile, __a1: ghidra.util.task.TaskMonitor) -> unicode: ...

    def getInfoMap(self, __a0: ghidra.app.util.bin.format.omf.OmfLibraryRecord.MemberHeader) -> java.util.Map: ...

    def getInputStream(self, __a0: ghidra.formats.gfilesystem.GFile, __a1: ghidra.util.task.TaskMonitor) -> java.io.InputStream: ...

    def getListing(self, __a0: ghidra.formats.gfilesystem.GFile) -> List[object]: ...

    def getName(self) -> unicode: ...

    def getRefManager(self) -> ghidra.formats.gfilesystem.FileSystemRefManager: ...

    def getType(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def isClosed(self) -> bool: ...

    def isStatic(self) -> bool: ...

    def lookup(self, __a0: unicode) -> ghidra.formats.gfilesystem.GFile: ...

    def mount(self, __a0: ghidra.util.task.TaskMonitor) -> None: ...

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
    def FSRL(self) -> ghidra.formats.gfilesystem.FSRLRoot: ...

    @property
    def closed(self) -> bool: ...

    @property
    def description(self) -> unicode: ...

    @property
    def fileCount(self) -> int: ...

    @property
    def name(self) -> unicode: ...

    @property
    def refManager(self) -> ghidra.formats.gfilesystem.FileSystemRefManager: ...

    @property
    def static(self) -> bool: ...

    @property
    def type(self) -> unicode: ...
