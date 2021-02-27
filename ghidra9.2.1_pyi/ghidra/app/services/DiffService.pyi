import ghidra.framework.model
import ghidra.program.model.listing
import java.lang


class DiffService(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def inProgress(self) -> bool: ...

    @overload
    def launchDiff(self, __a0: ghidra.framework.model.DomainFile) -> bool: ...

    @overload
    def launchDiff(self, __a0: ghidra.program.model.listing.Program) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
