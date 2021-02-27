import ghidra.app.plugin.core.reloc
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.reloc
import java.lang


class Elfx86_64bitRelocationFixupHandler(ghidra.app.plugin.core.reloc.RelocationFixupHandler):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def handlesProgram(self, __a0: ghidra.program.model.listing.Program) -> bool: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def process64BitRelocation(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.reloc.Relocation, __a2: ghidra.program.model.address.Address, __a3: ghidra.program.model.address.Address) -> bool: ...

    def processRelocation(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.reloc.Relocation, __a2: ghidra.program.model.address.Address, __a3: ghidra.program.model.address.Address) -> bool: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
