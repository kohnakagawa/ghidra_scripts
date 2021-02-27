from typing import List
import ghidra.docking.settings
import java.lang


class EnumSettingsDefinition(ghidra.docking.settings.SettingsDefinition, object):
    """
    Interface for a SettingsDefinition with enumerated values.
    """









    def clear(self, __a0: ghidra.docking.settings.Settings) -> None: ...

    @staticmethod
    def concat(__a0: List[ghidra.docking.settings.SettingsDefinition], __a1: List[ghidra.docking.settings.SettingsDefinition]) -> List[ghidra.docking.settings.SettingsDefinition]: ...

    def copySetting(self, __a0: ghidra.docking.settings.Settings, __a1: ghidra.docking.settings.Settings) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getChoice(self, settings: ghidra.docking.settings.Settings) -> int:
        """
        Returns the current value for this settings
        @param settings The settings to search
        @return the value for the settingsDefintions
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def getDisplayChoice(self, value: int, settings: ghidra.docking.settings.Settings) -> unicode:
        """
        Returns the String for the given enum value
        @param value the value to get a display string for
        @param settings the instance settings which may affect the results
        @return the display string for the given settings.
        """
        ...

    def getDisplayChoices(self, settings: ghidra.docking.settings.Settings) -> List[unicode]:
        """
        Gets the list of choices as strings based on the current settings
        @param settings the instance settings
        @return an array of strings which represent valid choices based on the current
         settings.
        """
        ...

    def getName(self) -> unicode: ...

    def hasValue(self, __a0: ghidra.docking.settings.Settings) -> bool: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setChoice(self, settings: ghidra.docking.settings.Settings, value: int) -> None:
        """
        Sets the given value into the settings object using this definition as a key
        @param settings the settings to store the value.
        @param value the settings value to be stored.
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
