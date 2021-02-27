import docking.widgets.table
import ghidra.program.model.address
import ghidra.program.model.listing
import java.lang


class DisplayableAddress(docking.widgets.table.DisplayStringProvider, java.lang.Comparable, object):
    NO_ADDRESS: unicode = u'No Address'







    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address: ...

    def getClass(self) -> java.lang.Class: ...

    def getDisplayString(self) -> unicode: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

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
    def displayString(self) -> unicode: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...