from typing import List
import ghidra.app.util.bin.format.coff
import ghidra.program.model.data
import java.lang


class AoutHeaderMIPS(ghidra.app.util.bin.format.coff.AoutHeader):
    SIZEOF: int = 56







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCprMask(self) -> List[int]:
        """
        Returns the co-processor register masks.
        @return the co-processor register masks
        """
        ...

    def getEntry(self) -> int: ...

    def getGpValue(self) -> int:
        """
        Returns the GP value.
        @return the GP value
        """
        ...

    def getGprMask(self) -> int:
        """
        Returns the general purpose register mask.
        @return the general purpose register mask
        """
        ...

    def getInitializedDataSize(self) -> int: ...

    def getInitializedDataStart(self) -> int: ...

    def getMagic(self) -> int: ...

    def getTextSize(self) -> int: ...

    def getTextStart(self) -> int: ...

    def getUninitializedDataSize(self) -> int: ...

    def getUnitializedDataStart(self) -> int: ...

    def getVersionStamp(self) -> int: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def cprMask(self) -> List[int]: ...

    @property
    def gpValue(self) -> int: ...

    @property
    def gprMask(self) -> int: ...

    @property
    def unitializedDataStart(self) -> int: ...
