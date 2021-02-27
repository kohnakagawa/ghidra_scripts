import docking
import docking.dnd
import ghidra.app.util
import java.awt.datatransfer
import java.awt.dnd
import java.awt.event
import java.lang


class FileOpenDropHandler(object, docking.DropTargetHandler, docking.dnd.Droppable, java.awt.event.ContainerListener):
    """
    Handles drag/drop events on a given component such that a file
      dropped on the component from the front end tool will cause
      that file to be opened.  Properly handles drop events with
      child components and listens for components being added/removed
      in order to properly support drag/drop with all components.
    """





    def __init__(self, tool: ghidra.framework.plugintool.PluginTool, component: java.awt.Component):
        """
        Construct a new FileOpenDropHandler.
        @param tool plugin tool
        @param component component that is the drop target
        """
        ...



    def add(self, obj: object, e: java.awt.dnd.DropTargetDropEvent, f: java.awt.datatransfer.DataFlavor) -> None: ...

    @staticmethod
    def addDataFlavorHandler(dataFlavor: java.awt.datatransfer.DataFlavor, handler: ghidra.app.util.FileOpenDataFlavorHandler) -> None: ...

    def componentAdded(self, e: java.awt.event.ContainerEvent) -> None: ...

    def componentRemoved(self, e: java.awt.event.ContainerEvent) -> None: ...

    def dispose(self) -> None:
        """
        Dispose this drop handler.
        """
        ...

    def dragUnderFeedback(self, ok: bool, e: java.awt.dnd.DropTargetDragEvent) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isDropOk(self, e: java.awt.dnd.DropTargetDragEvent) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def removeDataFlavorHandler(dataFlavor: java.awt.datatransfer.DataFlavor) -> ghidra.app.util.FileOpenDataFlavorHandler: ...

    def toString(self) -> unicode: ...

    def undoDragUnderFeedback(self) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
