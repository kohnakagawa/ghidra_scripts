import docking.widgets.fieldpanel.field
import docking.widgets.fieldpanel.internal
import docking.widgets.fieldpanel.support
import ghidra.app.util.viewer.field
import ghidra.app.util.viewer.format
import ghidra.app.util.viewer.proxy
import java.awt
import java.lang
import javax.swing


class ImageFactoryField(docking.widgets.fieldpanel.field.SimpleImageField, ghidra.app.util.viewer.field.ListingField):
    """
    Class for displaying images in fields.
    """





    @overload
    def __init__(self, factory: ghidra.app.util.viewer.field.FieldFactory, icon: javax.swing.ImageIcon, proxy: ghidra.app.util.viewer.proxy.ProxyObj, metrics: java.awt.FontMetrics, x: int, width: int):
        """
        Constructor
        @param factory the FieldFactory that generated this field.
        @param icon the ImageIcon to display.
        @param proxy the object that this field represents.
        @param metrics the FontMetrics used to render.
        @param x the starting x position for this field.
        @param width the width of this field.
        """
        ...

    @overload
    def __init__(self, factory: ghidra.app.util.viewer.field.FieldFactory, icon: javax.swing.ImageIcon, proxy: ghidra.app.util.viewer.proxy.ProxyObj, metrics: java.awt.FontMetrics, x: int, width: int, center: bool):
        """
        Constructor
        @param factory the FieldFactory that generated this field.
        @param icon the ImageIcon to display.
        @param proxy the object that this field represents.
        @param metrics the FontMetrics used to render.
        @param x the starting x position for this field.
        @param width the width of this field.
        @param center centers the image if true.
        """
        ...



    def contains(self, x: int, y: int) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getClickedObject(self, fieldLocation: docking.widgets.fieldpanel.support.FieldLocation) -> object:
        """
        @see ListingField#getClickedObject(FieldLocation)
        """
        ...

    def getCol(self, row: int, x: int) -> int: ...

    def getCursorBounds(self, row: int, col: int) -> java.awt.Rectangle: ...

    def getFieldFactory(self) -> ghidra.app.util.viewer.field.FieldFactory:
        """
        Returns the FieldFactory that generated this Field.
        """
        ...

    def getFieldModel(self) -> ghidra.app.util.viewer.format.FieldFormatModel:
        """
        Returns the model that contains the FieldFactory that generated this Field.
        """
        ...

    def getHeight(self) -> int: ...

    def getHeightAbove(self) -> int: ...

    def getHeightBelow(self) -> int: ...

    def getNumCols(self, row: int) -> int: ...

    def getNumRows(self) -> int: ...

    def getPreferredWidth(self) -> int: ...

    def getProxy(self) -> ghidra.app.util.viewer.proxy.ProxyObj:
        """
        Returns the object that this field is associated with.
        """
        ...

    def getRow(self, y: int) -> int: ...

    def getScrollableUnitIncrement(self, topOfScreen: int, direction: int, max: int) -> int: ...

    def getStartX(self) -> int: ...

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

    def setPrimary(self, state: bool) -> None:
        """
        Sets the primary state of this field
        @param state true if this field is primary, false otherwise.
        """
        ...

    def textOffsetToScreenLocation(self, textOffset: int) -> docking.widgets.fieldpanel.support.RowColLocation: ...

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
    def proxy(self) -> ghidra.app.util.viewer.proxy.ProxyObj: ...
