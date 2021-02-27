import ghidra.app.plugin.core.searchtext.databasesearcher
import ghidra.program.model.address
import ghidra.program.util
import java.lang


class DataMnemonicOperandFieldSearcher(ghidra.app.plugin.core.searchtext.databasesearcher.ProgramDatabaseFieldSearcher):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getMatch(self) -> ghidra.program.util.ProgramLocation: ...

    def getNextSignificantAddress(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address: ...

    def hasMatch(self, __a0: ghidra.program.model.address.Address) -> bool: ...

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
