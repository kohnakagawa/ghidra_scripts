import ghidra.app.util.bin.format.pdb2.pdbreader
import ghidra.app.util.bin.format.pdb2.pdbreader.msf
import ghidra.util.task
import java.lang


class MsfParser(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def parse(__a0: unicode, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbReaderOptions, __a2: ghidra.util.task.TaskMonitor) -> ghidra.app.util.bin.format.pdb2.pdbreader.msf.AbstractMsf: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
