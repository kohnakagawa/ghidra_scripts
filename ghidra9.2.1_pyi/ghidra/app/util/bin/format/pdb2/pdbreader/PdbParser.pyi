import ghidra.app.util.bin.format.pdb2.pdbreader
import ghidra.util.task
import java.lang


class PdbParser(object):
    VC110_ID: int = 20091201
    VC140_ID: int = 20140508
    VC2_ID: int = 19941610
    VC41_ID: int = 19950814
    VC4_ID: int = 19950623
    VC50_ID: int = 19960307
    VC70DEP_ID: int = 19990604
    VC70_ID: int = 20000404
    VC80_ID: int = 20030901
    VC98_ID: int = 19970604



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def parse(__a0: unicode, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbReaderOptions, __a2: ghidra.util.task.TaskMonitor) -> ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
