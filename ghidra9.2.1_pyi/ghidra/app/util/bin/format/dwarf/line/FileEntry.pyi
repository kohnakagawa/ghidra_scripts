import ghidra.app.util.bin.format.dwarf.line
import java.lang


class FileEntry(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDirectoryIndex(self) -> ghidra.app.util.bin.format.dwarf.line.LEB128: ...

    def getFileLengthInBytes(self) -> ghidra.app.util.bin.format.dwarf.line.LEB128: ...

    def getFileName(self) -> unicode: ...

    def getLastModifiedTime(self) -> ghidra.app.util.bin.format.dwarf.line.LEB128: ...

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
    def directoryIndex(self) -> ghidra.app.util.bin.format.dwarf.line.LEB128: ...

    @property
    def fileLengthInBytes(self) -> ghidra.app.util.bin.format.dwarf.line.LEB128: ...

    @property
    def fileName(self) -> unicode: ...

    @property
    def lastModifiedTime(self) -> ghidra.app.util.bin.format.dwarf.line.LEB128: ...
