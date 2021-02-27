from typing import List
import ghidra.docking.settings
import java.lang


class PaddingSettingsDefinition(object, ghidra.docking.settings.EnumSettingsDefinition):
    """
    The Settings definition for setting the padded/unpadded setting
    """

    DEF: ghidra.program.model.data.PaddingSettingsDefinition = ghidra.program.model.data.PaddingSettingsDefinition@490588e6







    def clear(self, settings: ghidra.docking.settings.Settings) -> None: ...

    @staticmethod
    def concat(__a0: List[ghidra.docking.settings.SettingsDefinition], __a1: List[ghidra.docking.settings.SettingsDefinition]) -> List[ghidra.docking.settings.SettingsDefinition]: ...

    def copySetting(self, settings: ghidra.docking.settings.Settings, destSettings: ghidra.docking.settings.Settings) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getChoice(self, settings: ghidra.docking.settings.Settings) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def getDisplayChoice(self, value: int, s1: ghidra.docking.settings.Settings) -> unicode: ...

    def getDisplayChoices(self, settings: ghidra.docking.settings.Settings) -> List[unicode]: ...

    def getName(self) -> unicode: ...

    def hasValue(self, setting: ghidra.docking.settings.Settings) -> bool: ...

    def hashCode(self) -> int: ...

    def isPadded(self, settings: ghidra.docking.settings.Settings) -> bool:
        """
        Checks if the current settings are padded or unpadded
        @param settings the instance settings to check
        @return true if the value is "padded".
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setChoice(self, settings: ghidra.docking.settings.Settings, value: int) -> None: ...

    def setPadded(self, settings: ghidra.docking.settings.Settings, isPadded: bool) -> None:
        """
        Set true if value should display padded out with zero's
        @param settings settings to set padded value
        @param isPadded true for padding
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
