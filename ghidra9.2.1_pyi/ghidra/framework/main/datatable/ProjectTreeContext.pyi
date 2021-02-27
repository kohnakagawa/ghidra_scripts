from typing import List
import ghidra.framework.main.datatree
import ghidra.framework.model
import java.lang
import javax.swing.tree


class ProjectTreeContext(object):
    """
    Common methods appropriate for both the FrontEndProjectTreeContext and the
     DialogProjectTreeContext.  The project tree actions require that the contexts be
     separate even though they need many of the same methods. By extracting the methods to this
     interface, the contexts can be kept separate, but can share action code.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFileCount(self) -> int:
        """
        Returns the number of files selected in the tree.
        @return the number of files selected in the tree.
        """
        ...

    def getFolderCount(self) -> int:
        """
        Returns the number of folders selected in the tree.
        @return the number of folders selected in the tree.
        """
        ...

    def getSelectedFiles(self) -> List[ghidra.framework.model.DomainFile]:
        """
        Returns a list of {@link DomainFile}s selected in the tree.
        @return a list of {@link DomainFile}s selected in the tree.
        """
        ...

    def getSelectedFolders(self) -> List[ghidra.framework.model.DomainFolder]:
        """
        Returns a list of {@link DomainFolder}s selected in the tree.
        @return a list of {@link DomainFolder}s selected in the tree.
        """
        ...

    def getSelectionPaths(self) -> List[javax.swing.tree.TreePath]:
        """
        Returns the list of selected {@link TreePath}s selected.
        @return the list of selected {@link TreePath}s selected.
        """
        ...

    def getTree(self) -> ghidra.framework.main.datatree.DataTree:
        """
        Returns the project data tree component.
        @return the project data tree component.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def fileCount(self) -> int: ...

    @property
    def folderCount(self) -> int: ...

    @property
    def selectedFiles(self) -> List[object]: ...

    @property
    def selectedFolders(self) -> List[object]: ...

    @property
    def selectionPaths(self) -> List[javax.swing.tree.TreePath]: ...

    @property
    def tree(self) -> ghidra.framework.main.datatree.DataTree: ...
