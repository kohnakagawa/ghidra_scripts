import ghidra.app.util.datatype.microsoft
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.program.model.mem
import ghidra.program.model.scalar
import ghidra.program.model.symbol
import java.lang


class EHDataTypeUtilities(object):








    @staticmethod
    def createFunctionIfNeeded(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address) -> bool: ...

    @staticmethod
    def createPlateCommentIfNeeded(__a0: ghidra.program.model.listing.Program, __a1: unicode, __a2: unicode, __a3: unicode, __a4: ghidra.program.model.address.Address, __a5: ghidra.app.util.datatype.microsoft.DataApplyOptions) -> unicode: ...

    @overload
    @staticmethod
    def createSymbolIfNeeded(__a0: ghidra.program.model.listing.Program, __a1: unicode, __a2: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Symbol: ...

    @overload
    @staticmethod
    def createSymbolIfNeeded(__a0: ghidra.program.model.listing.Program, __a1: unicode, __a2: unicode, __a3: unicode, __a4: ghidra.program.model.address.Address, __a5: ghidra.app.util.datatype.microsoft.DataApplyOptions) -> ghidra.program.model.symbol.Symbol: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getAddress(__a0: ghidra.program.model.data.DataType, __a1: int, __a2: ghidra.program.model.mem.MemBuffer) -> ghidra.program.model.address.Address: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getComponentAddress(__a0: ghidra.program.model.data.DataType, __a1: int, __a2: ghidra.program.model.mem.MemBuffer) -> ghidra.program.model.address.Address: ...

    @staticmethod
    def getCount(__a0: ghidra.program.model.data.DataType, __a1: int, __a2: ghidra.program.model.mem.MemBuffer) -> int: ...

    @staticmethod
    def getEHStateValue(__a0: ghidra.program.model.data.DataType, __a1: int, __a2: ghidra.program.model.mem.MemBuffer) -> int: ...

    @staticmethod
    def getIntegerValue(__a0: ghidra.program.model.data.DataType, __a1: int, __a2: ghidra.program.model.mem.MemBuffer) -> int: ...

    @staticmethod
    def getScalarValue(__a0: ghidra.program.model.data.DataType, __a1: int, __a2: ghidra.program.model.mem.MemBuffer) -> ghidra.program.model.scalar.Scalar: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isValidAddress(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address) -> bool: ...

    @staticmethod
    def isValidForFunction(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
