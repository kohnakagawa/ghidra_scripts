from typing import List
import ghidra.app.plugin.core.overview
import ghidra.framework.plugintool
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util
import ghidra.util.classfinder
import java.awt
import java.lang


class OverviewColorService(ghidra.util.classfinder.ExtensionPoint, object):








    def equals(self, __a0: object) -> bool: ...

    def getActions(self) -> List[object]: ...

    def getClass(self) -> java.lang.Class: ...

    def getColor(self, __a0: ghidra.program.model.address.Address) -> java.awt.Color: ...

    def getHelpLocation(self) -> ghidra.util.HelpLocation: ...

    def getName(self) -> unicode: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def getToolTipText(self, __a0: ghidra.program.model.address.Address) -> unicode: ...

    def hashCode(self) -> int: ...

    def initialize(self, __a0: ghidra.framework.plugintool.PluginTool) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setOverviewComponent(self, __a0: ghidra.app.plugin.core.overview.OverviewColorComponent) -> None: ...

    def setProgram(self, __a0: ghidra.program.model.listing.Program) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def actions(self) -> List[object]: ...

    @property
    def helpLocation(self) -> ghidra.util.HelpLocation: ...

    @property
    def name(self) -> unicode: ...

    @property
    def overviewComponent(self) -> None: ...  # No getter available.

    @overviewComponent.setter
    def overviewComponent(self, value: ghidra.app.plugin.core.overview.OverviewColorComponent) -> None: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...

    @program.setter
    def program(self, value: ghidra.program.model.listing.Program) -> None: ...
