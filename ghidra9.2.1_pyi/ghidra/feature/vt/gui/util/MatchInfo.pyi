import ghidra.feature.vt.api.main
import ghidra.feature.vt.api.markuptype
import ghidra.feature.vt.gui.plugin
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.util
import ghidra.util.task
import java.lang
import java.util


class MatchInfo(object):








    def clearCache(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getAppliableMarkupItems(self, __a0: ghidra.util.task.TaskMonitor) -> java.util.Collection: ...

    def getClass(self) -> java.lang.Class: ...

    def getCurrentMarkupForLocation(self, __a0: ghidra.program.util.ProgramLocation, __a1: ghidra.program.model.listing.Program) -> ghidra.feature.vt.api.main.VTMarkupItem: ...

    def getDestinationAddress(self, __a0: ghidra.program.model.address.Address, __a1: ghidra.feature.vt.gui.plugin.AddressCorrelatorManager) -> ghidra.program.model.address.Address: ...

    def getDestinationAddressSet(self) -> ghidra.program.model.address.AddressSetView: ...

    def getDestinationData(self) -> ghidra.program.model.listing.Data: ...

    def getDestinationFunction(self) -> ghidra.program.model.listing.Function: ...

    @staticmethod
    def getMarkupAddressForLocation(__a0: ghidra.program.util.ProgramLocation, __a1: ghidra.program.model.listing.Program) -> ghidra.program.model.address.Address: ...

    @staticmethod
    def getMarkupTypeForLocation(__a0: ghidra.program.util.ProgramLocation, __a1: ghidra.program.model.listing.Program) -> ghidra.feature.vt.api.markuptype.VTMarkupType: ...

    def getMatch(self) -> ghidra.feature.vt.api.main.VTMatch: ...

    def getSourceAddressSet(self) -> ghidra.program.model.address.AddressSetView: ...

    def getSourceData(self) -> ghidra.program.model.listing.Data: ...

    def getSourceFunction(self) -> ghidra.program.model.listing.Function: ...

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
    def destinationAddressSet(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def destinationData(self) -> ghidra.program.model.listing.Data: ...

    @property
    def destinationFunction(self) -> ghidra.program.model.listing.Function: ...

    @property
    def match(self) -> ghidra.feature.vt.api.main.VTMatch: ...

    @property
    def sourceAddressSet(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def sourceData(self) -> ghidra.program.model.listing.Data: ...

    @property
    def sourceFunction(self) -> ghidra.program.model.listing.Function: ...