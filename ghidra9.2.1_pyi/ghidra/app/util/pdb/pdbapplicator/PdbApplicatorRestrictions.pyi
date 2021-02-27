from typing import List
import ghidra.app.util.pdb.pdbapplicator
import java.lang


class PdbApplicatorRestrictions(java.lang.Enum):
    DATA_TYPES_ONLY: ghidra.app.util.pdb.pdbapplicator.PdbApplicatorRestrictions = Data Types Only
    NONE: ghidra.app.util.pdb.pdbapplicator.PdbApplicatorRestrictions = None
    PUBLIC_SYMBOLS_ONLY: ghidra.app.util.pdb.pdbapplicator.PdbApplicatorRestrictions = Public Symbols Only







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
    def valueOf(__a0: unicode) -> ghidra.app.util.pdb.pdbapplicator.PdbApplicatorRestrictions: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.pdb.pdbapplicator.PdbApplicatorRestrictions]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
