from typing import List
import docking.widgets.tree
import docking.widgets.tree.support
import ghidra.app.plugin.core.datamgr.tree
import ghidra.program.model.data
import ghidra.util.task
import java.lang
import java.util
import java.util.stream
import javax.swing
import javax.swing.tree


class DataTypeNode(ghidra.app.plugin.core.datamgr.tree.DataTypeTreeNode):




    def __init__(self, __a0: ghidra.program.model.data.DataType): ...



    @overload
    def addNode(self, __a0: docking.widgets.tree.GTreeNode) -> None: ...

    @overload
    def addNode(self, __a0: int, __a1: docking.widgets.tree.GTreeNode) -> None: ...

    def addNodes(self, __a0: List[object]) -> None: ...

    def canCut(self) -> bool: ...

    def canDelete(self) -> bool: ...

    def canPaste(self, __a0: List[object]) -> bool: ...

    def clone(self) -> object: ...

    def collapse(self) -> None: ...

    @overload
    def compareTo(self, __a0: docking.widgets.tree.GTreeNode) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def dataTypeChanged(self) -> None: ...

    def dataTypeStatusChanged(self) -> None: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def expand(self) -> None: ...

    def filter(self, __a0: docking.widgets.tree.support.GTreeFilter, __a1: ghidra.util.task.TaskMonitor) -> docking.widgets.tree.GTreeNode: ...

    def fireNodeChanged(self, __a0: docking.widgets.tree.GTreeNode, __a1: docking.widgets.tree.GTreeNode) -> None: ...

    def fireNodeStructureChanged(self, __a0: docking.widgets.tree.GTreeNode) -> None: ...

    def getArchiveNode(self) -> ghidra.app.plugin.core.datamgr.tree.ArchiveNode: ...

    @overload
    def getChild(self, __a0: int) -> docking.widgets.tree.GTreeNode: ...

    @overload
    def getChild(self, __a0: unicode) -> docking.widgets.tree.GTreeNode: ...

    def getChildCount(self) -> int: ...

    def getChildren(self) -> List[object]: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataType(self) -> ghidra.program.model.data.DataType: ...

    def getDisplayText(self) -> unicode: ...

    def getIcon(self, __a0: bool) -> javax.swing.Icon: ...

    def getIndexInParent(self) -> int: ...

    def getIndexOfChild(self, __a0: docking.widgets.tree.GTreeNode) -> int: ...

    def getLeafCount(self) -> int: ...

    def getName(self) -> unicode: ...

    def getNodeCount(self) -> int: ...

    def getParent(self) -> docking.widgets.tree.GTreeNode: ...

    def getRoot(self) -> docking.widgets.tree.GTreeNode: ...

    def getToolTip(self) -> unicode: ...

    def getTree(self) -> docking.widgets.tree.GTree: ...

    def getTreePath(self) -> javax.swing.tree.TreePath: ...

    def hasCustomEditor(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isAncestor(self, __a0: docking.widgets.tree.GTreeNode) -> bool: ...

    def isCut(self) -> bool: ...

    def isEditable(self) -> bool: ...

    def isExpanded(self) -> bool: ...

    def isFavorite(self) -> bool: ...

    def isInProgress(self) -> bool: ...

    def isLeaf(self) -> bool: ...

    def isLoaded(self) -> bool: ...

    def isModifiable(self) -> bool: ...

    def isRoot(self) -> bool: ...

    def iterator(self, __a0: bool) -> java.util.Iterator: ...

    def loadAll(self, __a0: ghidra.util.task.TaskMonitor) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeAll(self) -> None: ...

    def removeNode(self, __a0: docking.widgets.tree.GTreeNode) -> None: ...

    def setChildren(self, __a0: List[object]) -> None: ...

    def setNodeCut(self, __a0: bool) -> None: ...

    def stream(self, __a0: bool) -> java.util.stream.Stream: ...

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
    def archiveNode(self) -> ghidra.app.plugin.core.datamgr.tree.ArchiveNode: ...

    @property
    def cut(self) -> bool: ...

    @property
    def dataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def displayText(self) -> unicode: ...

    @property
    def editable(self) -> bool: ...

    @property
    def favorite(self) -> bool: ...

    @property
    def leaf(self) -> bool: ...

    @property
    def modifiable(self) -> bool: ...

    @property
    def name(self) -> unicode: ...

    @property
    def nodeCut(self) -> None: ...  # No getter available.

    @nodeCut.setter
    def nodeCut(self, value: bool) -> None: ...

    @property
    def toolTip(self) -> unicode: ...