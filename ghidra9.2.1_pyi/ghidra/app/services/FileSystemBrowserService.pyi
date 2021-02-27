import ghidra.formats.gfilesystem
import java.lang


class FileSystemBrowserService(object):
    """
    A service to interact with file systems.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def openFileSystem(self, fsrl: ghidra.formats.gfilesystem.FSRL) -> None:
        """
        Opens the given {@link FSRL} in a file system browser.
        @param fsrl The thing to open in a file system browser.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
