import ghidra.app.util.bin.format.pdb2.pdbreader
import ghidra.app.util.bin.format.pdb2.pdbreader.type
import java.lang


class EmptyTPI(ghidra.app.util.bin.format.pdb2.pdbreader.AbstractTypeProgramInterface):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getRecord(self, __a0: int) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractMsType: ...

    def getTypeIndexMaxExclusive(self) -> int: ...

    def getTypeIndexMin(self) -> int: ...

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
