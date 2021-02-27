import ghidra.program.model.correlate
import ghidra.program.model.listing
import java.lang


class MnemonicHashCalculator(object, ghidra.program.model.correlate.HashCalculator):
    """
    Hash function hashing only the mnemonic of an individual Instruction
    """





    def __init__(self): ...



    def calcHash(self, startHash: int, inst: ghidra.program.model.listing.Instruction) -> int: ...

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
