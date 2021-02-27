import ghidra.program.database.function
import java.lang


class CallingConventionDBAdapterNoTable(ghidra.program.database.function.CallingConventionDBAdapter):
    """
    Adapter needed for a read-only version of Program that is not going
     to be upgraded, and there is no Calling Convention table in the Program.
    """





    def __init__(self): ...



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
