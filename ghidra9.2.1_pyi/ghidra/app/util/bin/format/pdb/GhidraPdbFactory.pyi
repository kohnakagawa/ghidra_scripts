import ghidra.app.util.bin
import ghidra.app.util.bin.format.pdb
import java.lang


class GhidraPdbFactory(ghidra.app.util.bin.format.pdb.PdbFactory):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getPdbInfoDotNetInstance(__a0: ghidra.app.util.bin.BinaryReader, __a1: int) -> ghidra.app.util.bin.format.pdb.PdbInfoDotNetIface: ...

    @staticmethod
    def getPdbInfoInstance(__a0: ghidra.app.util.bin.BinaryReader, __a1: int) -> ghidra.app.util.bin.format.pdb.PdbInfoIface: ...

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
