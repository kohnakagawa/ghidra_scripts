import ghidra.app.util.demangler
import ghidra.feature.fid.service
import ghidra.program.model.listing
import java.lang


class NameVersions(object):
    demangledBaseName: unicode
    demangledFull: unicode
    demangledNoTemplate: unicode
    rawName: unicode
    similarName: unicode



    def __init__(self, __a0: unicode): ...



    @staticmethod
    def demangle(__a0: ghidra.program.model.listing.Program, __a1: unicode) -> ghidra.app.util.demangler.DemangledObject: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def generate(__a0: unicode, __a1: ghidra.program.model.listing.Program) -> ghidra.feature.fid.service.NameVersions: ...

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
