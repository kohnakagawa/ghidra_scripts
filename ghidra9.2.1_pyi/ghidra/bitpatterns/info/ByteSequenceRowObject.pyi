from typing import List
import ghidra.bitpatterns.info
import ghidra.util.bytesearch
import java.lang


class ByteSequenceRowObject(object):




    def __init__(self, __a0: unicode, __a1: unicode, __a2: int, __a3: float): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDisassembly(self) -> unicode: ...

    @staticmethod
    def getFilteredRowObjects(__a0: List[object], __a1: ghidra.bitpatterns.info.PatternType, __a2: ghidra.bitpatterns.info.ContextRegisterFilter, __a3: ghidra.bitpatterns.info.ByteSequenceLengthFilter) -> List[object]: ...

    def getNumOccurrences(self) -> int: ...

    def getPercentage(self) -> float: ...

    @staticmethod
    def getRowObjectsFromInstructionSequences(__a0: List[object], __a1: ghidra.bitpatterns.info.InstructionSequenceTreePathFilter, __a2: ghidra.bitpatterns.info.ContextRegisterFilter) -> List[object]: ...

    def getSequence(self) -> unicode: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def merge(__a0: List[object]) -> ghidra.util.bytesearch.DittedBitSequence: ...

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
    def disassembly(self) -> unicode: ...

    @property
    def numOccurrences(self) -> int: ...

    @property
    def percentage(self) -> float: ...

    @property
    def sequence(self) -> unicode: ...
