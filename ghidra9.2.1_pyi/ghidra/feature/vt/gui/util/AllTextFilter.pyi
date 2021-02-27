import ghidra.feature.vt.gui.filters
import ghidra.feature.vt.gui.util
import ghidra.framework.options
import java.lang
import javax.swing


class AllTextFilter(ghidra.feature.vt.gui.util.AbstractTextFilter):




    def __init__(self, __a0: ghidra.feature.vt.gui.plugin.VTController, __a1: docking.widgets.table.GTable, __a2: docking.widgets.table.threaded.ThreadedTableModel): ...



    def addFilterStatusListener(self, __a0: ghidra.feature.vt.gui.filters.FilterStatusListener) -> None: ...

    def clearFilter(self) -> None: ...

    def createCopy(self) -> ghidra.feature.vt.gui.filters.Filter: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getComponent(self) -> javax.swing.JComponent: ...

    def getFilterShortcutState(self) -> ghidra.feature.vt.gui.filters.Filter.FilterShortcutState: ...

    def getFilterStatus(self) -> ghidra.feature.vt.gui.filters.Filter.FilterEditingStatus: ...

    def hashCode(self) -> int: ...

    def isSubFilterOf(self, __a0: ghidra.feature.vt.gui.filters.Filter) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def passesFilter(self, __a0: object) -> bool: ...

    def readConfigState(self, __a0: ghidra.framework.options.SaveState) -> None: ...

    def setName(self, __a0: unicode) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeConfigState(self, __a0: ghidra.framework.options.SaveState) -> None: ...