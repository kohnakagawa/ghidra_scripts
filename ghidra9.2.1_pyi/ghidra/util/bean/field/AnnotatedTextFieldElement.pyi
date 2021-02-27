from typing import List
import docking.widgets.fieldpanel.field
import docking.widgets.fieldpanel.support
import ghidra.app.nav
import ghidra.framework.plugintool
import java.awt
import java.lang
import javax.swing


class AnnotatedTextFieldElement(docking.widgets.fieldpanel.field.AbstractTextFieldElement):
    """
    A subclass of FieldElement that allows for mouse handling callbacks via the
     #handleMouseClicked(Navigatable, ServiceProvider) method.  This class
     is based upon Annotation objects, which are elements that perform actions when the
     use clicks an instance of this class in the display.
    """





    def __init__(self, annotation: ghidra.app.util.viewer.field.Annotation, row: int, column: int):
        """
        Constructor that initializes this text field element with the given annotation and row
         and column information.  The text of this element is the text returned from
         {@link Annotation#getDisplayString()}.
        @param annotation The Annotation that this element is describing.
        @param row The row that this element is on
        @param column The column value of this element (the column index where this element starts)
        """
        ...



    def charAt(self, index: int) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getCharacterIndexForDataLocation(self, dataRow: int, dataColumn: int) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getColor(self, charIndex: int) -> java.awt.Color: ...

    def getDataLocationForCharacterIndex(self, characterIndex: int) -> docking.widgets.fieldpanel.support.RowColLocation: ...

    def getFieldElement(self, characterOffset: int) -> docking.widgets.fieldpanel.field.FieldElement: ...

    def getHeightAbove(self) -> int: ...

    def getHeightBelow(self) -> int: ...

    def getMaxCharactersForWidth(self, width: int) -> int: ...

    def getRawText(self) -> unicode:
        """
        Returns the original annotation text in the data model, which will differ from the display
         text.
        @return the original annotation text in the data model.
        """
        ...

    def getStringWidth(self) -> int: ...

    def getText(self) -> unicode: ...

    def handleMouseClicked(self, sourceNavigatable: ghidra.app.nav.Navigatable, serviceProvider: ghidra.framework.plugintool.ServiceProvider) -> bool:
        """
        This method is designed to be called when a mouse click has occurred for a given
         {@link ProgramLocation}.
        @param sourceNavigatable The source Navigatable
        @param serviceProvider A service provider from which system resources can be retrieved
        @return true if this string handles the mouse click.
        """
        ...

    def hashCode(self) -> int: ...

    def length(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def paint(self, c: javax.swing.JComponent, g: java.awt.Graphics, x: int, y: int) -> None: ...

    def replaceAll(self, targets: List[int], replacement: int) -> docking.widgets.fieldpanel.field.FieldElement: ...

    @overload
    def substring(self, start: int) -> docking.widgets.fieldpanel.field.FieldElement: ...

    @overload
    def substring(self, start: int, end: int) -> docking.widgets.fieldpanel.field.FieldElement: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def rawText(self) -> unicode: ...
