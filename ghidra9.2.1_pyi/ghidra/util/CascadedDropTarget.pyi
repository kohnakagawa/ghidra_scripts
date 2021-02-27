import java.awt
import java.awt.datatransfer
import java.awt.dnd
import java.lang


class CascadedDropTarget(java.awt.dnd.DropTarget):
    """
    Combines two drop targets and sends events to them in priority order.  If the first drop target
     accepts the event, then the second drop target is not accessed.

     Either of the given drop targets can be an instance of CascadedDropTarget, effectively creating
     a tree structure of drop targets.
    """





    def __init__(self, comp: java.awt.Component, firstDropTarget: java.awt.dnd.DropTarget, secondDropTarget: java.awt.dnd.DropTarget): ...



    def addDropTargetListener(self, __a0: java.awt.dnd.DropTargetListener) -> None: ...

    def addNotify(self) -> None: ...

    def dragEnter(self, dtde: java.awt.dnd.DropTargetDragEvent) -> None: ...

    def dragExit(self, dte: java.awt.dnd.DropTargetEvent) -> None: ...

    def dragOver(self, dtde: java.awt.dnd.DropTargetDragEvent) -> None: ...

    def drop(self, dtde: java.awt.dnd.DropTargetDropEvent) -> None: ...

    def dropActionChanged(self, dtde: java.awt.dnd.DropTargetDragEvent) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getComponent(self) -> java.awt.Component: ...

    def getDefaultActions(self) -> int: ...

    def getDropTargetContext(self) -> java.awt.dnd.DropTargetContext: ...

    def getFlavorMap(self) -> java.awt.datatransfer.FlavorMap: ...

    def getPrimaryDropTarget(self) -> java.awt.dnd.DropTarget: ...

    def getSecondaryDropTarget(self) -> java.awt.dnd.DropTarget: ...

    def hashCode(self) -> int: ...

    def isActive(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeDropTarget(self, dropTarget: java.awt.dnd.DropTarget) -> java.awt.dnd.DropTarget:
        """
        Removes the given drop target from anywhere within the tree of CascadedDropTargets.

         If the given <code>dropTarget</code> is an immediate child of this CascadedDropTarget (CDT), then
         the other child is returned.  Otherwise, a reference to this CDT will be returned with the
         given <code>dropTarget</code> having been removed from one of this CDT's children.  This method
         effectively removes the given <code>dropTarget</code> from the hierarchy and collapses the tree
         structure as needed.
        @param dropTarget The target to remove
        @return the new drop target reference
        """
        ...

    def removeDropTargetListener(self, __a0: java.awt.dnd.DropTargetListener) -> None: ...

    def removeNotify(self) -> None: ...

    def setActive(self, __a0: bool) -> None: ...

    def setComponent(self, __a0: java.awt.Component) -> None: ...

    def setDefaultActions(self, __a0: int) -> None: ...

    def setFlavorMap(self, __a0: java.awt.datatransfer.FlavorMap) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def primaryDropTarget(self) -> java.awt.dnd.DropTarget: ...

    @property
    def secondaryDropTarget(self) -> java.awt.dnd.DropTarget: ...
