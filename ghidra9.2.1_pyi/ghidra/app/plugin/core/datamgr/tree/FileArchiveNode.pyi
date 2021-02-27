from typing import List
import docking.widgets.tree
import docking.widgets.tree.support
import ghidra.app.plugin.core.datamgr.archive
import ghidra.app.plugin.core.datamgr.tree
import ghidra.program.model.data
import ghidra.util.task
import java.lang
import java.util
import java.util.stream
import javax.swing
import javax.swing.tree


class FileArchiveNode(ghidra.app.plugin.core.datamgr.tree.ArchiveNode):




    def __init__(self, __a0: ghidra.app.plugin.core.datamgr.archive.FileArchive, __a1: ghidra.app.plugin.core.datamgr.tree.ArrayPointerFilterState): ...



    @overload
    def addNode(self, __a0: docking.widgets.tree.GTreeNode) -> None: ...

    @overload
    def addNode(self, __a0: int, __a1: docking.widgets.tree.GTreeNode) -> None: ...

    def addNodes(self, __a0: List[object]) -> None: ...

    def canCut(self) -> bool: ...

    def canDelete(self) -> bool: ...

    def canPaste(self, __a0: List[object]) -> bool: ...

    def canRename(self) -> bool: ...

    def categoryAdded(self, __a0: ghidra.program.model.data.Category) -> None: ...

    def categoryRemoved(self, __a0: unicode) -> None: ...

    def clone(self) -> object: ...

    def collapse(self) -> None: ...

    @overload
    def compareTo(self, __a0: docking.widgets.tree.GTreeNode) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def dataTypeAdded(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    def dataTypeChanged(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    def dataTypeRemoved(self, __a0: unicode) -> None: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def expand(self) -> None: ...

    def filter(self, __a0: docking.widgets.tree.support.GTreeFilter, __a1: ghidra.util.task.TaskMonitor) -> docking.widgets.tree.GTreeNode: ...

    @overload
    def findCategoryNode(self, __a0: ghidra.program.model.data.Category) -> ghidra.app.plugin.core.datamgr.tree.CategoryNode: ...

    @overload
    def findCategoryNode(self, __a0: ghidra.program.model.data.Category, __a1: bool) -> ghidra.app.plugin.core.datamgr.tree.CategoryNode: ...

    def fireNodeChanged(self, __a0: docking.widgets.tree.GTreeNode, __a1: docking.widgets.tree.GTreeNode) -> None: ...

    def fireNodeStructureChanged(self, __a0: docking.widgets.tree.GTreeNode) -> None: ...

    def getArchive(self) -> ghidra.app.plugin.core.datamgr.archive.Archive: ...

    def getArchiveNode(self) -> ghidra.app.plugin.core.datamgr.tree.ArchiveNode: ...

    def getCategory(self) -> ghidra.program.model.data.Category: ...

    @overload
    def getChild(self, __a0: int) -> docking.widgets.tree.GTreeNode: ...

    @overload
    def getChild(self, __a0: unicode) -> docking.widgets.tree.GTreeNode: ...

    def getChildCount(self) -> int: ...

    def getChildren(self) -> List[object]: ...

    def getClass(self) -> java.lang.Class: ...

    def getDisplayText(self) -> unicode: ...

    def getIcon(self, __a0: bool) -> javax.swing.Icon: ...

    def getIndexInParent(self) -> int: ...

    def getIndexOfChild(self, __a0: docking.widgets.tree.GTreeNode) -> int: ...

    def getLeafCount(self) -> int: ...

    def getName(self) -> unicode: ...

    def getNode(self, __a0: ghidra.program.model.data.DataType) -> ghidra.app.plugin.core.datamgr.tree.DataTypeNode: ...

    def getNodeCount(self) -> int: ...

    def getParent(self) -> docking.widgets.tree.GTreeNode: ...

    def getRoot(self) -> docking.widgets.tree.GTreeNode: ...

    def getToolTip(self) -> unicode: ...

    def getTree(self) -> docking.widgets.tree.GTree: ...

    def getTreePath(self) -> javax.swing.tree.TreePath: ...

    def hasWriteLock(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isAncestor(self, __a0: docking.widgets.tree.GTreeNode) -> bool: ...

    def isCut(self) -> bool: ...

    def isEditable(self) -> bool: ...

    def isEnabled(self) -> bool: ...

    def isExpanded(self) -> bool: ...

    def isInProgress(self) -> bool: ...

    def isLeaf(self) -> bool: ...

    def isLoaded(self) -> bool: ...

    def isModifiable(self) -> bool: ...

    def isRoot(self) -> bool: ...

    def iterator(self, __a0: bool) -> java.util.Iterator: ...

    def loadAll(self, __a0: ghidra.util.task.TaskMonitor) -> int: ...

    def nodeChanged(self) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeAll(self) -> None: ...

    def removeNode(self, __a0: docking.widgets.tree.GTreeNode) -> None: ...

    def setChildren(self, __a0: List[object]) -> None: ...

    def setNodeCut(self, __a0: bool) -> None: ...

    def stream(self, __a0: bool) -> java.util.stream.Stream: ...

    def structureChanged(self) -> None: ...

    def toString(self) -> unicode: ...

    def unloadChildren(self) -> None: ...

    def valueChanged(self, __a0: object) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def toolTip(self) -> unicode: ...
