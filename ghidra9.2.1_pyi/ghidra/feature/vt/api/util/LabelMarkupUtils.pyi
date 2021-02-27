import ghidra.program.model.address
import ghidra.program.model.listing
import java.lang


class LabelMarkupUtils(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def removeAllLabels(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address) -> None: ...

    @staticmethod
    def removeDefaultLabels(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
