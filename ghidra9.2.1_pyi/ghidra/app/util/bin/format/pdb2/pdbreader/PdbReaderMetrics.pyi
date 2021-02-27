import ghidra.app.util.bin.format.pdb2.pdbreader
import java.lang


class PdbReaderMetrics(object):




    def __init__(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getPostProcessingReport(self) -> unicode: ...

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

    def witnessDataTypeId(self, __a0: int) -> None: ...

    def witnessIpiDetection(self, __a0: bool, __a1: bool) -> None: ...

    def witnessPrimitive(self, __a0: int) -> None: ...

    def witnessRecordNumber(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber) -> None: ...

    def witnessSymbolTypeId(self, __a0: int) -> None: ...

    def witnessedSectionSegmentNumber(self, __a0: int) -> None: ...

    @property
    def postProcessingReport(self) -> unicode: ...
