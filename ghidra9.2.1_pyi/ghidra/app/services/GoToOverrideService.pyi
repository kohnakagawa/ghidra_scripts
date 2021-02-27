import ghidra.program.model.address
import ghidra.program.util
import java.lang
import javax.swing


class GoToOverrideService(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getOverrideComponent(self) -> javax.swing.JComponent: ...

    @overload
    def goTo(self, queryInput: unicode) -> ghidra.program.util.ProgramLocation: ...

    @overload
    def goTo(self, gotoAddress: ghidra.program.model.address.Address) -> ghidra.program.util.ProgramLocation: ...

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
    def overrideComponent(self) -> javax.swing.JComponent: ...
