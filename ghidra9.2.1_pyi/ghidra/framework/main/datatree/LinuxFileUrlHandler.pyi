import docking.widgets.tree
import ghidra.app.util
import ghidra.framework.main.datatree
import ghidra.framework.plugintool
import java.awt.datatransfer
import java.awt.dnd
import java.lang


class LinuxFileUrlHandler(object, ghidra.framework.main.datatree.DataTreeFlavorHandler, ghidra.app.util.FileOpenDataFlavorHandler):
    """
    A special handler to deal with files dragged from Linux to Ghidra.   This class does double
     duty in that it opens files for DataTrees and for Tools (signaled via the interfaces it
     implements).
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def handle(self, tool: ghidra.framework.plugintool.PluginTool, transferData: object, e: java.awt.dnd.DropTargetDropEvent, f: java.awt.datatransfer.DataFlavor) -> None: ...

    @overload
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
