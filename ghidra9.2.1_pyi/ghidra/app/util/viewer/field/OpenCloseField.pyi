import docking.widgets.fieldpanel.internal
import docking.widgets.fieldpanel.support
import ghidra.app.util.viewer.field
import ghidra.app.util.viewer.format
import ghidra.app.util.viewer.proxy
import java.awt
import java.lang
import javax.swing


class OpenCloseField(object, ghidra.app.util.viewer.field.ListingField):
    """
    FactoryField class for displaying the open/close field.
    """





    def __init__(self, factory: ghidra.app.util.viewer.field.FieldFactory, proxy: ghidra.app.util.viewer.proxy.ProxyObj, indentLevel: int, metrics: java.awt.FontMetrics, x: int, width: int, isLast: bool):
        """
        Constructor
        @param factory the FieldFactory that created this field.
        @param proxy the object associated with this field.
        @param indentLevel the indentation level of the data object.
        @param metrics the FontMetrics used to render this field.
        @param x the starting x position of this field.
        @param width the width of this field.
        @param isLast true if the data object is the last subcomponent at its level.
        """
        ...



    def contains(self, x: int, y: int) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getClickedObject(self, fieldLocation: docking.widgets.fieldpanel.support.FieldLocation) -> object: ...

    def getCol(self, row: int, x: int) -> int: ...

    def getCursorBounds(self, row: int, col: int) -> java.awt.Rectangle: ...

    def getFieldFactory(self) -> ghidra.app.util.viewer.field.FieldFactory: ...

    def getFieldModel(self) -> ghidra.app.util.viewer.format.FieldFormatModel: ...

    def getHeight(self) -> int: ...

    def getHeightAbove(self) -> int: ...

    def getHeightBelow(self) -> int: ...

    def getNumCols(self, row: int) -> int: ...

    def getNumRows(self) -> int: ...

    def getPreferredWidth(self) -> int: ...

    def getProxy(self) -> ghidra.app.util.viewer.proxy.ProxyObj: ...

    def getRow(self, y: int) -> int: ...

    def getScrollableUnitIncrement(self, topOfScreen: int, direction: int, max: int) -> int: ...

    def getStartX(self) -> int: ...

    def getStartY(self) -> int:
        """
        Returns the vertical position of this field.
        """
        ...

    def getText(self) -> unicode: ...

    def getTextWithLineSeparators(self) -> unicode: ...

    def getWidth(self) -> int: ...

    def getX(self, row: int, col: int) -> int: ...

    def getY(self, row: int) -> int: ...

    def hashCode(self) -> int: ...

    def isPrimary(self) -> bool: ...

    def isValid(self, row: int, col: int) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def paint(self, c: javax.swing.JComponent, g: java.awt.Graphics, context: docking.widgets.fieldpanel.internal.PaintContext, clip: java.awt.Rectangle, map: docking.widgets.fieldpanel.internal.FieldBackgroundColorManager, cursorLoc: docking.widgets.fieldpanel.support.RowColLocation, rowHeight: int) -> None: ...

    def rowHeightChanged(self, newHeightAbove: int, newHeightBelow: int) -> None: ...

    def screenLocationToTextOffset(self, row: int, col: int) -> int: ...

    def setStartY(self, startY: int) -> None:
        """
        Sets the starting vertical position of this field.
        @param startY the starting vertical position.
        """
        ...

    def setYPos(self, yPos: int, heightAbove: int, heightBelow: int) -> None:
        """
        Sets the yPos relative to the overall layout.
        @param yPos the starting Ypos of the layout row.
        @param heightAbove the heightAbove the alignment line in the layout row.
        @param heightBelow the heightBelow the alignment line in the layout row.
        """
        ...

    def textOffsetToScreenLocation(self, textOffset: int) -> docking.widgets.fieldpanel.support.RowColLocation: ...

    def toString(self) -> unicode: ...

    def toggleOpenCloseState(self) -> None:
        """
        Toggles the open state of this field.
        """
        ...

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
    def startY(self) -> int: ...

    @startY.setter
    def startY(self, value: int) -> None: ...

    @property
    def text(self) -> unicode: ...

    @property
    def textWithLineSeparators(self) -> unicode: ...

    @property
    def width(self) -> int: ...
