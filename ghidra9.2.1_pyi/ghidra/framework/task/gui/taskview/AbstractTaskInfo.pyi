import ghidra.framework.task
import ghidra.framework.task.gui
import ghidra.framework.task.gui.taskview
import java.awt
import java.lang


class AbstractTaskInfo(object, java.lang.Comparable):








    @overload
    def compareTo(self, o: ghidra.framework.task.gui.taskview.AbstractTaskInfo) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getComponent(self) -> ghidra.framework.task.gui.taskview.ScheduledTaskPanel: ...

    def getGroup(self) -> ghidra.framework.task.GTaskGroup: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setBackground(self, c: java.awt.Color) -> None:
        """
        sets the background of the component being managed by this info.  It is used by the animation
         framework.
        @param c the color
        """
        ...

    def setRunning(self) -> ghidra.framework.task.gui.GProgressBar: ...

    def setScrollFraction(self, fraction: float) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def background(self) -> None: ...  # No getter available.

    @background.setter
    def background(self, value: java.awt.Color) -> None: ...

    @property
    def component(self) -> ghidra.framework.task.gui.taskview.ScheduledTaskPanel: ...

    @property
    def group(self) -> ghidra.framework.task.GTaskGroup: ...

    @property
    def scrollFraction(self) -> None: ...  # No getter available.

    @scrollFraction.setter
    def scrollFraction(self, value: float) -> None: ...
