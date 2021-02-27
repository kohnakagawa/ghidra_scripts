import ghidra.app.services
import ghidra.app.util.importer
import ghidra.framework.options
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.classfinder
import ghidra.util.task
import java.lang


class Analyzer(ghidra.util.classfinder.ExtensionPoint, object):
    """
    NOTE:  ALL ANALYZER CLASSES MUST END IN "Analyzer".  If not,
     the ClassSearcher will not find them.

     Interface to perform automatic analysis.
    """









    def added(self, program: ghidra.program.model.listing.Program, set: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor, log: ghidra.app.util.importer.MessageLog) -> bool:
        """
        Called when the requested information type has been added.
         (ie: function added.)
        @param program program to analyze
        @param set AddressSet of locations that have been added
        @param monitor monitor that indicates progress and indicates whether
         the user canceled the analysis
        @param log a message log to record analysis information
        @return true if the analysis succeeded
        """
        ...

    def analysisEnded(self, program: ghidra.program.model.listing.Program) -> None:
        """
        Called when an auto-analysis session ends. This notifies the analyzer so it can clean up any
         resources that only needed to be maintained during a single auto-analysis session.
        @param program the program that was just completed being analyzed
        """
        ...

    def canAnalyze(self, program: ghidra.program.model.listing.Program) -> bool:
        """
        Can this analyzer work on this program.
        @param program program to be analyzed
        @return true if this analyzer can analyze this program
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAnalysisType(self) -> ghidra.app.services.AnalyzerType:
        """
        Get the type of analysis this analyzer performs
        @return analyze type
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultEnablement(self, program: ghidra.program.model.listing.Program) -> bool:
        """
        Returns true if this analyzer should be enabled by default.  Generally useful
         analyzers should return true. Specialized analyzers should return false;
        """
        ...

    def getDescription(self) -> unicode:
        """
        Get a longer description of what this analyzer does.
        @return analyzer description
        """
        ...

    def getName(self) -> unicode:
        """
        Get the name of this analyzer
        @return analyzer name
        """
        ...

    def getPriority(self) -> ghidra.app.services.AnalysisPriority:
        """
        Get the priority that this analyzer should run at.
        @return analyzer priority
        """
        ...

    def hashCode(self) -> int: ...

    def isPrototype(self) -> bool:
        """
        Returns true if this analyzer is a prototype.
        @return true if this analyzer is a prototype
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def optionsChanged(self, options: ghidra.framework.options.Options, program: ghidra.program.model.listing.Program) -> None:
        """
        Analyzers should initialize their options from the values in the given Options,
         providing appropriate default values.
        @param options the program options/property list that contains the options
        @param program program to be analyzed
        """
        ...

    def registerOptions(self, options: ghidra.framework.options.Options, program: ghidra.program.model.listing.Program) -> None:
        """
        Analyzers should register their options with associated default value, help content and
         description
        @param options the program options/property list that contains the options
        @param program program to be analyzed
        """
        ...

    def removed(self, program: ghidra.program.model.listing.Program, set: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor, log: ghidra.app.util.importer.MessageLog) -> bool:
        """
        Called when the requested information type has been removed.
         (ie: function removed.)
        @param program program to analyze
        @param set AddressSet of locations that have been added
        @param monitor monitor that indicates progress and indicates whether
         the user canceled the analysis
        @param log a message log to record analysis information
        @return true if the analysis succeeded
        """
        ...

    def supportsOneTimeAnalysis(self) -> bool:
        """
        Returns true if it makes sense for this analyzer to directly invoked on an address or
         addressSet.  The AutoAnalyzer plug-in will automatically create an action for each
         analyzer that returns true.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def analysisType(self) -> ghidra.app.services.AnalyzerType: ...

    @property
    def description(self) -> unicode: ...

    @property
    def name(self) -> unicode: ...

    @property
    def priority(self) -> ghidra.app.services.AnalysisPriority: ...

    @property
    def prototype(self) -> bool: ...
