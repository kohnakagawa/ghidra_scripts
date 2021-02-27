import ghidra.app.analyzers
import ghidra.app.services
import ghidra.app.util.importer
import ghidra.framework.options
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class CoffArchiveAnalyzer(ghidra.app.analyzers.AbstractBinaryFormatAnalyzer):




    def __init__(self): ...



    def added(self, program: ghidra.program.model.listing.Program, set: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor, log: ghidra.app.util.importer.MessageLog) -> bool: ...

    def analysisEnded(self, program: ghidra.program.model.listing.Program) -> None: ...

    def canAnalyze(self, program: ghidra.program.model.listing.Program) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getAnalysisType(self) -> ghidra.app.services.AnalyzerType: ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultEnablement(self, program: ghidra.program.model.listing.Program) -> bool: ...

    def getDescription(self) -> unicode: ...

    def getName(self) -> unicode: ...

    def getPriority(self) -> ghidra.app.services.AnalysisPriority: ...

    def hashCode(self) -> int: ...

    def isPrototype(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def optionsChanged(self, options: ghidra.framework.options.Options, program: ghidra.program.model.listing.Program) -> None: ...

    def registerOptions(self, options: ghidra.framework.options.Options, program: ghidra.program.model.listing.Program) -> None: ...

    def removed(self, program: ghidra.program.model.listing.Program, set: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor, log: ghidra.app.util.importer.MessageLog) -> bool: ...

    def supportsOneTimeAnalysis(self) -> bool: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
