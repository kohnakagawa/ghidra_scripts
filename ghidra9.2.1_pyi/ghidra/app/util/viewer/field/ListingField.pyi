import docking.widgets.fieldpanel.field
import docking.widgets.fieldpanel.internal
import docking.widgets.fieldpanel.support
import ghidra.app.util.viewer.field
import ghidra.app.util.viewer.format
import ghidra.app.util.viewer.proxy
import java.awt
import java.lang
import javax.swing


class ListingField(docking.widgets.fieldpanel.field.Field, object):
    """
    Interface that extends the Field interface to add addition information that
     the browser needs from the fields.
    """









    def contains(self, __a0: int, __a1: int) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getClickedObject(self, fieldLocation: docking.widgets.fieldpanel.support.FieldLocation) -> object:
        """
        Returns the object that was clicked on a Field for the given FieldLocation.  This may be the
         field itself or a lower-level entity, such as a FieldElement.
        @param fieldLocation The location that was clicked.
        @return the object that was clicked
        """
        ...

    def getCol(self, __a0: int, __a1: int) -> int: ...

    def getCursorBounds(self, __a0: int, __a1: int) -> java.awt.Rectangle: ...

    def getFieldFactory(self) -> ghidra.app.util.viewer.field.FieldFactory:
        """
        Returns the FieldFactory that generated this Field
        """
        ...

    def getFieldModel(self) -> ghidra.app.util.viewer.format.FieldFormatModel:
        """
        Returns the fieldModel that has the FieldFactory that generated this field.
        """
        ...

    def getHeight(self) -> int: ...

    def getHeightAbove(self) -> int:
        """
        Returns the height above the imaginary base line used for alignment of
         fields.
        """
        ...

    def getHeightBelow(self) -> int:
        """
        Returns the height below the imaginary base line used for alignment of
         fields.
        """
        ...

    def getNumCols(self, __a0: int) -> int: ...

    def getNumRows(self) -> int: ...

    def getPreferredWidth(self) -> int: ...

    def getProxy(self) -> ghidra.app.util.viewer.proxy.ProxyObj:
        """
        Returns the object that the fieldFactory used to generate the information
         in this field.
        """
        ...

    def getRow(self, __a0: int) -> int: ...

    def getScrollableUnitIncrement(self, __a0: int, __a1: int, __a2: int) -> int: ...

    def getStartX(self) -> int: ...

    def getText(self) -> unicode: ...

    def getTextWithLineSeparators(self) -> unicode: ...

    def getWidth(self) -> int: ...

    def getX(self, __a0: int, __a1: int) -> int: ...

    def getY(self, __a0: int) -> int: ...

    def hashCode(self) -> int: ...

    def isPrimary(self) -> bool: ...

    def isValid(self, __a0: int, __a1: int) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def paint(self, __a0: javax.swing.JComponent, __a1: java.awt.Graphics, __a2: docking.widgets.fieldpanel.internal.PaintContext, __a3: java.awt.Rectangle, __a4: docking.widgets.fieldpanel.internal.FieldBackgroundColorManager, __a5: docking.widgets.fieldpanel.support.RowColLocation, __a6: int) -> None: ...

    def rowHeightChanged(self, __a0: int, __a1: int) -> None: ...

    def screenLocationToTextOffset(self, __a0: int, __a1: int) -> int: ...

    def textOffsetToScreenLocation(self, __a0: int) -> docking.widgets.fieldpanel.support.RowColLocation: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def fieldFactory(self) -> ghidra.app.util.viewer.field.FieldFactory: ...

    @property
    def fieldModel(self) -> ghidra.app.util.viewer.format.FieldFormatModel: ...

    @property
    def height(self) -> int: ...

    @property
    def heightAbove(self) -> int: ...

    @property
    def heightBelow(self) -> int: ...

    @property
    def numRows(self) -> int: ...

    @property
    def preferredWidth(self) -> int: ...

    @property
    def primary(self) -> bool: ...

    @property
    def proxy(self) -> ghidra.app.util.viewer.proxy.ProxyObj: ...

    @property
    def startX(self) -> int: ...

    @property
    def text(self) -> unicode: ...

    @property
    def textWithLineSeparators(self) -> unicode: ...

    @property
    def width(self) -> int: ...
