from typing import List
import ghidra.feature.vt.gui.provider.functionassociation
import java.lang


class VTFunctionAssociationMode(java.lang.Enum):
    ALL: ghidra.feature.vt.gui.provider.functionassociation.VTFunctionAssociationMode = ALL
    Callee: ghidra.feature.vt.gui.provider.functionassociation.VTFunctionAssociationMode = Callee
    Caller: ghidra.feature.vt.gui.provider.functionassociation.VTFunctionAssociationMode = Caller
    NonMatched: ghidra.feature.vt.gui.provider.functionassociation.VTFunctionAssociationMode = NonMatched







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
    def valueOf(__a0: unicode) -> ghidra.feature.vt.gui.provider.functionassociation.VTFunctionAssociationMode: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.feature.vt.gui.provider.functionassociation.VTFunctionAssociationMode]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
