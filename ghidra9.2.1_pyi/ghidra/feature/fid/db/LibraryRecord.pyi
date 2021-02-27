import ghidra.program.model.lang
import java.lang


class LibraryRecord(object):




    def __init__(self, __a0: db.Record): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getGhidraCompilerSpecID(self) -> ghidra.program.model.lang.CompilerSpecID: ...

    def getGhidraLanguageID(self) -> ghidra.program.model.lang.LanguageID: ...

    def getGhidraLanguageMinorVersion(self) -> int: ...

    def getGhidraLanguageVersion(self) -> int: ...

    def getGhidraVersion(self) -> unicode: ...

    def getLibraryFamilyName(self) -> unicode: ...

    def getLibraryID(self) -> long: ...

    def getLibraryVariant(self) -> unicode: ...

    def getLibraryVersion(self) -> unicode: ...

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
    def ghidraCompilerSpecID(self) -> ghidra.program.model.lang.CompilerSpecID: ...

    @property
    def ghidraLanguageID(self) -> ghidra.program.model.lang.LanguageID: ...

    @property
    def ghidraLanguageMinorVersion(self) -> int: ...

    @property
    def ghidraLanguageVersion(self) -> int: ...

    @property
    def ghidraVersion(self) -> unicode: ...

    @property
    def libraryFamilyName(self) -> unicode: ...

    @property
    def libraryID(self) -> long: ...

    @property
    def libraryVariant(self) -> unicode: ...

    @property
    def libraryVersion(self) -> unicode: ...