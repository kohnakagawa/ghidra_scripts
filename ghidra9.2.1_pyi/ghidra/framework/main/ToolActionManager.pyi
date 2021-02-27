import ghidra.framework.model
import java.lang


class ToolActionManager(object, ghidra.framework.model.ToolChestChangeListener):
    """
    Helper class to manage actions on the Tool menu.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    def toolRemoved(self, toolName: unicode) -> None:
        """
        ToolConfig was removed from the project toolchest
        """
        ...

    def toolSetAdded(self, toolset: ghidra.framework.model.ToolSet) -> None:
        """
        ToolSet was added to the project toolchest
        """
        ...

    def toolTemplateAdded(self, tc: ghidra.framework.model.ToolTemplate) -> None:
        """
        ToolConfig was added to the project toolchest
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
