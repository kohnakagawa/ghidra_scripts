from typing import List
import ghidra.docking.settings
import ghidra.program.model.lang
import ghidra.program.model.mem
import java.lang


class EndianSettingsDefinition(object, ghidra.docking.settings.EnumSettingsDefinition):
    """
    SettingsDefinition for endianess
    """

    BIG: int = 2
    DEF: ghidra.program.model.data.EndianSettingsDefinition = ghidra.program.model.data.EndianSettingsDefinition@3a0f87f2
    DEFAULT: int = 0
    ENDIAN: ghidra.program.model.data.EndianSettingsDefinition = ghidra.program.model.data.EndianSettingsDefinition@3a0f87f2
    LITTLE: int = 1







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

    def getEndianess(self, settings: ghidra.docking.settings.Settings, defaultValue: ghidra.program.model.lang.Endian) -> ghidra.program.model.lang.Endian: ...

    def getName(self) -> unicode: ...

    def hasValue(self, setting: ghidra.docking.settings.Settings) -> bool: ...

    def hashCode(self) -> int: ...

    def isBigEndian(self, settings: ghidra.docking.settings.Settings, buf: ghidra.program.model.mem.MemBuffer) -> bool:
        """
        Returns the endianess settings.  First looks in settings, then defaultSettings
         and finally returns a default value if the first two have no value for this definition.
        @param settings the instance settings to search for the value
        @param buf the data context
        @return a boolean value for the endianess setting
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setBigEndian(self, settings: ghidra.docking.settings.Settings, isBigEndian: bool) -> None: ...

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
