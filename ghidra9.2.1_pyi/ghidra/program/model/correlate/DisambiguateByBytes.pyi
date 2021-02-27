from typing import List
import ghidra.program.model.correlate
import java.lang


class DisambiguateByBytes(object, ghidra.program.model.correlate.DisambiguateStrategy):
    """
    Attempt to disambiguate similar n-grams by hashing over all the bytes in their constituent instructions.
    """





    def __init__(self): ...



    def calcHashes(self, instHash: ghidra.program.model.correlate.InstructHash, matchSize: int, store: ghidra.program.model.correlate.HashStore) -> List[ghidra.program.model.correlate.Hash]: ...

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
