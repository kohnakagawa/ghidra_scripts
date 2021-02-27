from typing import Iterator
from typing import List
import docking.widgets.tree
import docking.widgets.tree.support
import ghidra.formats.gfilesystem
import ghidra.plugins.fsbrowser
import ghidra.util.task
import java.lang
import java.util.stream
import javax.swing
import javax.swing.tree


class FSBRootNode(ghidra.plugins.fsbrowser.FSBNode):
    """
    A GTreeNode that represents the root of a GFileSystem, and keeps the
     filesystem pinned in memory with its FileSystemRef.

     The FileSystemRef is released when this node is #dispose()d.

     Visible to just this package.
    """









    @overload
    def addNode(self, node: docking.widgets.tree.GTreeNode) -> None: ...

    @overload
    def addNode(self, index: int, node: docking.widgets.tree.GTreeNode) -> None: ...

    def addNodes(self, __a0: List[object]) -> None: ...

    def clone(self) -> docking.widgets.tree.GTreeNode:
        """
        Creates a clone of this node.  The clone should contain a shallow copy of all the node's
         attributes except that the parent and children are null.
        @return the clone of this object.
        @throws CloneNotSupportedException if some implementation prevents itself from being cloned.
        """
        ...

    def collapse(self) -> None:
        """
        Convenience method for collapsing (closing) this node in the tree.  If this node is not
         currently attached to a visible tree, then this call does nothing
        """
        ...

    @overload
    def compareTo(self, node: docking.widgets.tree.GTreeNode) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def dispose(self) -> None: ...

    def equals(self, obj: object) -> bool: ...

    def expand(self) -> None:
        """
        Convenience method for expanding (opening) this node in the tree.  If this node is not
         currently attached to a visible tree, then this call does nothing
        """
        ...

    def filter(self, filter: docking.widgets.tree.support.GTreeFilter, monitor: ghidra.util.task.TaskMonitor) -> docking.widgets.tree.GTreeNode:
        """
        Generates a filtered copy of this node and its children.
         <P>
         A node will be included if it or any of its descendants are accepted by the filter.
         NOTE: the filter will only be applied to a nodes children if they are loaded. So to
         perform a filter on all the nodes in the tree, the {@link #loadAll(TaskMonitor)} should
         be called before the filter call.
        @param filter the filter being applied
        @param monitor a TaskMonitor for tracking the progress and cancelling
        @return A copy of this node and its children that matches the filter or null
         if this node and none of its children match the filter.
        @throws CancelledException if the operation is cancelled via the TaskMonitor
        @throws CloneNotSupportedException if any nodes in the tree explicitly prevents cloning
        """
        ...

    @staticmethod
    def findContainingFileSystemFSBRootNode(node: ghidra.plugins.fsbrowser.FSBNode) -> ghidra.plugins.fsbrowser.FSBRootNode:
        """
        Returns the {@link FSBRootNode} that represents the root of the file system that
         contains the specified file node.
        @param node GTree node that represents a file.
        @return FSBRootNode that represents the file system holding the file.
        """
        ...

    def fireNodeChanged(self, parentNode: docking.widgets.tree.GTreeNode, node: docking.widgets.tree.GTreeNode) -> None:
        """
        Notifies the tree that a node has changed
        @param parentNode the node that contains the node that was changed
        @param node the that changed
        """
        ...

    def fireNodeStructureChanged(self, node: docking.widgets.tree.GTreeNode) -> None:
        """
        Notifies the tree that the node has different children.  This method
        @param node the node that has changed.
        """
        ...

    def generateChildren(self, monitor: ghidra.util.task.TaskMonitor) -> List[docking.widgets.tree.GTreeNode]: ...

    @overload
    def getChild(self, index: int) -> docking.widgets.tree.GTreeNode:
        """
        Returns the child node at the given index. Returns null if the index is out of
         bounds.
        @param index the index of the child to be returned
        @return the child at the given index
        """
        ...

    @overload
    def getChild(self, name: unicode) -> docking.widgets.tree.GTreeNode:
        """
        Returns the child node of this node with the given name.
        @param name the name of the child to be returned
        @return the child with the given name
        """
        ...

    def getChildCount(self) -> int:
        """
        Returns the number of <b>visible</b> children of this node.  Does not include
         nodes that are current filtered out
        @return the number of <b>visible</b> children of this node
        """
        ...

    def getChildren(self) -> List[docking.widgets.tree.GTreeNode]:
        """
        Returns all of the <b>visible</b> children of this node.  If there are filtered nodes, then
         they will not be returned.
        @return all of the <b>visible</b> children of this node.  If there are filtered nodes, then
         		   they will not be returned.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDisplayText(self) -> unicode:
        """
        Returns the display text for the node.  By default, this is the same as the name of the node.
         The name of the node usually serves two purposes: 1) to uniquely identify the node (the
         identity) and 2) the display text (what you see in the tree). Sometimes, it is useful to
         display more information in the tree without affecting the nodes identity.  In this case,
         you can override this method to return the "display" name, while {@link #getName()} will
         still return the name used to identify the node.
        @return the display text for the node.
        """
        ...

    def getFSRL(self) -> ghidra.formats.gfilesystem.FSRL: ...

    def getFSRef(self) -> ghidra.formats.gfilesystem.FileSystemRef: ...

    def getIcon(self, expanded: bool) -> javax.swing.Icon: ...

    def getIndexInParent(self) -> int:
        """
        Returns the index of this node within its parent node
        @return the index of this node within its parent node
        """
        ...

    def getIndexOfChild(self, node: docking.widgets.tree.GTreeNode) -> int:
        """
        Returns the index of the given node within this node.  -1 is returned
         if the node is not a child of this node.
        @param node whose index we want
        @return the index of the given node within this node
        """
        ...

    def getLeafCount(self) -> int:
        """
        Returns the total number of leaf nodes in the subtree from this node.  Note that if any
         nodes are "lazy" (see {@link GTreeLazyNode}) and not currently loaded, then it will be
         considered as a leaf and return 1.
        @return the total number of leaf nodes in the subtree from this node
        """
        ...

    def getName(self) -> unicode: ...

    def getNodeCount(self) -> int:
        """
        Returns the total number of nodes in the subtree rooted at this node.  Leaf
         nodes return 1.
        @return the number of nodes from this node downward
        """
        ...

    @staticmethod
    def getNodeFromFile(file: ghidra.formats.gfilesystem.GFile) -> ghidra.plugins.fsbrowser.FSBNode:
        """
        Helper method to convert a single {@link GFile} object into a FSBNode object.
        @param file {@link GFile} to convert
        @return a new {@link FSBNode} with type specific to the GFile's type.
        """
        ...

    @staticmethod
    def getNodesFromFileList(__a0: List[object]) -> List[object]: ...

    def getParent(self) -> docking.widgets.tree.GTreeNode:
        """
        Returns the parent of this node.

         Note: this method is deliberately not synchronized (See comments above)
        @return the parent of this node.
        """
        ...

    def getPrevNode(self) -> ghidra.plugins.fsbrowser.FSBFileNode: ...

    def getRoot(self) -> docking.widgets.tree.GTreeNode:
        """
        Returns the rootNode for this tree or null if there is no parent path to a
         GTRootNode
        @return the rootNode for this tree
        """
        ...

    def getSubRootNodes(self) -> List[ghidra.plugins.fsbrowser.FSBRootNode]: ...

    def getToolTip(self) -> unicode: ...

    def getTree(self) -> docking.widgets.tree.GTree:
        """
        Returns the GTree that this node is attached to
        @return the GTree that this node is attached to
        """
        ...

    def getTreePath(self) -> javax.swing.tree.TreePath:
        """
        Returns the TreePath for this node
        @return the TreePath for this node
        """
        ...

    def hashCode(self) -> int: ...

    def isAncestor(self, node: docking.widgets.tree.GTreeNode) -> bool:
        """
        Returns true if the given node is a child of this node or one of its children.
        @param node the potential descendant node to check
        @return true if the given node is a child of this node or one of its children
        """
        ...

    def isEditable(self) -> bool:
        """
        Returns true if this node is allowed to be edited in the tree.  You must override this
         method to allow a node to be edited.  You must also override {@link #valueChanged(Object)}
         to handle the result of the edit.
        @return true if this node is allowed to be edited in the tree
        @see #valueChanged(Object)
        """
        ...

    def isExpanded(self) -> bool:
        """
        Convenience method determining if this node is expanded in a tree.  If the node is not
         currently attached to a visible tree, then this call returns false
        @return true if the node is expanded in a currently visible tree.
        """
        ...

    def isInProgress(self) -> bool:
        """
        Returns true if the node is in the process of loading its children.
         See {@link GTreeSlowLoadingNode}
        @return true if the node is in the process of loading its children.
        """
        ...

    def isLeaf(self) -> bool: ...

    def isLoaded(self) -> bool:
        """
        True if the children for this node have been loaded yet.  Some GTree nodes are lazy in that they
         don't load their children until needed. Nodes that have the IN_PROGRESS node as it child
         is considered loaded if in the swing thread, otherwise they are considered not loaded.
        @return true if the children for this node have been loaded.
        """
        ...

    def isRoot(self) -> bool:
        """
        Returns true if this is a root node
        @return true if this is a root node
        """
        ...

    def iterator(self, depthFirst: bool) -> Iterator[docking.widgets.tree.GTreeNode]:
        """
        Returns an iterator of the GTree nodes in the subtree of this node
        @param depthFirst if true, the nodes will be returned in depth-first order, otherwise breadth-first order
        @return an iterator of the GTree nodes in the subtree of this node
        """
        ...

    def loadAll(self, monitor: ghidra.util.task.TaskMonitor) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def releaseFSRefs(self) -> None: ...

    def removeAll(self) -> None: ...

    def removeNode(self, node: docking.widgets.tree.GTreeNode) -> None: ...

    def setChildren(self, __a0: List[object]) -> None: ...

    def stream(self, depthFirst: bool) -> java.util.stream.Stream:
        """
        Returns a stream of the GTree nodes in the subtree of this node
        @param depthFirst if true, the nodes will be streamed in depth-first order, otherwise breadth-first order
        @return a stream of the GTree nodes in the subtree of this node
        """
        ...

    def toString(self) -> unicode: ...

    def unloadChildren(self) -> None:
        """
        Sets this lazy node back to the "unloaded" state such that if
         its children are accessed, it will reload its children as needed.
        """
        ...

    def valueChanged(self, newValue: object) -> None:
        """
        Notification method called when a cell editor completes editing to notify this
         node that its value has changed.  If you override this method you must also override
         {@link #isEditable()}.
        @param newValue the new value provided by the cell editor
        @see #isEditable()
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def FSRL(self) -> ghidra.formats.gfilesystem.FSRL: ...

    @property
    def FSRef(self) -> ghidra.formats.gfilesystem.FileSystemRef: ...

    @property
    def leaf(self) -> bool: ...

    @property
    def name(self) -> unicode: ...

    @property
    def prevNode(self) -> ghidra.plugins.fsbrowser.FSBFileNode: ...

    @property
    def subRootNodes(self) -> List[object]: ...

    @property
    def toolTip(self) -> unicode: ...
