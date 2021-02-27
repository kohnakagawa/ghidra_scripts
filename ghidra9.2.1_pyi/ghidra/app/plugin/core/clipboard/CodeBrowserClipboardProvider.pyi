from typing import List
import docking
import ghidra.app.services
import ghidra.app.util
import ghidra.app.util.viewer.listingpanel
import ghidra.program.model.listing
import ghidra.program.util
import ghidra.util.task
import java.awt.datatransfer
import java.lang
import javax.swing.event


class CodeBrowserClipboardProvider(ghidra.app.util.ByteCopier, ghidra.app.services.ClipboardContentProviderService):
    ADDRESS_TEXT_TYPE: ghidra.app.util.ClipboardType = Address
    CODE_TEXT_TYPE: ghidra.app.util.ClipboardType = Formatted Code
    COMMENTS_TYPE: ghidra.app.util.ClipboardType = Comments
    LABELS_COMMENTS_TYPE: ghidra.app.util.ClipboardType = Labels and Comments
    LABELS_TYPE: ghidra.app.util.ClipboardType = Labels



    def __init__(self, __a0: ghidra.framework.plugintool.PluginTool, __a1: docking.ComponentProvider): ...



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

    def getStringContent(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def isValidContext(self, __a0: docking.ActionContext) -> bool: ...

    def lostOwnership(self, __a0: java.awt.datatransfer.Transferable) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def paste(self, __a0: java.awt.datatransfer.Transferable) -> bool: ...

    def removeChangeListener(self, __a0: javax.swing.event.ChangeListener) -> None: ...

    def setListingLayoutModel(self, __a0: ghidra.app.util.viewer.listingpanel.ListingModel) -> None: ...

    def setLocation(self, __a0: ghidra.program.util.ProgramLocation) -> None: ...

    def setProgram(self, __a0: ghidra.program.model.listing.Program) -> None: ...

    def setSelection(self, __a0: ghidra.program.util.ProgramSelection) -> None: ...

    def setStringContent(self, __a0: unicode) -> None: ...

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
    def listingLayoutModel(self) -> None: ...  # No getter available.

    @listingLayoutModel.setter
    def listingLayoutModel(self, value: ghidra.app.util.viewer.listingpanel.ListingModel) -> None: ...

    @property
    def location(self) -> None: ...  # No getter available.

    @location.setter
    def location(self, value: ghidra.program.util.ProgramLocation) -> None: ...

    @property
    def program(self) -> None: ...  # No getter available.

    @program.setter
    def program(self, value: ghidra.program.model.listing.Program) -> None: ...

    @property
    def selection(self) -> None: ...  # No getter available.

    @selection.setter
    def selection(self, value: ghidra.program.util.ProgramSelection) -> None: ...

    @property
    def stringContent(self) -> unicode: ...

    @stringContent.setter
    def stringContent(self, value: unicode) -> None: ...