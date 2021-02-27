from typing import List
import ghidra.app.plugin.core.string
import ghidra.app.services
import ghidra.app.util.importer
import ghidra.framework.options
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class StringsAnalyzer(ghidra.app.services.AbstractAnalyzer):





    class MinStringLen(java.lang.Enum):
        LEN_10: ghidra.app.plugin.core.string.StringsAnalyzer.MinStringLen = LEN_10
        LEN_11: ghidra.app.plugin.core.string.StringsAnalyzer.MinStringLen = LEN_11
        LEN_12: ghidra.app.plugin.core.string.StringsAnalyzer.MinStringLen = LEN_12
        LEN_13: ghidra.app.plugin.core.string.StringsAnalyzer.MinStringLen = LEN_13
        LEN_14: ghidra.app.plugin.core.string.StringsAnalyzer.MinStringLen = LEN_14
        LEN_15: ghidra.app.plugin.core.string.StringsAnalyzer.MinStringLen = LEN_15
        LEN_16: ghidra.app.plugin.core.string.StringsAnalyzer.MinStringLen = LEN_16
        LEN_17: ghidra.app.plugin.core.string.StringsAnalyzer.MinStringLen = LEN_17
        LEN_18: ghidra.app.plugin.core.string.StringsAnalyzer.MinStringLen = LEN_18
        LEN_19: ghidra.app.plugin.core.string.StringsAnalyzer.MinStringLen = LEN_19
        LEN_20: ghidra.app.plugin.core.string.StringsAnalyzer.MinStringLen = LEN_20
        LEN_21: ghidra.app.plugin.core.string.StringsAnalyzer.MinStringLen = LEN_21
        LEN_22: ghidra.app.plugin.core.string.StringsAnalyzer.MinStringLen = LEN_22
        LEN_23: ghidra.app.plugin.core.string.StringsAnalyzer.MinStringLen = LEN_23
        LEN_24: ghidra.app.plugin.core.string.StringsAnalyzer.MinStringLen = LEN_24
        LEN_25: ghidra.app.plugin.core.string.StringsAnalyzer.MinStringLen = LEN_25
        LEN_4: ghidra.app.plugin.core.string.StringsAnalyzer.MinStringLen = LEN_4
        LEN_5: ghidra.app.plugin.core.string.StringsAnalyzer.MinStringLen = LEN_5
        LEN_6: ghidra.app.plugin.core.string.StringsAnalyzer.MinStringLen = LEN_6
        LEN_7: ghidra.app.plugin.core.string.StringsAnalyzer.MinStringLen = LEN_7
        LEN_8: ghidra.app.plugin.core.string.StringsAnalyzer.MinStringLen = LEN_8
        LEN_9: ghidra.app.plugin.core.string.StringsAnalyzer.MinStringLen = LEN_9







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def getMinLength(self) -> int: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.app.plugin.core.string.StringsAnalyzer.MinStringLen: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.app.plugin.core.string.StringsAnalyzer.MinStringLen]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...

        @property
        def minLength(self) -> int: ...




    class Alignment(java.lang.Enum):
        ALIGN_1: ghidra.app.plugin.core.string.StringsAnalyzer.Alignment = ALIGN_1
        ALIGN_2: ghidra.app.plugin.core.string.StringsAnalyzer.Alignment = ALIGN_2
        ALIGN_4: ghidra.app.plugin.core.string.StringsAnalyzer.Alignment = ALIGN_4







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getAlignment(self) -> int: ...

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
        def valueOf(__a0: unicode) -> ghidra.app.plugin.core.string.StringsAnalyzer.Alignment: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.app.plugin.core.string.StringsAnalyzer.Alignment]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...

        @property
        def alignment(self) -> int: ...

    def __init__(self): ...



    def added(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.AddressSetView, __a2: ghidra.util.task.TaskMonitor, __a3: ghidra.app.util.importer.MessageLog) -> bool: ...

    def analysisEnded(self, __a0: ghidra.program.model.listing.Program) -> None: ...

    def canAnalyze(self, __a0: ghidra.program.model.listing.Program) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getAnalysisType(self) -> ghidra.app.services.AnalyzerType: ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultEnablement(self, __a0: ghidra.program.model.listing.Program) -> bool: ...

    def getDescription(self) -> unicode: ...

    def getName(self) -> unicode: ...

    def getPriority(self) -> ghidra.app.services.AnalysisPriority: ...

    def hashCode(self) -> int: ...

    def isPrototype(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def optionsChanged(self, __a0: ghidra.framework.options.Options, __a1: ghidra.program.model.listing.Program) -> None: ...

    def registerOptions(self, __a0: ghidra.framework.options.Options, __a1: ghidra.program.model.listing.Program) -> None: ...

    def removed(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.AddressSetView, __a2: ghidra.util.task.TaskMonitor, __a3: ghidra.app.util.importer.MessageLog) -> bool: ...

    def supportsOneTimeAnalysis(self) -> bool: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
