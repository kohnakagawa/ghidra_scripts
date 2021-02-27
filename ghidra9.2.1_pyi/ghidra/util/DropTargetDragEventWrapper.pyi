from typing import List
import java.awt
import java.awt.datatransfer
import java.awt.dnd
import java.lang


class DropTargetDragEventWrapper(java.awt.dnd.DropTargetDragEvent):




    def __init__(self, __a0: java.awt.dnd.DropTargetContext, __a1: java.awt.Point, __a2: int, __a3: int): ...



    def acceptDrag(self, dragOp: int) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCurrentDataFlavors(self) -> List[java.awt.datatransfer.DataFlavor]: ...

    def getCurrentDataFlavorsAsList(self) -> List[object]: ...

    def getDropAction(self) -> int: ...

    def getDropTargetContext(self) -> java.awt.dnd.DropTargetContext: ...

    def getLocation(self) -> java.awt.Point: ...

    def getSource(self) -> object: ...

    def getSourceActions(self) -> int: ...

    def getTransferable(self) -> java.awt.datatransfer.Transferable: ...

    def hashCode(self) -> int: ...

    def isDataFlavorSupported(self, __a0: java.awt.datatransfer.DataFlavor) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def rejectDrag(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...