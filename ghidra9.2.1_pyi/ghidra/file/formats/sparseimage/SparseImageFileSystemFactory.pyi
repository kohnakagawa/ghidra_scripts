import ghidra.app.util.bin
import ghidra.formats.gfilesystem
import ghidra.formats.gfilesystem.factory
import ghidra.util.task
import java.io
import java.lang


class SparseImageFileSystemFactory(object, ghidra.formats.gfilesystem.factory.GFileSystemFactoryWithFile, ghidra.formats.gfilesystem.factory.GFileSystemProbeFull):




    def __init__(self): ...



    def create(self, __a0: ghidra.formats.gfilesystem.FSRL, __a1: ghidra.formats.gfilesystem.FSRLRoot, __a2: java.io.File, __a3: ghidra.formats.gfilesystem.FileSystemService, __a4: ghidra.util.task.TaskMonitor) -> ghidra.formats.gfilesystem.GFileSystem: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def probe(self, __a0: ghidra.formats.gfilesystem.FSRL, __a1: ghidra.app.util.bin.ByteProvider, __a2: java.io.File, __a3: ghidra.formats.gfilesystem.FileSystemService, __a4: ghidra.util.task.TaskMonitor) -> bool: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
