import ghidra.app.util.html
import ghidra.program.model.data
import java.awt
import java.lang


class VariableTextLine(object, ghidra.app.util.html.ValidatableLine):
    INVALID_COLOR: java.awt.Color = java.awt.Color[r=255,g=0,b=0]



    def __init__(self, variableType: unicode, variableName: unicode, dataType: ghidra.program.model.data.DataType): ...



    def copy(self) -> ghidra.app.util.html.ValidatableLine: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataType(self) -> ghidra.program.model.data.DataType: ...

    def getText(self) -> unicode: ...

    def getVariableName(self) -> unicode: ...

    def getVariableNameColor(self) -> java.awt.Color: ...

    def getVariableType(self) -> unicode: ...

    def getVariableTypeColor(self) -> java.awt.Color: ...

    def hasUniversalId(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isDiffColored(self) -> bool: ...

    def isValidated(self) -> bool: ...

    def matches(self, otherValidatableLine: ghidra.app.util.html.ValidatableLine) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setValidationLine(self, line: ghidra.app.util.html.ValidatableLine) -> None: ...

    def toString(self) -> unicode: ...

    def updateColor(self, otherValidatableLine: ghidra.app.util.html.ValidatableLine, invalidColor: java.awt.Color) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def dataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def diffColored(self) -> bool: ...

    @property
    def text(self) -> unicode: ...

    @property
    def validated(self) -> bool: ...

    @property
    def validationLine(self) -> None: ...  # No getter available.

    @validationLine.setter
    def validationLine(self, value: ghidra.app.util.html.ValidatableLine) -> None: ...

    @property
    def variableName(self) -> unicode: ...

    @property
    def variableNameColor(self) -> java.awt.Color: ...

    @property
    def variableType(self) -> unicode: ...

    @property
    def variableTypeColor(self) -> java.awt.Color: ...
