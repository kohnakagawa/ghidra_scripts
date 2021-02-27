from typing import List
import ghidra.docking.settings
import java.lang
import java.util


class CharsetSettingsDefinition(object, ghidra.docking.settings.EnumSettingsDefinition):
    """
    SettingsDefinition for setting the charset of a string instance.

      Charsets control how raw bytes are converted to native java String instances.

      CharsetInfo controls the list of character sets that the user is shown.
    """

    CHARSET: ghidra.program.model.data.CharsetSettingsDefinition = ghidra.program.model.data.CharsetSettingsDefinition@3035956a







    def clear(self, settings: ghidra.docking.settings.Settings) -> None: ...

    @staticmethod
    def concat(__a0: List[ghidra.docking.settings.SettingsDefinition], __a1: List[ghidra.docking.settings.SettingsDefinition]) -> List[ghidra.docking.settings.SettingsDefinition]: ...

    def copySetting(self, settings: ghidra.docking.settings.Settings, destSettings: ghidra.docking.settings.Settings) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getCharset(self, settings: ghidra.docking.settings.Settings, defaultValue: unicode) -> unicode: ...

    def getChoice(self, settings: ghidra.docking.settings.Settings) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def getDisplayChoice(self, ordinalOfValue: int, s1: ghidra.docking.settings.Settings) -> unicode: ...

    def getDisplayChoices(self, settings: ghidra.docking.settings.Settings) -> List[unicode]: ...

    def getName(self) -> unicode: ...

    def hasValue(self, setting: ghidra.docking.settings.Settings) -> bool: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setCharset(self, settings: ghidra.docking.settings.Settings, charset: unicode) -> None: ...

    def setChoice(self, settings: ghidra.docking.settings.Settings, ordinalOfValue: int) -> None: ...

    @staticmethod
    def setStaticEncodingMappingValues(mappingValues: java.util.Map) -> None:
        """
        Sets a static lookup table that maps from old deprecated (language,encoding) index
         values to a charset name.
         <p>
         The old index values were used by old-style MBCS data type.
        @param mappingValues map of language_id to list of charset names.
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
