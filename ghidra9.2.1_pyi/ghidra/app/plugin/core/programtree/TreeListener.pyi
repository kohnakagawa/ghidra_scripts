import ghidra.program.model.address
import java.lang
import javax.swing.event


class TreeListener(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def goTo(self, __a0: ghidra.program.model.address.Address) -> None: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    def treeViewChanged(self, __a0: javax.swing.event.ChangeEvent) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
