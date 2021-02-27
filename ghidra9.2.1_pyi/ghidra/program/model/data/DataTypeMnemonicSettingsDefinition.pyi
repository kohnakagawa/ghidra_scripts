from typing import List
import ghidra.docking.settings
import java.lang


class DataTypeMnemonicSettingsDefinition(object, ghidra.docking.settings.EnumSettingsDefinition):
    """
    The settings definition for the numeric display format
    """

    ASSEMBLY: int = 1
    CSPEC: int = 2
    DEF: ghidra.program.model.data.DataTypeMnemonicSettingsDefinition = ghidra.program.model.data.DataTypeMnemonicSettingsDefinition@1bfce38e
    DEFAULT: int = 0







    def clear(self, settings: ghidra.docking.settings.Settings) -> None: ...

    @staticmethod
    def concat(__a0: List[ghidra.docking.settings.SettingsDefinition], __a1: List[ghidra.docking.settings.SettingsDefinition]) -> List[ghidra.docking.settings.SettingsDefinition]: ...

    def copySetting(self, settings: ghidra.docking.settings.Settings, destSettings: ghidra.docking.settings.Settings) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getChoice(self, settings: ghidra.docking.settings.Settings) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def getDisplayChoice(self, value: int, settings: ghidra.docking.settings.Settings) -> unicode: ...

    def getDisplayChoices(self, settings: ghidra.docking.settings.Settings) -> List[unicode]: ...

    def getMnemonicStyle(self, settings: ghidra.docking.settings.Settings) -> int:
        """
        Returns the format based on the specified settings
        @param settings the instance settings.
        @return the format value (HEX, DECIMAL, BINARY, OCTAL, CHAR)
        """
        ...

    def getName(self) -> unicode: ...

    def hasValue(self, setting: ghidra.docking.settings.Settings) -> bool: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setChoice(self, settings: ghidra.docking.settings.Settings, value: int) -> None: ...

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
