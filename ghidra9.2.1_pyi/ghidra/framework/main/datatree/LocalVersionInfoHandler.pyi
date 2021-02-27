import docking.widgets.tree
import ghidra.app.util
import ghidra.framework.main.datatree
import ghidra.framework.plugintool
import java.awt.datatransfer
import java.awt.dnd
import java.lang


class LocalVersionInfoHandler(object, ghidra.framework.main.datatree.DataTreeFlavorHandler, ghidra.app.util.FileOpenDataFlavorHandler):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def handle(self, tool: ghidra.framework.plugintool.PluginTool, obj: object, e: java.awt.dnd.DropTargetDropEvent, f: java.awt.datatransfer.DataFlavor) -> None: ...

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
