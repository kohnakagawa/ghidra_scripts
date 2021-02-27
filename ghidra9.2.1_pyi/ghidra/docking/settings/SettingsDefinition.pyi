from typing import List
import ghidra.docking.settings
import java.lang


class SettingsDefinition(object):
    """
    Generic interface for defining display options on data and dataTypes.  Uses
     Settings objects to store values which are interpreted by SettingsDefinition objects.
    """









    def clear(self, settings: ghidra.docking.settings.Settings) -> None:
        """
        Removes any values in the given settings object assocated with this settings definition
        @param settings the settings object to be cleared.
        """
        ...

    @staticmethod
    def concat(settings: List[ghidra.docking.settings.SettingsDefinition], additional: List[ghidra.docking.settings.SettingsDefinition]) -> List[ghidra.docking.settings.SettingsDefinition]:
        """
        Create a new list of {@link SettingsDefinition}s by concat'ing a base list with
         a var-arg'ish additional list of setting defs.
        @param settings List of settings defs.
        @param additional More settings defs to add
        @return new array with all the settings defs joined together.
        """
        ...

    def copySetting(self, srcSettings: ghidra.docking.settings.Settings, destSettings: ghidra.docking.settings.Settings) -> None:
        """
        Copies any setting value associated with this settings definition from the
         srcSettings settings to the destSettings.
        @param srcSettings the settings to be copied
        @param destSettings the settings to be updated.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode:
        """
        Returns a description of this settings definition
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of this SettingsDefinition
        """
        ...

    def hasValue(self, setting: ghidra.docking.settings.Settings) -> bool: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

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
