from typing import List
import docking
import docking.widgets.fieldpanel.support
import ghidra.app.services
import ghidra.app.util
import ghidra.util.task
import java.awt
import java.awt.datatransfer
import java.lang
import javax.swing.event


class DecompilerClipboardProvider(ghidra.app.util.ByteCopier, ghidra.app.services.ClipboardContentProviderService):




    def __init__(self, __a0: ghidra.app.plugin.core.decompile.DecompilePlugin, __a1: ghidra.app.plugin.core.decompile.DecompilerProvider): ...



    def addChangeListener(self, __a0: javax.swing.event.ChangeListener) -> None: ...

    def canCopy(self) -> bool: ...

    def canCopySpecial(self) -> bool: ...

    def canPaste(self, __a0: List[java.awt.datatransfer.DataFlavor]) -> bool: ...

    def copy(self, __a0: ghidra.util.task.TaskMonitor) -> java.awt.datatransfer.Transferable: ...

    def copySpecial(self, __a0: ghidra.app.util.ClipboardType, __a1: ghidra.util.task.TaskMonitor) -> java.awt.datatransfer.Transferable: ...

    @staticmethod
    def createStringTransferable(__a0: unicode) -> java.awt.datatransfer.Transferable: ...

    def enableCopy(self) -> bool: ...

    def enableCopySpecial(self) -> bool: ...

    def enablePaste(self) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getComponentProvider(self) -> docking.ComponentProvider: ...

    def getCurrentCopyTypes(self) -> List[object]: ...

    def getCurrentPasteTypes(self, __a0: java.awt.datatransfer.Transferable) -> List[object]: ...

    def hashCode(self) -> int: ...

    def isValidContext(self, __a0: docking.ActionContext) -> bool: ...

    def lostOwnership(self, __a0: java.awt.datatransfer.Transferable) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def paste(self, __a0: java.awt.datatransfer.Transferable) -> bool: ...

    def pasteSpecial(self, __a0: java.awt.datatransfer.Transferable, __a1: ghidra.app.util.ClipboardType) -> bool: ...

    def removeChangeListener(self, __a0: javax.swing.event.ChangeListener) -> None: ...

    def selectionChanged(self, __a0: docking.widgets.fieldpanel.support.FieldSelection) -> None: ...

    def setFontMetrics(self, __a0: java.awt.FontMetrics) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def componentProvider(self) -> docking.ComponentProvider: ...

    @property
    def currentCopyTypes(self) -> List[object]: ...

    @property
    def fontMetrics(self) -> None: ...  # No getter available.

    @fontMetrics.setter
    def fontMetrics(self, value: java.awt.FontMetrics) -> None: ...