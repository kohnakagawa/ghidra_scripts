import ghidra.app.util.importer
import ghidra.app.util.pdb.pdbapplicator
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class PdbApplicator(object):




    def __init__(self, __a0: unicode, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb): ...



    def applyTo(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.data.DataTypeManager, __a2: ghidra.program.model.address.Address, __a3: ghidra.app.util.pdb.pdbapplicator.PdbApplicatorOptions, __a4: ghidra.util.task.TaskMonitor, __a5: ghidra.app.util.importer.MessageLog) -> None: ...

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
