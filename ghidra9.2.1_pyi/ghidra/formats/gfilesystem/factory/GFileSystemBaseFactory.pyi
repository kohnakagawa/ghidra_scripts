import ghidra.app.util.bin
import ghidra.formats.gfilesystem
import ghidra.formats.gfilesystem.factory
import ghidra.util.task
import java.io
import java.lang


class GFileSystemBaseFactory(object, ghidra.formats.gfilesystem.factory.GFileSystemFactoryFull, ghidra.formats.gfilesystem.factory.GFileSystemProbeFull):
    """
    A GFileSystemFactory implementation that probes and creates instances of
     GFileSystemBase which use the legacy filesystem lifecycle pattern.

     For each operation, this factory will mint a new instance of a GFileSystemBase-derived
     fs, using its 3 param constructor, and call its isValid() or open().

     After an isValid() call, the newly minted filesystem instance is thrown away.

     This class requires special support in the FileSystemFactoryMgr to push
     the fsClass into each factory instance after it is constructed.
    """





    def __init__(self): ...



    def create(self, containerFSRL: ghidra.formats.gfilesystem.FSRL, targetFSRL: ghidra.formats.gfilesystem.FSRLRoot, byteProvider: ghidra.app.util.bin.ByteProvider, containerFile: java.io.File, fsService: ghidra.formats.gfilesystem.FileSystemService, monitor: ghidra.util.task.TaskMonitor) -> ghidra.formats.gfilesystem.GFileSystemBase: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def probe(self, containerFSRL: ghidra.formats.gfilesystem.FSRL, byteProvider: ghidra.app.util.bin.ByteProvider, containerFile: java.io.File, fsService: ghidra.formats.gfilesystem.FileSystemService, monitor: ghidra.util.task.TaskMonitor) -> bool: ...

    def setFileSystemClass(self, fsClass: java.lang.Class) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def fileSystemClass(self) -> None: ...  # No getter available.

    @fileSystemClass.setter
    def fileSystemClass(self, value: java.lang.Class) -> None: ...
