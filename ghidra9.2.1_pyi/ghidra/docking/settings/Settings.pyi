from typing import List
import ghidra.docking.settings
import java.lang


class Settings(object):
    """
    Settings objects store name-value pairs.  Each SettingsDefinition defines one
     or more names to use to store values in settings objects.  Exactly what type
     of value and how to interpret the value is done by the SettingsDefinition object.
    """









    def clearAllSettings(self) -> None:
        """
        Removes all name-value pairs from this settings object
        """
        ...

    def clearSetting(self, name: unicode) -> None:
        """
        Removes any value associated with the given name
        @param name the key to remove any association
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getByteArray(self, name: unicode) -> List[int]:
        """
        Gets the byte[] value associated with the given name
        @param name the key used to retrieve a value
        @return the byte[] value for a key
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultSettings(self) -> ghidra.docking.settings.Settings:
        """
        Returns the underlying default settings for these settings or null if there are none
        """
        ...

    def getLong(self, name: unicode) -> long:
        """
        Gets the Long value associated with the given name
        @param name the key used to retrieve a value
        @return the Long value for a key
        """
        ...

    def getNames(self) -> List[unicode]:
        """
        Get this list of keys that currently have values associated with them
        @return an array of string keys.
        """
        ...

    def getString(self, name: unicode) -> unicode:
        """
        Gets the String value associated with the given name
        @param name the key used to retrieve a value
        @return the String value for a key
        """
        ...

    def getValue(self, name: unicode) -> object:
        """
        Gets the object associated with the given name
        @param name the key used to retrieve a value
        @return the object associated with a given key
        """
        ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool:
        """
        Returns true if there are no key-value pairs stored in this settings object
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setByteArray(self, name: unicode, value: List[int]) -> None:
        """
        Associates the given byte[] with the name
        @param name the key
        @param value the value associated with the key
        """
        ...

    def setLong(self, name: unicode, value: long) -> None:
        """
        Associates the given long value with the name
        @param name the key
        @param value the value associated with the key
        """
        ...

    def setString(self, name: unicode, value: unicode) -> None:
        """
        Associates the given String value with the name
        @param name the key
        @param value the value associated with the key
        """
        ...

    def setValue(self, name: unicode, value: object) -> None:
        """
        Associates the given object with the name
        @param name the key
        @param value the value to associate with the key
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
    def defaultSettings(self) -> ghidra.docking.settings.Settings: ...

    @property
    def empty(self) -> bool: ...

    @property
    def names(self) -> List[unicode]: ...
