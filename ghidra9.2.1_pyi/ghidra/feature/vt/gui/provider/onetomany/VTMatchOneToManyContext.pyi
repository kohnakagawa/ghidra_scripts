from typing import List
import docking
import java.awt
import java.awt.event
import java.lang


class VTMatchOneToManyContext(docking.ActionContext):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getComponentProvider(self) -> docking.ComponentProvider: ...

    def getContextObject(self) -> object: ...

    def getGlobalContext(self) -> docking.ActionContext: ...

    def getMouseEvent(self) -> java.awt.event.MouseEvent: ...

    def getSelectedMatches(self) -> List[object]: ...

    def getSourceComponent(self) -> java.awt.Component: ...

    def getSourceObject(self) -> object: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setContextObject(self, __a0: object) -> docking.ActionContext: ...

    def setMouseEvent(self, __a0: java.awt.event.MouseEvent) -> docking.ActionContext: ...

    def setSourceObject(self, __a0: object) -> docking.ActionContext: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def selectedMatches(self) -> List[object]: ...