import ghidra.docking.settings
import ghidra.util.exception
import ghidra.util.table.column
import ghidra.util.table.column.GColumnRenderer
import java.awt
import java.lang
import javax.swing


class AbstractWrapperTypeColumnRenderer(ghidra.util.table.column.GColumnRenderer, object):
    """
    A convenience interface of GColumnRenderer for primitive-based/wrapper-based
     renderers.   This class implements #getFilterString(Object, Settings) to
     throw an exception, as it should not be called for primitive types.

     The basic wrapper types, like Number, and some others, like Date, have special
     built-in filtering capabilities.  Columns whose column type is one of the wrapper classes
     will not have their #getFilterString(Object, Settings) methods called.  They can
     stub out those methods by throwing the exception returned by this method.
    """









    def createWrapperTypeException(self) -> ghidra.util.exception.AssertException: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getColumnConstraintFilterMode(self) -> ghidra.util.table.column.GColumnRenderer.ColumnConstraintFilterMode: ...

    def getFilterString(self, t: object, settings: ghidra.docking.settings.Settings) -> unicode: ...

    def getTableCellRendererComponent(self, __a0: javax.swing.JTable, __a1: object, __a2: bool, __a3: bool, __a4: int, __a5: int) -> java.awt.Component: ...

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

    @property
    def columnConstraintFilterMode(self) -> ghidra.util.table.column.GColumnRenderer.ColumnConstraintFilterMode: ...
