from typing import List
import ghidra.feature.vt.api.main
import ghidra.feature.vt.gui.provider.relatedMatches
import java.lang


class VTRelatedMatchType(java.lang.Enum):
    CALLEE_MATCHES_CALLEE_ACCEPTED: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = CALLEE_MATCHES_CALLEE_ACCEPTED
    CALLEE_MATCHES_CALLEE_AVAILABLE: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = CALLEE_MATCHES_CALLEE_AVAILABLE
    CALLEE_MATCHES_CALLEE_LOCKED_OUT: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = CALLEE_MATCHES_CALLEE_LOCKED_OUT
    CALLEE_MATCHES_CALLER_ACCEPTED: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = CALLEE_MATCHES_CALLER_ACCEPTED
    CALLEE_MATCHES_CALLER_AVAILABLE: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = CALLEE_MATCHES_CALLER_AVAILABLE
    CALLEE_MATCHES_CALLER_LOCKED_OUT: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = CALLEE_MATCHES_CALLER_LOCKED_OUT
    CALLEE_MATCHES_TARGET_ACCEPTED: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = CALLEE_MATCHES_TARGET_ACCEPTED
    CALLEE_MATCHES_TARGET_AVAILABLE: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = CALLEE_MATCHES_TARGET_AVAILABLE
    CALLEE_MATCHES_TARGET_LOCKED_OUT: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = CALLEE_MATCHES_TARGET_LOCKED_OUT
    CALLEE_MATCHES_UNRELATED_ACCEPTED: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = CALLEE_MATCHES_UNRELATED_ACCEPTED
    CALLEE_MATCHES_UNRELATED_AVAILABLE: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = CALLEE_MATCHES_UNRELATED_AVAILABLE
    CALLEE_MATCHES_UNRELATED_LOCKED_OUT: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = CALLEE_MATCHES_UNRELATED_LOCKED_OUT
    CALLER_MATCHES_CALLEE_ACCEPTED: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = CALLER_MATCHES_CALLEE_ACCEPTED
    CALLER_MATCHES_CALLEE_AVAILABLE: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = CALLER_MATCHES_CALLEE_AVAILABLE
    CALLER_MATCHES_CALLEE_LOCKED_OUT: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = CALLER_MATCHES_CALLEE_LOCKED_OUT
    CALLER_MATCHES_CALLER_ACCEPTED: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = CALLER_MATCHES_CALLER_ACCEPTED
    CALLER_MATCHES_CALLER_AVAILABLE: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = CALLER_MATCHES_CALLER_AVAILABLE
    CALLER_MATCHES_CALLER_LOCKED_OUT: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = CALLER_MATCHES_CALLER_LOCKED_OUT
    CALLER_MATCHES_TARGET_ACCEPTED: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = CALLER_MATCHES_TARGET_ACCEPTED
    CALLER_MATCHES_TARGET_AVAILABLE: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = CALLER_MATCHES_TARGET_AVAILABLE
    CALLER_MATCHES_TARGET_LOCKED_OUT: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = CALLER_MATCHES_TARGET_LOCKED_OUT
    CALLER_MATCHES_UNRELATED_ACCEPTED: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = CALLER_MATCHES_UNRELATED_ACCEPTED
    CALLER_MATCHES_UNRELATED_AVAILABLE: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = CALLER_MATCHES_UNRELATED_AVAILABLE
    CALLER_MATCHES_UNRELATED_LOCKED_OUT: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = CALLER_MATCHES_UNRELATED_LOCKED_OUT
    TARGET_MATCHES_CALLEE_ACCEPTED: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = TARGET_MATCHES_CALLEE_ACCEPTED
    TARGET_MATCHES_CALLEE_AVAILABLE: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = TARGET_MATCHES_CALLEE_AVAILABLE
    TARGET_MATCHES_CALLEE_LOCKED_OUT: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = TARGET_MATCHES_CALLEE_LOCKED_OUT
    TARGET_MATCHES_CALLER_ACCEPTED: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = TARGET_MATCHES_CALLER_ACCEPTED
    TARGET_MATCHES_CALLER_AVAILABLE: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = TARGET_MATCHES_CALLER_AVAILABLE
    TARGET_MATCHES_CALLER_LOCKED_OUT: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = TARGET_MATCHES_CALLER_LOCKED_OUT
    TARGET_MATCHES_TARGET_ACCEPTED: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = TARGET_MATCHES_TARGET_ACCEPTED
    TARGET_MATCHES_TARGET_AVAILABLE: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = TARGET_MATCHES_TARGET_AVAILABLE
    TARGET_MATCHES_TARGET_LOCKED_OUT: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = TARGET_MATCHES_TARGET_LOCKED_OUT
    TARGET_MATCHES_UNRELATED_ACCEPTED: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = TARGET_MATCHES_UNRELATED_ACCEPTED
    TARGET_MATCHES_UNRELATED_AVAILABLE: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = TARGET_MATCHES_UNRELATED_AVAILABLE
    TARGET_MATCHES_UNRELATED_LOCKED_OUT: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = TARGET_MATCHES_UNRELATED_LOCKED_OUT
    UNRELATED_MATCHES_CALLEE_ACCEPTED: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = UNRELATED_MATCHES_CALLEE_ACCEPTED
    UNRELATED_MATCHES_CALLEE_AVAILABLE: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = UNRELATED_MATCHES_CALLEE_AVAILABLE
    UNRELATED_MATCHES_CALLEE_LOCKED_OUT: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = UNRELATED_MATCHES_CALLEE_LOCKED_OUT
    UNRELATED_MATCHES_CALLER_ACCEPTED: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = UNRELATED_MATCHES_CALLER_ACCEPTED
    UNRELATED_MATCHES_CALLER_AVAILABLE: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = UNRELATED_MATCHES_CALLER_AVAILABLE
    UNRELATED_MATCHES_CALLER_LOCKED_OUT: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = UNRELATED_MATCHES_CALLER_LOCKED_OUT
    UNRELATED_MATCHES_TARGET_ACCEPTED: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = UNRELATED_MATCHES_TARGET_ACCEPTED
    UNRELATED_MATCHES_TARGET_AVAILABLE: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = UNRELATED_MATCHES_TARGET_AVAILABLE
    UNRELATED_MATCHES_TARGET_LOCKED_OUT: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType = UNRELATED_MATCHES_TARGET_LOCKED_OUT







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def findMatchType(__a0: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchCorrelationType, __a1: ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchCorrelationType, __a2: ghidra.feature.vt.api.main.VTAssociationStatus) -> ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType: ...

    def getAssociationStatus(self) -> ghidra.feature.vt.api.main.VTAssociationStatus: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def getDestinationType(self) -> ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchCorrelationType: ...

    def getGoodness(self) -> int: ...

    def getSourceType(self) -> ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchCorrelationType: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchType]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def associationStatus(self) -> ghidra.feature.vt.api.main.VTAssociationStatus: ...

    @property
    def destinationType(self) -> ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchCorrelationType: ...

    @property
    def goodness(self) -> int: ...

    @property
    def sourceType(self) -> ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchCorrelationType: ...
