import docking.widgets
import ghidra.program.util
import java.lang


class ProgramLocationListener(object):
    """
    Listener interface for when the program location changes.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def programLocationChanged(self, loc: ghidra.program.util.ProgramLocation, trigger: docking.widgets.EventTrigger) -> None:
        """
        Called whenever the program location changes.
        @param loc the new program location.
        @param trigger TODO
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
