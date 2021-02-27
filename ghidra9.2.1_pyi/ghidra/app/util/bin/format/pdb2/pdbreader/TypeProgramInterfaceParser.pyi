import ghidra.app.util.bin.format.pdb2.pdbreader
import ghidra.util.task
import java.lang


class TypeProgramInterfaceParser(object):
    TI20_ID: int = 920924
    TI40_ID: int = 19950410
    TI41_ID: int = 19951122
    TI42_ID: int = 19951204
    TI50DEP_ID: int = 19960307
    TI50_ID: int = 19961031
    TI70_ID: int = 19990903
    TI80_ID: int = 20040203



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def parse(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: ghidra.util.task.TaskMonitor) -> ghidra.app.util.bin.format.pdb2.pdbreader.AbstractTypeProgramInterface: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
