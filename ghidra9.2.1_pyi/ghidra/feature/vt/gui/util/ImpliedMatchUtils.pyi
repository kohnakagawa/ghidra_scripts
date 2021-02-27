import ghidra.feature.vt.api.main
import ghidra.feature.vt.gui.plugin
import ghidra.feature.vt.gui.provider.impliedmatches
import ghidra.program.model.listing
import ghidra.util.task
import java.lang
import java.util


class ImpliedMatchUtils(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def findImpliedMatches(__a0: ghidra.feature.vt.gui.plugin.VTController, __a1: ghidra.program.model.listing.Function, __a2: ghidra.program.model.listing.Function, __a3: ghidra.feature.vt.api.main.VTSession, __a4: ghidra.feature.vt.gui.plugin.AddressCorrelatorManager, __a5: ghidra.util.task.TaskMonitor) -> java.util.Set: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getDestinationFunction(__a0: ghidra.feature.vt.api.main.VTSession, __a1: ghidra.feature.vt.api.main.VTAssociation) -> ghidra.program.model.listing.Function: ...

    @staticmethod
    def getSourceFunction(__a0: ghidra.feature.vt.api.main.VTSession, __a1: ghidra.feature.vt.api.main.VTAssociation) -> ghidra.program.model.listing.Function: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def resolveImpliedMatch(__a0: ghidra.feature.vt.gui.provider.impliedmatches.VTImpliedMatchInfo, __a1: ghidra.feature.vt.api.main.VTSession) -> ghidra.feature.vt.api.main.VTMatch: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
