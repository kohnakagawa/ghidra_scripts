from typing import List
import ghidra.program.model.listing
import ghidra.program.model.listing.LabelString
import java.lang


class LabelString(object):
    CODE_LABEL: ghidra.program.model.listing.LabelString.LabelType = CODE_LABEL
    EXTERNAL: ghidra.program.model.listing.LabelString.LabelType = EXTERNAL
    VARIABLE: ghidra.program.model.listing.LabelString.LabelType = VARIABLE




    class LabelType(java.lang.Enum):
        CODE_LABEL: ghidra.program.model.listing.LabelString.LabelType = CODE_LABEL
        EXTERNAL: ghidra.program.model.listing.LabelString.LabelType = EXTERNAL
        VARIABLE: ghidra.program.model.listing.LabelString.LabelType = VARIABLE







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
        def valueOf(__a0: unicode) -> ghidra.program.model.listing.LabelString.LabelType: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.program.model.listing.LabelString.LabelType]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self, label: unicode, type: ghidra.program.model.listing.LabelString.LabelType): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLabelType(self) -> ghidra.program.model.listing.LabelString.LabelType: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def labelType(self) -> ghidra.program.model.listing.LabelString.LabelType: ...
