import ghidra.app.plugin.match
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class ExactInstructionsFunctionHasher(ghidra.app.plugin.match.AbstractFunctionHasher):
    INSTANCE: ghidra.app.plugin.match.ExactInstructionsFunctionHasher = ghidra.app.plugin.match.ExactInstructionsFunctionHasher@45d0f359







    def commonBitCount(self, __a0: ghidra.program.model.listing.Function, __a1: ghidra.program.model.listing.Function, __a2: ghidra.util.task.TaskMonitor) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hash(self, __a0: ghidra.program.model.listing.Function, __a1: ghidra.util.task.TaskMonitor) -> long: ...

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
