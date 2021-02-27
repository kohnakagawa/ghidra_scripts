import docking.widgets.conditiontestpanel
import ghidra.feature.vt.gui.validator
import ghidra.util.task
import java.lang


class PercentAnalyzedVTPreconditionValidator(ghidra.feature.vt.gui.validator.VTPostAnalysisPreconditionValidatorAdaptor):




    def __init__(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.listing.Program, __a2: ghidra.feature.vt.api.main.VTSession): ...



    def doRun(self, __a0: ghidra.util.task.TaskMonitor) -> docking.widgets.conditiontestpanel.ConditionResult: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def getName(self) -> unicode: ...

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
