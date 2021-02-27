from typing import List
import ghidra.docking.settings
import ghidra.util
import java.lang


class IntegerSignednessFormattingModeSettingsDefinition(object, ghidra.docking.settings.EnumSettingsDefinition):
    """
    The settings definition for the numeric display format for handling signed values.

    """

    DEF: ghidra.docking.settings.IntegerSignednessFormattingModeSettingsDefinition = ghidra.docking.settings.IntegerSignednessFormattingModeSettingsDefinition@7fe952da
    DEF_SIGNED: ghidra.docking.settings.IntegerSignednessFormattingModeSettingsDefinition = ghidra.docking.settings.IntegerSignednessFormattingModeSettingsDefinition@7cb604bb
    DEF_UNSIGNED: ghidra.docking.settings.IntegerSignednessFormattingModeSettingsDefinition = ghidra.docking.settings.IntegerSignednessFormattingModeSettingsDefinition@4c12df6b







    def clear(self, settings: ghidra.docking.settings.Settings) -> None: ...

    @staticmethod
    def concat(__a0: List[ghidra.docking.settings.SettingsDefinition], __a1: List[ghidra.docking.settings.SettingsDefinition]) -> List[ghidra.docking.settings.SettingsDefinition]: ...

    def copySetting(self, settings: ghidra.docking.settings.Settings, destSettings: ghidra.docking.settings.Settings) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getChoice(self, settings: ghidra.docking.settings.Settings) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    @overload
    def getDisplayChoice(self, settings: ghidra.docking.settings.Settings) -> unicode: ...

    @overload
    def getDisplayChoice(self, value: int, s1: ghidra.docking.settings.Settings) -> unicode: ...

    def getDisplayChoices(self, settings: ghidra.docking.settings.Settings) -> List[unicode]: ...

    def getFormatMode(self, settings: ghidra.docking.settings.Settings) -> ghidra.util.SignednessFormatMode:
        """
        Returns the format based on the specified settings
        @param settings the instance settings or null for default value.
        @return the format mode
        """
        ...

    def getName(self) -> unicode: ...

    def hasValue(self, setting: ghidra.docking.settings.Settings) -> bool: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setChoice(self, settings: ghidra.docking.settings.Settings, value: int) -> None: ...

    def setDisplayChoice(self, settings: ghidra.docking.settings.Settings, choice: unicode) -> None:
        """
        Sets the settings object to the enum value indicating the specified choice as a string.
        @param settings the settings to store the value.
        @param choice enum string representing a choice in the enum.
        """
        ...

    def setFormatMode(self, settings: ghidra.docking.settings.Settings, mode: ghidra.util.SignednessFormatMode) -> None:
        """
        Set, or clear if <code>mode</code> is null, the new mode in the provided settings
        @param settings settings object
        @param mode new value to assign, or null to clear
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
