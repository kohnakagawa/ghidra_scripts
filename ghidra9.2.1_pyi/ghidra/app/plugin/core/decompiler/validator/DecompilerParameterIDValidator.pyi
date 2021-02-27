import docking.widgets.conditiontestpanel
import ghidra.app.plugin.core.analysis.validator
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class DecompilerParameterIDValidator(ghidra.app.plugin.core.analysis.validator.PostAnalysisValidator):
    MIN_NUM_FUNCS: unicode = u'Minimum analysis threshold (% of funcs)'
    MIN_NUM_FUNCS_DEFAULT: int = 1



    def __init__(self, __a0: ghidra.program.model.listing.Program): ...



    def doRun(self, __a0: ghidra.util.task.TaskMonitor) -> docking.widgets.conditiontestpanel.ConditionResult: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def getName(self) -> unicode: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def run(self, __a0: ghidra.util.task.TaskMonitor) -> docking.widgets.conditiontestpanel.ConditionResult: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def description(self) -> unicode: ...

    @property
    def name(self) -> unicode: ...
