from typing import List
import ghidra.framework.model
import java.lang


class ToolChest(object):
    """
    Interface to define methods to manage tools in a central location.
    """









    def addToolChestChangeListener(self, l: ghidra.framework.model.ToolChestChangeListener) -> None:
        """
        Add a listener to be notified when the tool chest is changed.
        @param l listener to add
        """
        ...

    def addToolTemplate(self, template: ghidra.framework.model.ToolTemplate) -> bool:
        """
        Add tool template to the tool chest.
         <br>
         Note: If the given tool template name already exists in the project, then the name will
         be altered by appending an underscore and a one-up value.  The <code>template</code>
         parameter's name is also updated with then new name.
         <p>
         To simply replace a tool with without changing its name, call
         {@link #replaceToolTemplate(ToolTemplate)}
        @param template tool template to add
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getToolCount(self) -> int:
        """
        Get the number of tools in this tool chest.
        @return tool count.
        """
        ...

    def getToolTemplate(self, toolName: unicode) -> ghidra.framework.model.ToolTemplate:
        """
        Get the tool template for the given tool name.
        @param toolName name of tool
        @return null if there is no tool template for the given
         toolName.
        """
        ...

    def getToolTemplates(self) -> List[ghidra.framework.model.ToolTemplate]:
        """
        Get the tool templates from the tool chest.
        @return list of tool template
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, toolName: unicode) -> bool:
        """
        Remove entry (toolTemplate or toolSet) from the tool chest.
        @param toolName name of toolConfig or toolSet to remove
        @return true if the toolConfig or toolset was
         successfully removed from the tool chest.
        """
        ...

    def removeToolChestChangeListener(self, l: ghidra.framework.model.ToolChestChangeListener) -> None:
        """
        Remove a listener that is listening to when the tool chest is changed.
        @param l to remove
        """
        ...

    def replaceToolTemplate(self, template: ghidra.framework.model.ToolTemplate) -> bool:
        """
        Performs the same action as calling {@link #remove(String)} and then
         {@link #addToolTemplate(ToolTemplate)}.  However, calling this method prevents state from
         being lost in the transition, such as position in the tool chest and default tool status.
        @param template The template to add to the tool chest, replacing any tools with the same name.
        @return True if the template was added.
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
    def toolCount(self) -> int: ...

    @property
    def toolTemplates(self) -> List[ghidra.framework.model.ToolTemplate]: ...
