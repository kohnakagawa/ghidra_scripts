import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.scalar
import java.lang


class ScalarRowObject(object):








    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address: ...

    def getClass(self) -> java.lang.Class: ...

    def getCodeUnit(self) -> ghidra.program.model.listing.CodeUnit: ...

    def getScalar(self) -> ghidra.program.model.scalar.Scalar: ...

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

    @property
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def codeUnit(self) -> ghidra.program.model.listing.CodeUnit: ...

    @property
    def scalar(self) -> ghidra.program.model.scalar.Scalar: ...
