from typing import List
import ghidra.feature.fid.db
import java.lang


class RelationType(java.lang.Enum):
    DIRECT_CALL: ghidra.feature.fid.db.RelationType = DIRECT_CALL
    INTER_LIBRARY_CALL: ghidra.feature.fid.db.RelationType = INTER_LIBRARY_CALL
    INTRA_LIBRARY_CALL: ghidra.feature.fid.db.RelationType = INTRA_LIBRARY_CALL







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

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
    def valueOf(__a0: unicode) -> ghidra.feature.fid.db.RelationType: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.feature.fid.db.RelationType]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
