from typing import List
import ghidra.docking.settings
import ghidra.program.model.data
import java.lang


class RenderUnicodeSettingsDefinition(ghidra.docking.settings.JavaEnumSettingsDefinition):
    """
    Settings definition for controlling the display of UNICODE characters.
    """

    RENDER: ghidra.program.model.data.RenderUnicodeSettingsDefinition = ghidra.program.model.data.RenderUnicodeSettingsDefinition@441f6b3d




    class RENDER_ENUM(java.lang.Enum):
        ALL: ghidra.program.model.data.RenderUnicodeSettingsDefinition.RENDER_ENUM = all
        BYTE_SEQ: ghidra.program.model.data.RenderUnicodeSettingsDefinition.RENDER_ENUM = byte sequence
        ESC_SEQ: ghidra.program.model.data.RenderUnicodeSettingsDefinition.RENDER_ENUM = escape sequence







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.program.model.data.RenderUnicodeSettingsDefinition.RENDER_ENUM: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.program.model.data.RenderUnicodeSettingsDefinition.RENDER_ENUM]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...







    def clear(self, settings: ghidra.docking.settings.Settings) -> None: ...

    @staticmethod
    def concat(__a0: List[ghidra.docking.settings.SettingsDefinition], __a1: List[ghidra.docking.settings.SettingsDefinition]) -> List[ghidra.docking.settings.SettingsDefinition]: ...

    def copySetting(self, srcSettings: ghidra.docking.settings.Settings, destSettings: ghidra.docking.settings.Settings) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getChoice(self, settings: ghidra.docking.settings.Settings) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultEnum(self) -> object:
        """
        Returns the Enum instance that is the default Enum for this {@link SettingsDefinition}.
        @return Enum
        """
        ...

    def getDescription(self) -> unicode: ...

    def getDisplayChoice(self, value: int, settings: ghidra.docking.settings.Settings) -> unicode: ...

    def getDisplayChoices(self, settings: ghidra.docking.settings.Settings) -> List[unicode]: ...

    def getEnumByOrdinal(self, ordinal: int) -> object:
        """
        Returns the Enum instance that corresponds to the specified ordinal value.
        @param ordinal integer that corresponds to an Enum.
        @return Enum
        """
        ...

    @overload
    def getEnumValue(self, settings: ghidra.docking.settings.Settings) -> object:
        """
        Returns an enum instance that corresponds to the setting stored, or the
         {@link #getDefaultEnum() default enum} if the setting has not been assigned yet.
        @param settings {@link Settings} object that stores the settings values.
        @return Enum&lt;T&gt; value, or {@link #getDefaultEnum()} if not present.
        """
        ...

    @overload
    def getEnumValue(self, __a0: ghidra.docking.settings.Settings, __a1: java.lang.Enum) -> java.lang.Enum: ...

    def getName(self) -> unicode: ...

    def getOrdinalByString(self, stringValue: unicode) -> int:
        """
        returns the Enum's ordinal using the Enum's string representation.
        @param stringValue Enum's string rep
        @return integer index of the Enum
        """
        ...

    def getSettingName(self) -> unicode:
        """
        The name of this setting as it is stored in a {@link Settings} object.
        @return String name.
        """
        ...

    def hasValue(self, setting: ghidra.docking.settings.Settings) -> bool: ...

    def hashCode(self) -> int: ...

    def isRenderAlphanumericOnly(self, settings: ghidra.docking.settings.Settings) -> bool:
        """
        Gets the current rendering setting from the given settings objects or returns
         the default if not in either settings object
        @param settings the instance settings
        @return the current value for this settings definition
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setChoice(self, settings: ghidra.docking.settings.Settings, value: int) -> None: ...

    def setEnumValue(self, __a0: ghidra.docking.settings.Settings, __a1: java.lang.Enum) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
