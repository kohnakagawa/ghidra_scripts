import docking.widgets.fieldpanel.support
import ghidra.app.util
import ghidra.app.util.viewer.field
import ghidra.app.util.viewer.format
import ghidra.app.util.viewer.proxy
import ghidra.framework.options
import ghidra.program.util
import java.awt
import java.lang


class DummyFieldFactory(ghidra.app.util.viewer.field.FieldFactory):
    """
    Generates Dummy Fields.
    """





    def __init__(self, mgr: ghidra.app.util.viewer.format.FormatManager): ...



    def acceptsType(self, category: int, proxyObjectClass: java.lang.Class) -> bool: ...

    def displayOptionsChanged(self, options: ghidra.framework.options.Options, optionName: unicode, oldValue: object, newValue: object) -> None:
        """
        Notifications that the display options changed.
        @param options the Display Options object that changed.
        @param optionName the name of the property that changed.
        @param oldValue the old value of the property.
        @param newValue the new value of the property.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def fieldOptionsChanged(self, options: ghidra.framework.options.Options, optionName: unicode, oldValue: object, newValue: object) -> None:
        """
        Notifications that the field options changed.
        @param options the Field Options object that changed.
        @param optionName the name of the property that changed.
        @param oldValue the old value of the property.
        @param newValue the new value of the property.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultColor(self) -> java.awt.Color:
        """
        Returns the default field color.
        """
        ...

    def getField(self, obj: ghidra.app.util.viewer.proxy.ProxyObj, varWidth: int) -> ghidra.app.util.viewer.field.ListingField: ...

    def getFieldLocation(self, bf: ghidra.app.util.viewer.field.ListingField, index: long, fieldNum: int, loc: ghidra.program.util.ProgramLocation) -> docking.widgets.fieldpanel.support.FieldLocation: ...

    def getFieldModel(self) -> ghidra.app.util.viewer.format.FieldFormatModel:
        """
        Returns the FieldModel that this factory belongs to.
        """
        ...

    def getFieldName(self) -> unicode: ...

    def getFieldText(self) -> unicode: ...

    def getMetrics(self) -> java.awt.FontMetrics:
        """
        Returns the font metrics used by this field factory
        """
        ...

    def getProgramLocation(self, row: int, col: int, bf: ghidra.app.util.viewer.field.ListingField) -> ghidra.program.util.ProgramLocation: ...

    def getStartX(self) -> int:
        """
        Returns the starting x position for the fields generated by this
         factory.
        """
        ...

    def getWidth(self) -> int:
        """
        Returns the width of the fields generated by this factory.
        """
        ...

    def hashCode(self) -> int: ...

    def isEnabled(self) -> bool:
        """
        Returns true if this FieldFactory is currently enabled to generate Fields.
        """
        ...

    def newInstance(self, formatModel: ghidra.app.util.viewer.format.FieldFormatModel, hlProvdier: ghidra.app.util.HighlightProvider, displayOptions: ghidra.framework.options.ToolOptions, fieldOptions: ghidra.framework.options.ToolOptions) -> ghidra.app.util.viewer.field.FieldFactory: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def optionsChanged(self, options: ghidra.framework.options.Options, optionName: unicode, oldValue: object, newValue: object) -> None:
        """
        Notification that the Options have changed.
        @param options the Options object that changed. Will be either the display
         options or the field options.
        @param optionName the name of the property that changed.
        @param oldValue the old value of the property.
        @param newValue the new value of the property.
        """
        ...

    def servicesChanged(self) -> None:
        """
        Notification the services changed. Subclasses should override this method
         if they care about service changes.
        """
        ...

    def setEnabled(self, state: bool) -> None:
        """
        Turns on or off the generating of Fields by this FieldFactory.
        @param state if true, this factory will generate fields.
        """
        ...

    def setStartX(self, x: int) -> None:
        """
        Sets the starting x position for the fields generated by this factory.
        """
        ...

    def setWidth(self, w: int) -> None:
        """
        Sets the width of the fields generated by this factory.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def fieldName(self) -> unicode: ...

    @property
    def fieldText(self) -> unicode: ...
