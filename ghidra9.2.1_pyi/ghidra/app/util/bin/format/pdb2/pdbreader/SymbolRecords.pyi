import ghidra.app.util.bin.format.pdb2.pdbreader
import ghidra.util.task
import java.lang
import java.util


class SymbolRecords(object):




    def __init__(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb): ...



    def deserializeSymbolRecords(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader, __a1: ghidra.util.task.TaskMonitor) -> java.util.Map: ...

    def equals(self, __a0: object) -> bool: ...

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
