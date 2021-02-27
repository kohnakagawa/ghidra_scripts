import docking.widgets.table.constraint
import ghidra.program.model.data
import java.lang


class DataTypeColumnTypeMapper(docking.widgets.table.constraint.ColumnTypeMapper):
    """
    Converts DataType Column objects to Strings so that column gets String type column
     filters
    """





    def __init__(self): ...



    @overload
    def convert(self, dataType: ghidra.program.model.data.DataType) -> unicode: ...

    @overload
    def convert(self, value: object) -> M:
        """
        Converts an object of type T1 to an object of type T2
        @param value the object to convert.
        @return the converted object.
        """
        ...

    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDestinationType(self) -> java.lang.Class:
        """
        Returns the class of the objects that this mapper will convert to.
        @return the class of the objects that this mapper will convert to.
        """
        ...

    def getSourceType(self) -> java.lang.Class:
        """
        Returns the class of the objects that this mapper will convert from.
        @return the class of the objects that this mapper will convert from.
        """
        ...

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
