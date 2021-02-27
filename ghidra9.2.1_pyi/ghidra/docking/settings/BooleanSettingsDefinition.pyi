from typing import List
import ghidra.docking.settings
import java.lang


class BooleanSettingsDefinition(ghidra.docking.settings.SettingsDefinition, object):
    """
    The inteface for SettingsDefinitions that have boolean values.  SettingsDefinitions
     objects are used as keys into Settings objects that contain the values using a name-value
     type storage mechanism.
    """









    def clear(self, __a0: ghidra.docking.settings.Settings) -> None: ...

    @staticmethod
    def concat(__a0: List[ghidra.docking.settings.SettingsDefinition], __a1: List[ghidra.docking.settings.SettingsDefinition]) -> List[ghidra.docking.settings.SettingsDefinition]: ...

    def copySetting(self, __a0: ghidra.docking.settings.Settings, __a1: ghidra.docking.settings.Settings) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def getName(self) -> unicode: ...

    def getValue(self, settings: ghidra.docking.settings.Settings) -> bool:
        """
        gets the value for this SettingsDefinition given a Settings object.
        @param settings the set of Settings values for a particular location or null for default value.
        @return the values for this settings object given the context.
        """
        ...

    def hasValue(self, __a0: ghidra.docking.settings.Settings) -> bool: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setValue(self, settings: ghidra.docking.settings.Settings, value: bool) -> None:
        """
        Sets the given value into the given settings object using this settingsDefinition as the key.
        @param settings the settings object to store the value in.
        @param value the value to store in the settings object using this settingsDefinition as the key.
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
    def description(self) -> unicode: ...

    @property
    def name(self) -> unicode: ...
