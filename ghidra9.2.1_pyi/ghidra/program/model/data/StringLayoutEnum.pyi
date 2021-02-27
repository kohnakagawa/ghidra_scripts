from typing import List
import ghidra.program.model.data
import java.lang


class StringLayoutEnum(java.lang.Enum):
    CHAR_SEQ: ghidra.program.model.data.StringLayoutEnum = char sequence
    FIXED_LEN: ghidra.program.model.data.StringLayoutEnum = fixed length
    NULL_TERMINATED_BOUNDED: ghidra.program.model.data.StringLayoutEnum = null-terminated & bounded
    NULL_TERMINATED_UNBOUNDED: ghidra.program.model.data.StringLayoutEnum = null-terminated & unbounded
    PASCAL_255: ghidra.program.model.data.StringLayoutEnum = pascal255
    PASCAL_64k: ghidra.program.model.data.StringLayoutEnum = pascal64k







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isFixedLen(self) -> bool: ...

    def isNullTerminated(self) -> bool: ...

    def isPascal(self) -> bool: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def shouldTrimTrailingNulls(self) -> bool: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.program.model.data.StringLayoutEnum: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.program.model.data.StringLayoutEnum]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def fixedLen(self) -> bool: ...

    @property
    def nullTerminated(self) -> bool: ...

    @property
    def pascal(self) -> bool: ...