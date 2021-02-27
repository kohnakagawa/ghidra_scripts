from typing import List
import java.awt.datatransfer
import java.awt.dnd
import java.lang


class ProgramDropProvider(object):
    """
    Generic interface to handle drag and drop.
    """









    def add(self, contextObj: object, data: object, flavor: java.awt.datatransfer.DataFlavor) -> None:
        """
        Adds the dropped data to this drop service.
        @param contextObj The object where the drop occurred
        @param data The actual data dropped
        @param flavor The selected data flavor
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataFlavors(self) -> List[java.awt.datatransfer.DataFlavor]:
        """
        Get the data flavors that this drop service accepts.
        @return an array of all DataFlavors that this drop service supports
        """
        ...

    def getPriority(self) -> int:
        """
        Returns the priority of this provider.  Higher priority services will be chosen
         if there are multiple services that accept the same type in the same context.
        """
        ...

    def hashCode(self) -> int: ...

    def isDropOk(self, contextObj: object, evt: java.awt.dnd.DropTargetDragEvent) -> bool:
        """
        Returns true if this service can accept a drop with the specified context.
        @param contextObj The object where the drop will occur
        @param evt The event associated with the drop that includes the dropped DataFlavors
        """
        ...

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
    def dataFlavors(self) -> List[java.awt.datatransfer.DataFlavor]: ...

    @property
    def priority(self) -> int: ...
