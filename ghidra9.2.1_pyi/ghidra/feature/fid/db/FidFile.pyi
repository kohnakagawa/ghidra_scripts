import ghidra.feature.fid.db
import ghidra.program.model.lang
import java.lang


class FidFile(object, java.lang.Comparable):
    FID_PACKED_DATABASE_FILE_EXTENSION: unicode = u'.fidb'
    FID_RAW_DATABASE_FILE_EXTENSION: unicode = u'.fidbf'







    def canProcessLanguage(self, __a0: ghidra.program.model.lang.Language) -> bool: ...

    @overload
    def compareTo(self, __a0: ghidra.feature.fid.db.FidFile) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getBaseName(self) -> unicode: ...

    def getClass(self) -> java.lang.Class: ...

    def getFidDB(self, __a0: bool) -> ghidra.feature.fid.db.FidDB: ...

    def getName(self) -> unicode: ...

    def getPath(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def isActive(self) -> bool: ...

    def isInstalled(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setActive(self, __a0: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def active(self) -> bool: ...

    @active.setter
    def active(self, value: bool) -> None: ...

    @property
    def baseName(self) -> unicode: ...

    @property
    def installed(self) -> bool: ...

    @property
    def name(self) -> unicode: ...

    @property
    def path(self) -> unicode: ...