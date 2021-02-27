import docking.widgets.table.constraint
import java.lang
import java.util


class ProgramColumnConstraintProvider(object, docking.widgets.table.constraint.ColumnConstraintProvider):
    """
    Class for providing Program related column type constraints.  Addresses get converted to
     UnsignedLong (via BigInteger) and many others get converted to Strings.  For example, some
     tables have a column whose type is "Symbol", but the column just displays the symbol's name.
     So we created a number of "Symbol" constraints, but they are just adapters to the
     various String constraints.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getColumnConstraints(self) -> java.util.Collection: ...

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
    def columnConstraints(self) -> java.util.Collection: ...
