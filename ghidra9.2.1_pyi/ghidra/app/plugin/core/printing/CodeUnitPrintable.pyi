import java.awt
import java.awt.print
import java.lang


class CodeUnitPrintable(object, java.awt.print.Printable):
    NO_SUCH_PAGE: int = 1
    PAGE_EXISTS: int = 0



    @overload
    def __init__(self, __a0: docking.widgets.fieldpanel.LayoutModel, __a1: List[object], __a2: float, __a3: ghidra.util.task.TaskMonitor, __a4: ghidra.app.plugin.core.printing.PrintOptionsDialog, __a5: java.awt.print.Book, __a6: java.awt.print.PrinterJob, __a7: java.util.Date): ...

    @overload
    def __init__(self, __a0: docking.widgets.fieldpanel.LayoutModel, __a1: int, __a2: int, __a3: float, __a4: ghidra.util.task.TaskMonitor, __a5: ghidra.app.plugin.core.printing.PrintOptionsDialog, __a6: java.awt.print.Book, __a7: java.awt.print.PrinterJob, __a8: java.util.Date): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def print(self, __a0: java.awt.Graphics, __a1: java.awt.print.PageFormat, __a2: int) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
