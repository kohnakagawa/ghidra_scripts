import ghidra.formats.gfilesystem.factory
import java.lang


class GFileSystemFactoryIgnore(object, ghidra.formats.gfilesystem.factory.GFileSystemFactory):
    """
    Marker class that tells the FileSystemFactoryMgr to not register this
     filesystem instance.
    """





    def __init__(self): ...



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
