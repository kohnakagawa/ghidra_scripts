from typing import List
import ghidra.graph.viewer.options
import java.lang


class RelayoutOption(java.lang.Enum):
    ALWAYS: ghidra.graph.viewer.options.RelayoutOption = Always
    BLOCK_MODEL_CHANGES: ghidra.graph.viewer.options.RelayoutOption = Block Model Changes Only
    NEVER: ghidra.graph.viewer.options.RelayoutOption = Never
    VERTEX_GROUPING_CHANGES: ghidra.graph.viewer.options.RelayoutOption = Vertex Grouping Changes Only







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
    def valueOf(__a0: unicode) -> ghidra.graph.viewer.options.RelayoutOption: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.graph.viewer.options.RelayoutOption]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
