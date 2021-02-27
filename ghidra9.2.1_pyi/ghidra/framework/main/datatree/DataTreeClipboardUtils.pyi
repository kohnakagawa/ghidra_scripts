from typing import List
import docking.widgets.tree
import ghidra.framework.main.datatree
import java.awt.datatransfer
import java.lang
import javax.swing.tree


class DataTreeClipboardUtils(object):
    """
    Manages Ghidra integration with the system clipboard when doing cut/copy/paste
     operations on domainFiles and domainFolders in a data tree widget.

    """





    def __init__(self): ...



    @overload
    @staticmethod
    def clearCuttables() -> None:
        """
        Clears the {@link Cuttable#isCut() isCut} flag on any GTreeNodes that are pointed to by
         the system clipboard.
        """
        ...

    @overload
    @staticmethod
    def clearCuttables(transferable: java.awt.datatransfer.Transferable) -> None:
        """
        Clears the {@link Cuttable#isCut() isCut} flag on any GTreeNodes that are pointed to by
         the specified {@link Transferable}
        @param transferable contains clipboard contents
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getDataTreeNodesFromClipboard() -> List[docking.widgets.tree.GTreeNode]:
        """
        Fetches any GTreeNodes from the system clipboard.
        @return List of {@link GTreeNode}s that were in the system clipboard, or empty list if
         no nodes or some other access error.
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isCuttablePresent() -> bool:
        """
        Returns true if the system clipboard has any GTreeNodes that have the {@link Cuttable#isCut()}
         flag set.
        @return boolean true if there are any cut nodes in the clipboard
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def setClipboardContents(tree: ghidra.framework.main.datatree.DataTree, paths: List[javax.swing.tree.TreePath]) -> None:
        """
        Pushes the GTreeNodes in the specified TreePath array to the clipboard.
        @param tree DataTree that contains the GTreeNodes
        @param paths array of TreePaths containing nodes to be pushed to clipboard.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
