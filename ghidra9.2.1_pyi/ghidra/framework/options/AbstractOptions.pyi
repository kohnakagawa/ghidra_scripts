from typing import List
import ghidra.framework.options
import ghidra.util
import java.awt
import java.beans
import java.io
import java.lang
import java.util
import javax.swing


class AbstractOptions(object, ghidra.framework.options.Options):
    DELIMITER: int = '.'
    DELIMITER_STRING: unicode = u'.'
    ILLEGAL_DELIMITER: unicode = u'..'
    SUPPORTED_CLASSES: java.util.Set = [class java.lang.Double, class java.lang.Long, class java.lang.String, class java.lang.Boolean, class java.lang.Integer, class java.io.File, class java.lang.Float, class java.lang.Short, class java.lang.Byte, class java.awt.Font, class javax.swing.KeyStroke, class java.util.Date, class java.awt.Color]




    class AliasBinding(object):








        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

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







    def contains(self, optionName: unicode) -> bool: ...

    def createAlias(self, aliasName: unicode, options: ghidra.framework.options.Options, optionsName: unicode) -> None: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def findPropertyEditor(originalValueClass: java.lang.Class) -> java.beans.PropertyEditor: ...

    def getBoolean(self, optionName: unicode, defaultValue: bool) -> bool: ...

    def getByteArray(self, optionName: unicode, defaultValue: List[int]) -> List[int]: ...

    def getCategoryHelpLocation(self, categoryPath: unicode) -> ghidra.util.HelpLocation: ...

    def getChildOptions(self) -> List[ghidra.framework.options.Options]: ...

    def getClass(self) -> java.lang.Class: ...

    def getColor(self, optionName: unicode, defaultValue: java.awt.Color) -> java.awt.Color: ...

    def getCustomOption(self, optionName: unicode, defaultValue: ghidra.framework.options.CustomOption) -> ghidra.framework.options.CustomOption: ...

    def getDate(self, optionName: unicode, defaultValue: java.util.Date) -> java.util.Date: ...

    def getDefaultValue(self, optionName: unicode) -> object: ...

    def getDefaultValueAsString(self, optionName: unicode) -> unicode: ...

    def getDescription(self, optionName: unicode) -> unicode: ...

    def getDouble(self, optionName: unicode, defaultValue: float) -> float: ...

    def getEnum(self, __a0: unicode, __a1: java.lang.Enum) -> java.lang.Enum: ...

    def getFile(self, optionName: unicode, defaultValue: java.io.File) -> java.io.File: ...

    def getFloat(self, optionName: unicode, defaultValue: float) -> float: ...

    def getFont(self, optionName: unicode, defaultValue: java.awt.Font) -> java.awt.Font: ...

    def getHelpLocation(self, optionName: unicode) -> ghidra.util.HelpLocation: ...

    def getID(self, optionName: unicode) -> unicode: ...

    def getInt(self, optionName: unicode, defaultValue: int) -> int: ...

    def getKeyStroke(self, optionName: unicode, defaultValue: javax.swing.KeyStroke) -> javax.swing.KeyStroke: ...

    def getLeafOptionNames(self) -> List[unicode]: ...

    def getLong(self, optionName: unicode, defaultValue: long) -> long: ...

    def getName(self) -> unicode: ...

    def getObject(self, optionName: unicode, defaultValue: object) -> object: ...

    def getOption(self, optionName: unicode, type: ghidra.framework.options.OptionType, defaultValue: object) -> ghidra.framework.options.Option: ...

    def getOptionNames(self) -> List[unicode]: ...

    def getOptions(self, path: unicode) -> ghidra.framework.options.Options: ...

    @overload
    def getOptionsEditor(self) -> ghidra.framework.options.OptionsEditor: ...

    @overload
    def getOptionsEditor(self, categoryPath: unicode) -> ghidra.framework.options.OptionsEditor: ...

    def getOptionsHelpLocation(self) -> ghidra.util.HelpLocation: ...

    def getPropertyEditor(self, optionName: unicode) -> java.beans.PropertyEditor: ...

    def getRegisteredPropertyEditor(self, optionName: unicode) -> java.beans.PropertyEditor: ...

    def getString(self, optionName: unicode, defaultValue: unicode) -> unicode: ...

    def getType(self, optionName: unicode) -> ghidra.framework.options.OptionType: ...

    def getValueAsString(self, optionName: unicode) -> unicode: ...

    def hashCode(self) -> int: ...

    def isAlias(self, aliasName: unicode) -> bool: ...

    def isDefaultValue(self, optionName: unicode) -> bool: ...

    def isRegistered(self, optionName: unicode) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def putObject(self, optionName: unicode, newValue: object) -> None: ...

    @overload
    def putObject(self, optionName: unicode, newValue: object, type: ghidra.framework.options.OptionType) -> None: ...

    @overload
    def registerOption(self, optionName: unicode, defaultValue: object, help: ghidra.util.HelpLocation, description: unicode) -> None: ...

    @overload
    def registerOption(self, optionName: unicode, type: ghidra.framework.options.OptionType, defaultValue: object, help: ghidra.util.HelpLocation, description: unicode) -> None: ...

    @overload
    def registerOption(self, optionName: unicode, type: ghidra.framework.options.OptionType, defaultValue: object, help: ghidra.util.HelpLocation, description: unicode, editor: java.beans.PropertyEditor) -> None: ...

    @overload
    def registerOptionsEditor(self, editor: ghidra.framework.options.OptionsEditor) -> None: ...

    @overload
    def registerOptionsEditor(self, categoryPath: unicode, editor: ghidra.framework.options.OptionsEditor) -> None: ...

    def removeOption(self, optionName: unicode) -> None: ...

    def restoreDefaultValue(self, optionName: unicode) -> None: ...

    def restoreDefaultValues(self) -> None: ...

    def setBoolean(self, optionName: unicode, value: bool) -> None: ...

    def setByteArray(self, optionName: unicode, value: List[int]) -> None: ...

    def setCategoryHelpLocation(self, categoryPath: unicode, helpLocation: ghidra.util.HelpLocation) -> None: ...

    def setColor(self, optionName: unicode, value: java.awt.Color) -> None: ...

    def setCustomOption(self, optionName: unicode, value: ghidra.framework.options.CustomOption) -> None: ...

    def setDate(self, optionName: unicode, value: java.util.Date) -> None: ...

    def setDouble(self, optionName: unicode, value: float) -> None: ...

    def setEnum(self, __a0: unicode, __a1: java.lang.Enum) -> None: ...

    def setFile(self, optionName: unicode, value: java.io.File) -> None: ...

    def setFloat(self, optionName: unicode, value: float) -> None: ...

    def setFont(self, optionName: unicode, value: java.awt.Font) -> None: ...

    def setInt(self, optionName: unicode, value: int) -> None: ...

    def setKeyStroke(self, optionName: unicode, value: javax.swing.KeyStroke) -> None: ...

    def setLong(self, optionName: unicode, value: long) -> None: ...

    def setName(self, newName: unicode) -> None:
        """
        Sets the name for this Options object.  Used when updating old options names to new names.
        @param newName the new name for this options object.
        """
        ...

    def setOptionsHelpLocation(self, helpLocation: ghidra.util.HelpLocation) -> None: ...

    def setString(self, optionName: unicode, value: unicode) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def childOptions(self) -> List[object]: ...

    @property
    def leafOptionNames(self) -> List[object]: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def optionNames(self) -> List[object]: ...

    @property
    def optionsEditor(self) -> ghidra.framework.options.OptionsEditor: ...

    @property
    def optionsHelpLocation(self) -> ghidra.util.HelpLocation: ...

    @optionsHelpLocation.setter
    def optionsHelpLocation(self, value: ghidra.util.HelpLocation) -> None: ...
