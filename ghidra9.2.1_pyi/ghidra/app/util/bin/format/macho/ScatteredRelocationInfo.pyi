from typing import List
import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.macho
import ghidra.program.model.data
import java.lang


class ScatteredRelocationInfo(ghidra.app.util.bin.format.macho.RelocationInfo):
    """
    Represents a scattered_relocation_info structure.
    """

    R_SCATTERED: int = -2147483648



    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    @staticmethod
    def createRelocationInfo(reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader) -> ghidra.app.util.bin.format.macho.RelocationInfo: ...

    @staticmethod
    def createScatteredRelocationInfo(reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader) -> ghidra.app.util.bin.format.macho.ScatteredRelocationInfo: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getLength(self) -> int: ...

    def getSymbolIndex(self) -> int: ...

    def getType(self) -> int: ...

    def getValue(self) -> int:
        """
        The address of the relocatable expression for the item in the file that
         needs to be updated if the address is changed. For relocatable
         expressions with the difference of two section addresses, the address
         from which to subtract (in mathematical terms, the minuend) is
         contained in the first relocation entry and the address to subtract (the
         subtrahend) is contained in the second relocation entry.
        @return
        """
        ...

    def hashCode(self) -> int: ...

    def isExternal(self) -> bool: ...

    def isPcRelocated(self) -> bool: ...

    def isScattered(self) -> bool:
        """
        Returns true this is a scattered relocation.
        @return true this is a scattered relocation
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    def toValues(self) -> List[long]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def scattered(self) -> bool: ...

    @property
    def value(self) -> int: ...
