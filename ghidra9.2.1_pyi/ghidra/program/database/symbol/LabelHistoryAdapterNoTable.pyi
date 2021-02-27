import ghidra.program.database.symbol
import java.lang


class LabelHistoryAdapterNoTable(ghidra.program.database.symbol.LabelHistoryAdapter):
    """
    Adapter needed when a Program is being opened read only and the label
     history table does not exist in the Program.
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
