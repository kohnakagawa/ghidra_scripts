import java.io
import java.lang


class RefdFile(object, java.io.Closeable):
    """
    A GFile along with a FileSystemRef to keep the filesystem pinned
     in memory.

     The caller is responsible for #close() this object, which releases
     the FilesystemRef.
    """

    file: ghidra.formats.gfilesystem.GFile
    fsRef: ghidra.formats.gfilesystem.FileSystemRef



    def __init__(self, fsRef: ghidra.formats.gfilesystem.FileSystemRef, file: ghidra.formats.gfilesystem.GFile): ...



    def close(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

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
