import ghidra.app.util.bin.format.pdb2.pdbreader
import ghidra.app.util.pdb.pdbapplicator
import java.lang


class CompositeTypeApplier(ghidra.app.util.pdb.pdbapplicator.AbstractComplexTypeApplier):




    def __init__(self, __a0: ghidra.app.util.pdb.pdbapplicator.PdbApplicator, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractCompositeMsType): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getComplexApplier(__a0: ghidra.app.util.pdb.pdbapplicator.PdbApplicator, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber) -> ghidra.app.util.pdb.pdbapplicator.AbstractComplexTypeApplier: ...

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
