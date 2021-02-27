import ghidra.program.model.address
import ghidra.program.model.listing
import java.lang


class AddressTranslator(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    def translate(self, address: ghidra.program.model.address.Address, primaryProgram: ghidra.program.model.listing.Program, program: ghidra.program.model.listing.Program) -> ghidra.program.model.address.Address: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
