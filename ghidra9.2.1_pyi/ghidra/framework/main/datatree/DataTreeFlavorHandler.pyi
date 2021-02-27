import docking.widgets.tree
import ghidra.framework.main.datatree
import ghidra.framework.plugintool
import java.lang


class DataTreeFlavorHandler(object):
    """
    Interface for classes that will handle drop actions for DataTrees.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def handle(self, tool: ghidra.framework.plugintool.PluginTool, dataTree: ghidra.framework.main.datatree.DataTree, destinationNode: docking.widgets.tree.GTreeNode, transferData: object, dropAction: int) -> None: ...

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
