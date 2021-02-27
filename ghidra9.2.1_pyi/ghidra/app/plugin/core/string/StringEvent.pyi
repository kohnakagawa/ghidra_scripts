import ghidra.app.plugin.core.string
import ghidra.program.model.address
import java.lang


class StringEvent(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getMaxAddress(self, __a0: ghidra.program.model.address.Address, __a1: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address: ...

    def getMinAddress(self, __a0: ghidra.program.model.address.Address, __a1: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def process(self, __a0: ghidra.app.plugin.core.string.StringTableModel, __a1: ghidra.app.plugin.core.string.StringTableOptions) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
