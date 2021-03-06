import docking.widgets.fieldpanel.support
import ghidra.app.util
import ghidra.app.util.viewer.field
import ghidra.app.util.viewer.format
import ghidra.app.util.viewer.proxy
import ghidra.framework.options
import ghidra.program.util
import java.awt
import java.lang


class StackDepthFieldFactory(ghidra.app.util.viewer.field.FieldFactory):
    FIELD_NAME: unicode = u'Stack Depth'



    def __init__(self): ...



    def acceptsType(self, __a0: int, __a1: java.lang.Class) -> bool: ...

    def displayOptionsChanged(self, __a0: ghidra.framework.options.Options, __a1: unicode, __a2: object, __a3: object) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def fieldOptionsChanged(self, __a0: ghidra.framework.options.Options, __a1: unicode, __a2: object, __a3: object) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultColor(self) -> java.awt.Color: ...

    def getField(self, __a0: ghidra.app.util.viewer.proxy.ProxyObj, __a1: int) -> ghidra.app.util.viewer.field.ListingField: ...

    def getFieldLocation(self, __a0: ghidra.app.util.viewer.field.ListingField, __a1: long, __a2: int, __a3: ghidra.program.util.ProgramLocation) -> docking.widgets.fieldpanel.support.FieldLocation: ...

    def getFieldModel(self) -> ghidra.app.util.viewer.format.FieldFormatModel: ...

    def getFieldName(self) -> unicode: ...

    def getFieldText(self) -> unicode: ...

    def getMetrics(self) -> java.awt.FontMetrics: ...

    def getProgramLocation(self, __a0: int, __a1: int, __a2: ghidra.app.util.viewer.field.ListingField) -> ghidra.program.util.ProgramLocation: ...

    def getStartX(self) -> int: ...

    def getWidth(self) -> int: ...

    def hashCode(self) -> int: ...

    def isEnabled(self) -> bool: ...

    def newInstance(self, __a0: ghidra.app.util.viewer.format.FieldFormatModel, __a1: ghidra.app.util.HighlightProvider, __a2: ghidra.framework.options.ToolOptions, __a3: ghidra.framework.options.ToolOptions) -> ghidra.app.util.viewer.field.FieldFactory: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def optionsChanged(self, __a0: ghidra.framework.options.Options, __a1: unicode, __a2: object, __a3: object) -> None: ...

    def servicesChanged(self) -> None: ...

    def setEnabled(self, __a0: bool) -> None: ...

    def setStartX(self, __a0: int) -> None: ...

    def setWidth(self, __a0: int) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
