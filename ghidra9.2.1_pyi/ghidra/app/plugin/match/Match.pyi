from typing import List
import ghidra.app.plugin.match
import ghidra.program.model.address
import ghidra.program.model.listing
import java.lang


class Match(object, java.lang.Comparable):




    @overload
    def __init__(self, __a0: ghidra.program.model.address.Address, __a1: ghidra.program.model.address.Address, __a2: List[int], __a3: int): ...

    @overload
    def __init__(self, __a0: ghidra.program.model.address.Address, __a1: ghidra.program.model.address.Address, __a2: List[ghidra.program.model.listing.CodeUnit], __a3: List[ghidra.program.model.listing.CodeUnit], __a4: int): ...



    @overload
    def compareTo(self, __a0: ghidra.app.plugin.match.Match) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    @overload
    def continueMatch(self, __a0: int) -> None: ...

    @overload
    def continueMatch(self, __a0: ghidra.program.model.listing.CodeUnit, __a1: ghidra.program.model.listing.CodeUnit) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def expectedAddressForNextMatch(self, __a0: int) -> ghidra.program.model.address.Address: ...

    def getBytes(self) -> List[object]: ...

    def getClass(self) -> java.lang.Class: ...

    def getOtherBeginning(self) -> ghidra.program.model.address.Address: ...

    def getOtherBytes(self) -> List[object]: ...

    def getThisBeginning(self) -> ghidra.program.model.address.Address: ...

    def hashCode(self) -> int: ...

    def length(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def printMatch(self) -> unicode: ...

    def toString(self) -> unicode: ...

    def totalLength(self) -> int: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def bytes(self) -> List[object]: ...

    @property
    def otherBeginning(self) -> ghidra.program.model.address.Address: ...

    @property
    def otherBytes(self) -> List[object]: ...

    @property
    def thisBeginning(self) -> ghidra.program.model.address.Address: ...
