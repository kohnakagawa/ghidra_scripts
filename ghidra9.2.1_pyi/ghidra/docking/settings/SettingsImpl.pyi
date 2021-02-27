from typing import List
import ghidra.docking.settings
import java.io
import java.lang


class SettingsImpl(object, ghidra.docking.settings.Settings, java.io.Serializable):
    """
    Basic implementation of the Settings object
    """

    NO_SETTINGS: ghidra.docking.settings.Settings = {}



    @overload
    def __init__(self):
        """
        Construct a new SettingsImpl
        """
        ...

    @overload
    def __init__(self, settings: ghidra.docking.settings.Settings):
        """
        Construct a new SettingsImpl object with the same set of name-value pairs
         as the given settings object
        @param settings the settings object to copy
        """
        ...

    @overload
    def __init__(self, listener: javax.swing.event.ChangeListener, changeSourceObj: object):
        """
        Construct a new SettingsImpl with the given listener
        @param listener object to be notified as settings values change
        @param changeSourceObj source object to be associated with change events
        """
        ...



    def clearAllSettings(self) -> None:
        """
        @see ghidra.docking.settings.Settings#clearAllSettings()
        """
        ...

    def clearSetting(self, name: unicode) -> None:
        """
        @see ghidra.docking.settings.Settings#clearSetting(java.lang.String)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getByteArray(self, name: unicode) -> List[int]:
        """
        @see ghidra.docking.settings.Settings#getByteArray(java.lang.String)
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultSettings(self) -> ghidra.docking.settings.Settings:
        """
        @see ghidra.docking.settings.Settings#getDefaultSettings()
        """
        ...

    def getLong(self, name: unicode) -> long:
        """
        @see ghidra.docking.settings.Settings#getLong(java.lang.String)
        """
        ...

    def getNames(self) -> List[unicode]:
        """
        @see ghidra.docking.settings.Settings#getNames()
        """
        ...

    def getString(self, name: unicode) -> unicode:
        """
        @see ghidra.docking.settings.Settings#getString(java.lang.String)
        """
        ...

    def getValue(self, name: unicode) -> object:
        """
        @see ghidra.docking.settings.Settings#getValue(java.lang.String)
        """
        ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool:
        """
        @see ghidra.docking.settings.Settings#isEmpty()
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setByteArray(self, name: unicode, value: List[int]) -> None:
        """
        @see ghidra.docking.settings.Settings#setByteArray(java.lang.String, byte[])
        """
        ...

    def setDefaultSettings(self, settings: ghidra.docking.settings.Settings) -> None: ...

    def setLong(self, name: unicode, value: long) -> None:
        """
        @see ghidra.docking.settings.Settings#setLong(java.lang.String, long)
        """
        ...

    def setString(self, name: unicode, value: unicode) -> None:
        """
        @see ghidra.docking.settings.Settings#setString(java.lang.String, java.lang.String)
        """
        ...

    def setValue(self, name: unicode, value: object) -> None:
        """
        @see ghidra.docking.settings.Settings#setValue(java.lang.String, java.lang.Object)
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

    @defaultSettings.setter
    def defaultSettings(self, value: ghidra.docking.settings.Settings) -> None: ...

    @property
    def empty(self) -> bool: ...

    @property
    def names(self) -> List[unicode]: ...
