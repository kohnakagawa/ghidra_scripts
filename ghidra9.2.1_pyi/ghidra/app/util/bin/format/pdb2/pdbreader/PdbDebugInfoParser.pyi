import ghidra.app.util.bin.format.pdb2.pdbreader
import java.lang


class PdbDebugInfoParser(object):
    DBI110_ID: int = 20091201
    DBI41_ID: int = 930803
    DBI50_ID: int = 19960307
    DBI60_ID: int = 19970606
    DBI70_ID: int = 19990903
    DBIHDR700_SIG: int = -1



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def parse(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb) -> ghidra.app.util.bin.format.pdb2.pdbreader.PdbDebugInfo: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
