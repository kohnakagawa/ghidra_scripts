import ghidra.app.plugin.core.analysis
import ghidra.app.services
import ghidra.app.util.importer
import ghidra.framework.options
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class GnuDemanglerAnalyzer(ghidra.app.plugin.core.analysis.AbstractDemanglerAnalyzer):




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
