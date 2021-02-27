import ghidra.feature.vt.gui.filters
import ghidra.framework.options
import java.lang
import java.util
import javax.swing


class MarkupStatusFilter(ghidra.feature.vt.gui.filters.CheckBoxBasedAncillaryFilter):




    def __init__(self): ...



    def addFilterChangedListener(self, __a0: ghidra.feature.vt.gui.filters.FilterChangedListener) -> None: ...

    def addFilterStatusListener(self, __a0: ghidra.feature.vt.gui.filters.FilterStatusListener) -> None: ...

    def clearFilter(self) -> None: ...

    def createCopy(self) -> ghidra.feature.vt.gui.filters.Filter: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def fireFilterStateChanged(self) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getComponent(self) -> javax.swing.JComponent: ...

    def getEnabledFilterNames(self) -> java.util.Set: ...

    def getFilterShortcutState(self) -> ghidra.feature.vt.gui.filters.Filter.FilterShortcutState: ...

    def getFilterState(self) -> ghidra.feature.vt.gui.filters.FilterState: ...

    def getFilterStatus(self) -> ghidra.feature.vt.gui.filters.Filter.FilterEditingStatus: ...

    def hashCode(self) -> int: ...

    def isSubFilterOf(self, __a0: ghidra.feature.vt.gui.filters.Filter) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def passesFilter(self, __a0: object) -> bool: ...

    def readConfigState(self, __a0: ghidra.framework.options.SaveState) -> None: ...

    def removeFilterChangedListener(self, __a0: ghidra.feature.vt.gui.filters.FilterChangedListener) -> None: ...

    def restoreFilterState(self, __a0: ghidra.feature.vt.gui.filters.FilterState) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeConfigState(self, __a0: ghidra.framework.options.SaveState) -> None: ...
