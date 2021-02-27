from typing import List
import ghidra.framework.options
import ghidra.util
import java.awt
import java.beans
import java.io
import java.lang
import java.util
import javax.swing


class Options(object):
    DELIMITER: int = '.'
    DELIMITER_STRING: unicode = u'.'
    ILLEGAL_DELIMITER: unicode = u'..'







    def contains(self, optionName: unicode) -> bool:
        """
        Return true if a option exists with the given name.
        @param optionName option name
        """
        ...

    def createAlias(self, aliasName: unicode, options: ghidra.framework.options.Options, optionsName: unicode) -> None:
        """
        Create an alias in this options for an existing option in some other options object.
        @param aliasName the name within this options object that will acutally refer to some other options object.
        @param options the options object that has the actual option.
        @param optionsName the name within the given options object of the actual option.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getBoolean(self, optionName: unicode, defaultValue: bool) -> bool:
        """
        Get the boolean value for the given option name.
        @param optionName option name
        @param defaultValue value that is stored and returned if there
         is no option with the given name.
        @return boolean option value
        """
        ...

    def getByteArray(self, optionName: unicode, defaultValue: List[int]) -> List[int]:
        """
        Get the byte array for the given option name.
        @param optionName option name
        @param defaultValue value that is stored and returned if there
         is no option with the given name
        @return byte[] byte array value
        """
        ...

    def getChildOptions(self) -> List[ghidra.framework.options.Options]:
        """
        Returns a list of Options objects that are nested one level down from this Options object.
        @return a list of Options objects that are nested one level down from this Options object.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getColor(self, optionName: unicode, defaultValue: java.awt.Color) -> java.awt.Color:
        """
        Get the Color for the given option name.
        @param optionName option name
        @param defaultValue value that is stored and returned if there is no
         option with the given name
        @return Color option
        @throws IllegalArgumentException is a option exists with the given
         name but it is not a Color
        """
        ...

    def getCustomOption(self, optionName: unicode, defaultValue: ghidra.framework.options.CustomOption) -> ghidra.framework.options.CustomOption:
        """
        Get the custom option value for the given option name.
        @param optionName option name
        @param defaultValue value that is stored and returned if there
         is no option with the given name
        @return WrappedOption value for the option
        """
        ...

    def getDate(self, pName: unicode, date: java.util.Date) -> java.util.Date:
        """
        Get the Date for the given option name.
        @param pName the property name
        @param date the default date that is stored and returned if there is no
         option with the given name
        @return the Date for the option
        @throws IllegalArgumentException is a option exists with the given
         name but it is not a Date options
        """
        ...

    def getDefaultValue(self, optionName: unicode) -> object:
        """
        Returns the default value for the given option.
        @param optionName the name of the option for which to retrieve the default value.
        @return the default value for the given option.
        """
        ...

    def getDefaultValueAsString(self, optionName: unicode) -> unicode:
        """
        Returns the default value as a string for the given option.
        @param optionName the name of the option for which to retrieve the default value as a string
        @return the default value as a string for the given option.
        """
        ...

    def getDescription(self, optionName: unicode) -> unicode:
        """
        Get the description for the given option name.
        @param optionName name of the option
        @return null if the description or option name does not exist
        """
        ...

    def getDouble(self, optionName: unicode, defaultValue: float) -> float:
        """
        Get the double value for the given option name.
        @param optionName option name
        @param defaultValue value that is stored and returned if there
         is no option with the given name
        @return double value for the option
        """
        ...

    def getEnum(self, __a0: unicode, __a1: java.lang.Enum) -> java.lang.Enum: ...

    def getFile(self, optionName: unicode, defaultValue: java.io.File) -> java.io.File:
        """
        Get the File for the given option name.
        @param optionName option name
        @param defaultValue value that is stored and returned if there is no
         option with the given name
        @return File option
        @throws IllegalArgumentException is a option exists with the given
         name but it is not a File options
        """
        ...

    def getFloat(self, optionName: unicode, defaultValue: float) -> float:
        """
        Get the float value for the given option name.
        @param optionName option name
        @param defaultValue value that is stored and returned if there
         is no option with the given name
        @return float value for the option
        """
        ...

    def getFont(self, optionName: unicode, defaultValue: java.awt.Font) -> java.awt.Font:
        """
        Get the Font for the given option name.
        @param optionName option name
        @param defaultValue value that is stored and returned if there is no
         option with the given name
        @return Font option
        @throws IllegalArgumentException is a option exists with the given
         name but it is not a Font
        """
        ...

    def getHelpLocation(self, optionName: unicode) -> ghidra.util.HelpLocation:
        """
        Get the location for where help can be found for the option with
         the given name.
        @param optionName name of the option
        @return null if the help location was not set on the option
        """
        ...

    def getID(self, optionName: unicode) -> unicode:
        """
        Returns a unique id for option in this options with the given name.  This will be the full
         path name to the root options object.
        @param optionName the name of the option for which to get an ID;
        @return the unique ID for the given option.
        """
        ...

    def getInt(self, optionName: unicode, defaultValue: int) -> int:
        """
        Get the int value for the given option name.
        @param optionName option name
        @param defaultValue value that is stored and returned if there
         is no option with the given name
        @return int option value
        """
        ...

    def getKeyStroke(self, optionName: unicode, defaultValue: javax.swing.KeyStroke) -> javax.swing.KeyStroke:
        """
        Get the KeyStrokg for the given action name.
        @param optionName the option name
        @param defaultValue value that is stored and returned if there is no
         option with the given name
        @return KeyStroke option
        @throws IllegalArgumentException is a option exists with the given
         name but it is not a KeyStroke
        """
        ...

    def getLeafOptionNames(self) -> List[unicode]:
        """
        Returns a list of option names that immediately fall under this options.  For example, if this options
         object had the following options named ("a", "b", "c.d"), only "a" and "b" would be returned.  The
         "c.d" leaf option name could be returned by getOptions("c").getLeafOptionNames()
        @return the list of the names of the options that are immediate children of this options object.
        """
        ...

    def getLong(self, optionName: unicode, defaultValue: long) -> long:
        """
        Get the long value for the given option name.
        @param optionName option name
        @param defaultValue value that is stored and returned if there
         is no option with the given name
        @return long value for the option
        """
        ...

    def getName(self) -> unicode:
        """
        Get the name of this options object.
        @return String
        """
        ...

    def getObject(self, optionName: unicode, defaultValue: object) -> object:
        """
        Get the object value; called when the options dialog is being
         populated.
        @param optionName option name
        @param defaultValue default value
        @return object with the given option name; if no option was found,
         return default value (this value is not stored in the option maps)
        """
        ...

    def getOptionNames(self) -> List[unicode]:
        """
        Get the list of option names. This method will return the names (paths) of all options contained
         in this options object or below.  For example, if the options has ("aaa", "bbb", "ccc.ddd"),
         all three will be returned.  the {@link Options#getLeafOptionNames()} method will return only
         the "aaa" and "bbb" names.
        @return the list of all option names(paths) under this options.
        """
        ...

    def getOptions(self, path: unicode) -> ghidra.framework.options.Options:
        """
        Returns a Options object that is a sub-options of this options.
        @param path the path for the sub-options object.
        @return a Options object that is a sub-options of this options.
        """
        ...

    def getOptionsEditor(self) -> ghidra.framework.options.OptionsEditor:
        """
        Get the editor that will handle editing all the values in this options or sub group of options.
        @return null if no options editor was registered
        """
        ...

    def getOptionsHelpLocation(self) -> ghidra.util.HelpLocation:
        """
        Returns the HelpLocation for this entire Options object.
        @return the HelpLocation for this entire Options object.
        """
        ...

    def getPropertyEditor(self, optionName: unicode) -> java.beans.PropertyEditor:
        """
        Get the property editor for the option with the given name. Note: This method must be called
         from the swing thread.
        @return either the PropertyEditor that was registered for this option or a default editor
         for the property type if one can be found; otherwise null.
        @throws IllegalStateException if not called from the swing thread.
        """
        ...

    def getRegisteredPropertyEditor(self, optionName: unicode) -> java.beans.PropertyEditor:
        """
        Get the property editor that was registered for the specific option with the given name.  Unlike
         the getPropertyEditor() method, this method does not have to be called from the swing thread
        @return the PropertyEditor that was registered for this option.
        """
        ...

    def getString(self, optionName: unicode, defaultValue: unicode) -> unicode:
        """
        Get the string value for the given option name.
        @param optionName option name
        @param defaultValue value that is stored and returned if there is no
         option with the given name
        @return String value for the option
        """
        ...

    def getType(self, optionName: unicode) -> ghidra.framework.options.OptionType:
        """
        Returns the OptionType of the given option.
        @param optionName the name of the option for which to get the type.
        @return the OptionType of option with the given name.
        """
        ...

    def getValueAsString(self, name: unicode) -> unicode:
        """
        Returns the value as a string for the given option.
        @param name the name of the option for which to retrieve the value as a string
        @return the value as a string for the given option.
        """
        ...

    def hashCode(self) -> int: ...

    def isAlias(self, aliasName: unicode) -> bool:
        """
        Returns
        @param aliasName the name of the alias.
        @return a Options object that is a sub-options of this options.
        """
        ...

    def isDefaultValue(self, optionName: unicode) -> bool:
        """
        Returns true if the option with the given name's current value is the default value.
        @param optionName the name of the option.
        @return true if the options has its current value equal to its default value.
        """
        ...

    def isRegistered(self, optionName: unicode) -> bool:
        """
        Returns true if the specified option has been registered.  Only registered names
         are saved.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def putObject(self, optionName: unicode, obj: object) -> None:
        """
        Put the object value.  If the option exists, the type must match the type of the existing
         object.
        @throws IllegalStateException if the object does not match the existing type of the option.
        @throws IllegalArgumentException if the object is null or not a supported type.
        """
        ...

    @overload
    def registerOption(self, optionName: unicode, defaultValue: object, help: ghidra.util.HelpLocation, description: unicode) -> None:
        """
        Registers an option with a description, help location, and a default value without specifying
         the option type.  This form requires that the default value not be null so that the option
         type can be inferred from the default value.
        @param optionName the name of the option being registered.
        @param defaultValue the defaultValue for the option. The default value must not be
         null so that the OptionType can be determined.  If the default value should be null, use
         {@link #registerOption(String, OptionType, Object, HelpLocation, String)}
        @param help the HelpLocation for this option.
        @param description a description of the option.
        @throws IllegalArgumentException if the defaultValue is null
        """
        ...

    @overload
    def registerOption(self, optionName: unicode, type: ghidra.framework.options.OptionType, defaultValue: object, help: ghidra.util.HelpLocation, description: unicode) -> None:
        """
        Registers an option with a description, help location, and a optional default value.  With an optional
         default value, an OptionType must be passed as it is otherwise derived from the default value.
        @param optionName the name of the option being registered.
        @param type the OptionType for this options.
        @param defaultValue the defaultValue for the option. In this version of the method, the default
         value may be null.
        @param help the HelpLocation for this option.
        @param description a description of the option.
        """
        ...

    @overload
    def registerOption(self, optionName: unicode, type: ghidra.framework.options.OptionType, defaultValue: object, help: ghidra.util.HelpLocation, description: unicode, editor: java.beans.PropertyEditor) -> None:
        """
        Registers an option with a description, help location, and a optional default value.  With an optional
         default value, an OptionType must be passed as it is otherwise derived from the default value.
        @param optionName the name of the option being registered.
        @param type the OptionType for this options.
        @param defaultValue the defaultValue for the option. In this version of the method, the default
         value may be null.
        @param help the HelpLocation for this option.
        @param description a description of the option.
        @param editor an optional custom editor for this property. Note if the option is a custom option,
         then the property editor can't be null;
        @throws IllegalStateException if the options is a custom option and the editor is null.
        """
        ...

    def registerOptionsEditor(self, editor: ghidra.framework.options.OptionsEditor) -> None:
        """
        Register the options editor that will handle the editing for all the options or a sub group of options.
        @param editor the custom editor panel to be used to edit the options or sub group of options.
        """
        ...

    def removeOption(self, optionName: unicode) -> None:
        """
        Remove the option name.
        @param optionName name of option to remove
        """
        ...

    def restoreDefaultValue(self, optionName: unicode) -> None:
        """
        Restores the option denoted by the given name to its default value.
        @param optionName The name of the option to restore
        @see #restoreDefaultValues()
        """
        ...

    def restoreDefaultValues(self) -> None:
        """
        Restores <b>all</b> options contained herein to their default values.
        @see #restoreDefaultValue(String)
        """
        ...

    def setBoolean(self, optionName: unicode, value: bool) -> None:
        """
        Sets the boolean value for the option.
        @param optionName name of the option
        @param value value of the option
        """
        ...

    def setByteArray(self, optionName: unicode, value: List[int]) -> None:
        """
        Sets the byte[] value for the given option name.
        @param optionName the name of the option on which to save bytes.
        @param value
        """
        ...

    def setColor(self, optionName: unicode, value: java.awt.Color) -> None:
        """
        Sets the Color value for the option
        @param optionName name of the option
        @param value Color to set
        @throws IllegalArgumentException if a option with the given
         name already exists, but it is not a Color
        """
        ...

    def setCustomOption(self, optionName: unicode, value: ghidra.framework.options.CustomOption) -> None:
        """
        Sets the Custom option value for the option.
        @param optionName name of the option
        @param value
        """
        ...

    def setDate(self, optionName: unicode, newSetting: java.util.Date) -> None:
        """
        Sets the Date value for the option.
        @param optionName name of the option
        @param newSetting the Date to set
        """
        ...

    def setDouble(self, optionName: unicode, value: float) -> None:
        """
        Sets the double value for the option.
        @param optionName name of the option
        @param value value of the option
        """
        ...

    def setEnum(self, __a0: unicode, __a1: java.lang.Enum) -> None: ...

    def setFile(self, optionName: unicode, value: java.io.File) -> None:
        """
        Sets the File value for the option.
        @param optionName name of the option
        @param value
        """
        ...

    def setFloat(self, optionName: unicode, value: float) -> None:
        """
        Sets the float value for the option.
        @param optionName name of the option
        @param value value of the option
        """
        ...

    def setFont(self, optionName: unicode, value: java.awt.Font) -> None:
        """
        Sets the Font value for the option
        @param optionName name of the option
        @param value Font to set
        @throws IllegalArgumentException if a option with the given
         name already exists, but it is not a Font
        """
        ...

    def setInt(self, optionName: unicode, value: int) -> None:
        """
        Sets the int value for the option.
        @param optionName name of the option
        @param value value of the option
        """
        ...

    def setKeyStroke(self, optionName: unicode, value: javax.swing.KeyStroke) -> None:
        """
        Sets the KeyStroke value for the option
        @param optionName name of the option
        @param value KeyStroke to set
        @throws IllegalArgumentException if a option with the given
         name already exists, but it is not a KeyStroke
        """
        ...

    def setLong(self, optionName: unicode, value: long) -> None:
        """
        Sets the long value for the option.
        @param optionName name of the option
        @param value value of the option
        """
        ...

    def setOptionsHelpLocation(self, helpLocation: ghidra.util.HelpLocation) -> None:
        """
        Set the location for where help can be found for this entire options object.
        @param helpLocation location for help on the option
        """
        ...

    def setString(self, optionName: unicode, value: unicode) -> None:
        """
        Set the String value for the option.
        @param optionName name of the option
        @param value value of the option
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
    def childOptions(self) -> List[object]: ...

    @property
    def leafOptionNames(self) -> List[object]: ...

    @property
    def name(self) -> unicode: ...

    @property
    def optionNames(self) -> List[object]: ...

    @property
    def optionsEditor(self) -> ghidra.framework.options.OptionsEditor: ...

    @property
    def optionsHelpLocation(self) -> ghidra.util.HelpLocation: ...

    @optionsHelpLocation.setter
    def optionsHelpLocation(self, value: ghidra.util.HelpLocation) -> None: ...
