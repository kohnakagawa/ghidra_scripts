from typing import List
import ghidra.docking.settings
import java.lang


class SettingsDBManager(object, ghidra.docking.settings.Settings):
    """
    Database implementation for settings.
    """









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
