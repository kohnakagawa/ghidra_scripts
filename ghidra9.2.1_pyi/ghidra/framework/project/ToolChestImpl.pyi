from typing import List
import ghidra.framework.model
import java.lang


class ToolChestImpl(object, ghidra.framework.model.ToolChest):
    """
    Implementation for the Project ToolChest.
    """









    def addToolChestChangeListener(self, l: ghidra.framework.model.ToolChestChangeListener) -> None: ...

    def addToolTemplate(self, template: ghidra.framework.model.ToolTemplate) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getToolCount(self) -> int:
        """
        @see ghidra.framework.model.ToolChest#getToolCount()
        """
        ...

    def getToolTemplate(self, toolName: unicode) -> ghidra.framework.model.ToolTemplate:
        """
        Get the tool template for the given tool name.
        @return null if there is no tool template for the given
         toolName.
        """
        ...

    def getToolTemplates(self) -> List[ghidra.framework.model.ToolTemplate]:
        """
        Get the ToolConfigs from the tool chest.
        @return zero-length array if there are no ToolConfigs in the
         tool chest.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, name: unicode) -> bool:
        """
        Remove tool template from the tool chest.
        @return true if the template was removed from the tool chest.
        """
        ...

    def removeToolChestChangeListener(self, l: ghidra.framework.model.ToolChestChangeListener) -> None: ...

    def replaceToolTemplate(self, template: ghidra.framework.model.ToolTemplate) -> bool: ...

    def toString(self) -> unicode:
        """
        Returns a string representation of the object. In general, the
         <code>toString</code> method returns a string that
         "textually represents" this object. The result should
         be a concise but informative representation that is easy for a
         person to read.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
