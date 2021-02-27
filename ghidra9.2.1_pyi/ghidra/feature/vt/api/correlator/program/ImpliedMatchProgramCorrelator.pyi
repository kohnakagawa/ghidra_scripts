import ghidra.feature.vt.api.main
import ghidra.feature.vt.api.util
import ghidra.framework.options
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class ImpliedMatchProgramCorrelator(ghidra.feature.vt.api.util.VTAbstractProgramCorrelator):
    MANUAL_SCORE: ghidra.feature.vt.api.main.VTScore = 1.000
    NAME: unicode = u'Implied Match'



    def __init__(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.listing.Program): ...



    def correlate(self, __a0: ghidra.feature.vt.api.main.VTSession, __a1: ghidra.util.task.TaskMonitor) -> ghidra.feature.vt.api.main.VTMatchSet: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDestinationAddressSet(self) -> ghidra.program.model.address.AddressSetView: ...

    def getDestinationProgram(self) -> ghidra.program.model.listing.Program: ...

    def getName(self) -> unicode: ...

    def getOptions(self) -> ghidra.framework.options.ToolOptions: ...

    def getSourceAddressSet(self) -> ghidra.program.model.address.AddressSetView: ...

    def getSourceProgram(self) -> ghidra.program.model.listing.Program: ...

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
    def name(self) -> unicode: ...