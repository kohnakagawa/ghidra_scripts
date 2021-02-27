import ghidra.app.util.bin.format.pdb2.pdbreader
import java.lang


class MsTypeField(ghidra.app.util.bin.format.pdb2.pdbreader.IdMsParsable, object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getPdbId(self) -> int: ...

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
    def pdbId(self) -> int: ...
