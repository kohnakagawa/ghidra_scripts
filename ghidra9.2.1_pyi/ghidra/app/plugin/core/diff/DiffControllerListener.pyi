import ghidra.app.plugin.core.diff
import ghidra.program.model.address
import java.lang


class DiffControllerListener(object):








    def diffLocationChanged(self, __a0: ghidra.app.plugin.core.diff.DiffController, __a1: ghidra.program.model.address.Address) -> None: ...

    def differencesChanged(self, __a0: ghidra.app.plugin.core.diff.DiffController) -> None: ...

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
