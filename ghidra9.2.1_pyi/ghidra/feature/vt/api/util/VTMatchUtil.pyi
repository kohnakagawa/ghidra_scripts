import ghidra.feature.vt.api.main
import ghidra.program.model.address
import java.lang


class VTMatchUtil(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getMatchAddresses(__a0: ghidra.feature.vt.api.main.VTMatch, __a1: bool) -> ghidra.program.model.address.AddressSetView: ...

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
