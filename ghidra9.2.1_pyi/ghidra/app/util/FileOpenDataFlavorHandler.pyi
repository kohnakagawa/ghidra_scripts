import ghidra.framework.plugintool
import java.awt.datatransfer
import java.awt.dnd
import java.lang


class FileOpenDataFlavorHandler(object):
    """
    Interface for classes that will handle drop actions for files dropped onto the tool
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def handle(self, tool: ghidra.framework.plugintool.PluginTool, obj: object, e: java.awt.dnd.DropTargetDropEvent, f: java.awt.datatransfer.DataFlavor) -> None: ...

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
