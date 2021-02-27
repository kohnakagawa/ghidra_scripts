from typing import List
import docking.widgets.tree
import docking.widgets.tree.support
import ghidra.framework.main.datatree
import java.awt.datatransfer
import java.lang


class DataTreeDragNDropHandler(object, docking.widgets.tree.support.GTreeDragNDropHandler):
    allSupportedFlavors: List[java.awt.datatransfer.DataFlavor]
    localDomainFileFlavor: java.awt.datatransfer.DataFlavor
    localDomainFileTreeFlavor: java.awt.datatransfer.DataFlavor







    @staticmethod
    def addActiveDataFlavorHandler(flavor: java.awt.datatransfer.DataFlavor, handler: ghidra.framework.main.datatree.DataTreeFlavorHandler) -> None: ...

    def drop(self, destination: docking.widgets.tree.GTreeNode, transferable: java.awt.datatransfer.Transferable, dropAction: int) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getSupportedDataFlavors(self, __a0: List[object]) -> List[java.awt.datatransfer.DataFlavor]: ...

    def getSupportedDragActions(self) -> int: ...

    def getTransferData(self, __a0: List[object], __a1: java.awt.datatransfer.DataFlavor) -> object: ...

    def hashCode(self) -> int: ...

    def isDropSiteOk(self, destUserData: docking.widgets.tree.GTreeNode, flavors: List[java.awt.datatransfer.DataFlavor], dropAction: int) -> bool: ...

    def isStartDragOk(self, __a0: List[object], __a1: int) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def removeActiveDataFlavorHandler(flavor: java.awt.datatransfer.DataFlavor) -> ghidra.framework.main.datatree.DataTreeFlavorHandler: ...

    def setProjectActive(self, b: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def projectActive(self) -> None: ...  # No getter available.

    @projectActive.setter
    def projectActive(self, value: bool) -> None: ...

    @property
    def supportedDragActions(self) -> int: ...
