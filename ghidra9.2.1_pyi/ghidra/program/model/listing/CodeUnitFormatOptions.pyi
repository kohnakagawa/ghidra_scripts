from typing import List
import ghidra.program.model.listing
import ghidra.program.model.listing.CodeUnitFormatOptions
import java.lang


class CodeUnitFormatOptions(object):





    class ShowNamespace(java.lang.Enum):
        ALWAYS: ghidra.program.model.listing.CodeUnitFormatOptions.ShowNamespace = ALWAYS
        LOCAL: ghidra.program.model.listing.CodeUnitFormatOptions.ShowNamespace = LOCAL
        NEVER: ghidra.program.model.listing.CodeUnitFormatOptions.ShowNamespace = NEVER
        NON_LOCAL: ghidra.program.model.listing.CodeUnitFormatOptions.ShowNamespace = NON_LOCAL







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
        def valueOf(__a0: unicode) -> ghidra.program.model.listing.CodeUnitFormatOptions.ShowNamespace: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.program.model.listing.CodeUnitFormatOptions.ShowNamespace]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class ShowBlockName(java.lang.Enum):
        ALWAYS: ghidra.program.model.listing.CodeUnitFormatOptions.ShowBlockName = ALWAYS
        NEVER: ghidra.program.model.listing.CodeUnitFormatOptions.ShowBlockName = NEVER
        NON_LOCAL: ghidra.program.model.listing.CodeUnitFormatOptions.ShowBlockName = NON_LOCAL







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
        def valueOf(__a0: unicode) -> ghidra.program.model.listing.CodeUnitFormatOptions.ShowBlockName: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.program.model.listing.CodeUnitFormatOptions.ShowBlockName]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    @overload
    def __init__(self): ...

    @overload
    def __init__(self, showBlockName: ghidra.program.model.listing.CodeUnitFormatOptions.ShowBlockName, showNamespace: ghidra.program.model.listing.CodeUnitFormatOptions.ShowNamespace):
        """
        Format options constructor using primarily default format options.
        @param showBlockName controls display of block name in address representations.
        @param showNamespace controls display of namespace path with label references.
        """
        ...

    @overload
    def __init__(self, showBlockName: ghidra.program.model.listing.CodeUnitFormatOptions.ShowBlockName, showNamespace: ghidra.program.model.listing.CodeUnitFormatOptions.ShowNamespace, localPrefixOverride: unicode, doRegVariableMarkup: bool, doStackVariableMarkup: bool, includeInferredVariableMarkup: bool, alwaysShowPrimaryReference: bool, includeScalarReferenceAdjustment: bool, showLibraryInNamespace: bool, followReferencedPointers: bool):
        """
        Format options constructor.  Extended reference mark-up is enabled.
        @param showBlockName controls display of block name in address representations.
        @param showNamespace controls display of namespace path with label references.
        @param localPrefixOverride optional override for local name-space when showNamespace
         is ShowNamespace.LOCAL or ShowNamespace.ALWAYS.  Specifying a null value
         will cause the actual name-space to be used.
        @param doRegVariableMarkup perform register variable/reference mark-up if true
        @param doStackVariableMarkup perform stack variable/reference mark-up if true
        @param includeInferredVariableMarkup if true and doRegVariableMarkup is also true, an attempt
         will be made to mark-up inferred register variable usage.
        @param alwaysShowPrimaryReference if true forces the primary reference to be rendered with
         the operand using the =&gt; separator if necessary
        @param includeScalarReferenceAdjustment if true scalar adjustment of certain reference offsets
         will be included to maintain replaced scalar value
        @param showLibraryInNamespace if true any referenced external symbols will include
         library name
        @param followReferencedPointers if true referenced pointers (read or indirect) will
         follow the pointer and display the indirect symbol with -&gt; instead of pointer label.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getShowBlockNameOption(self) -> ghidra.program.model.listing.CodeUnitFormatOptions.ShowBlockName:
        """
        Get current ShowBlockName option
        @return ShowBlockName option
        """
        ...

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
    def showBlockNameOption(self) -> ghidra.program.model.listing.CodeUnitFormatOptions.ShowBlockName: ...
