from typing import List
import ghidra.program.model.listing
import ghidra.program.model.symbol
import java.lang


class FlowOverride(java.lang.Enum):
    BRANCH: ghidra.program.model.listing.FlowOverride = BRANCH
    CALL: ghidra.program.model.listing.FlowOverride = CALL
    CALL_RETURN: ghidra.program.model.listing.FlowOverride = CALL_RETURN
    NONE: ghidra.program.model.listing.FlowOverride = NONE
    RETURN: ghidra.program.model.listing.FlowOverride = RETURN







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    @staticmethod
    def getFlowOverride(__a0: int) -> ghidra.program.model.listing.FlowOverride: ...

    @staticmethod
    def getModifiedFlowType(__a0: ghidra.program.model.symbol.FlowType, __a1: ghidra.program.model.listing.FlowOverride) -> ghidra.program.model.symbol.FlowType: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.program.model.listing.FlowOverride: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.program.model.listing.FlowOverride]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
