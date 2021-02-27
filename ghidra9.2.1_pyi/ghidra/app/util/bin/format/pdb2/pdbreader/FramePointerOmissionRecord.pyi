from typing import List
import ghidra.app.util.bin.format.pdb2.pdbreader
import java.lang


class FramePointerOmissionRecord(object):





    class FrameType(java.lang.Enum):
        FPO: ghidra.app.util.bin.format.pdb2.pdbreader.FramePointerOmissionRecord.FrameType = fpo
        NON_FPO: ghidra.app.util.bin.format.pdb2.pdbreader.FramePointerOmissionRecord.FrameType = std
        TRAP: ghidra.app.util.bin.format.pdb2.pdbreader.FramePointerOmissionRecord.FrameType = trap
        TSS: ghidra.app.util.bin.format.pdb2.pdbreader.FramePointerOmissionRecord.FrameType = tss
        label: unicode







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        @staticmethod
        def fromValue(__a0: int) -> ghidra.app.util.bin.format.pdb2.pdbreader.FramePointerOmissionRecord.FrameType: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pdb2.pdbreader.FramePointerOmissionRecord.FrameType: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.app.util.bin.format.pdb2.pdbreader.FramePointerOmissionRecord.FrameType]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self): ...



    def EBPAllocatedAndUsed(self) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFirstFunctionByteOffset(self) -> long: ...

    def getFrameType(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.FramePointerOmissionRecord.FrameType: ...

    def getNumberFunctionPrologBytes(self) -> int: ...

    def getNumberLocalVariables(self) -> long: ...

    def getNumberOfFunctionBytes(self) -> long: ...

    def getSizeOfParametersInDwords(self) -> int: ...

    def hasStructuredExceptionHandling(self) -> bool: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def parse(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader) -> None: ...

    def reserved(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def firstFunctionByteOffset(self) -> long: ...

    @property
    def frameType(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.FramePointerOmissionRecord.FrameType: ...

    @property
    def numberFunctionPrologBytes(self) -> int: ...

    @property
    def numberLocalVariables(self) -> long: ...

    @property
    def numberOfFunctionBytes(self) -> long: ...

    @property
    def sizeOfParametersInDwords(self) -> int: ...