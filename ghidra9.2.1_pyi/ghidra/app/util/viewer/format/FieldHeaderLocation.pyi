import ghidra.app.util.viewer.field
import ghidra.app.util.viewer.format
import java.lang


class FieldHeaderLocation(object):
    """
    Class used to represent a location within the field header component.
    """





    def __init__(self, model: ghidra.app.util.viewer.format.FieldFormatModel, factory: ghidra.app.util.viewer.field.FieldFactory, row: int, col: int):
        """
        Construct a new FieldHeaderLocation
        @param model the model containing this location
        @param factory the factory the containing this location.
        @param row the row containing the factory in the header
        @param col the column containing the factory in the header.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getColumn(self) -> int:
        """
        Returns the header column for this location.
        """
        ...

    def getFieldFactory(self) -> ghidra.app.util.viewer.field.FieldFactory:
        """
        Returns the field factory for this location.
        """
        ...

    def getModel(self) -> ghidra.app.util.viewer.format.FieldFormatModel:
        """
        Returns the FieldFormatModel for this location.
        """
        ...

    def getRow(self) -> int:
        """
        Returns the header row for this location.
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

    @property
    def column(self) -> int: ...

    @property
    def fieldFactory(self) -> ghidra.app.util.viewer.field.FieldFactory: ...

    @property
    def model(self) -> ghidra.app.util.viewer.format.FieldFormatModel: ...

    @property
    def row(self) -> int: ...
