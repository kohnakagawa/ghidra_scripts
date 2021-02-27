from typing import List
import ghidra.framework.model
import ghidra.framework.plugintool
import java.lang


class Workspace(object):
    """
    Defines methods for accessing a workspace; a workspace is
     simply a group of running tools and their templates.
    """









    def createTool(self) -> ghidra.framework.plugintool.PluginTool:
        """
        Launch an empty tool.
        @return name of empty tool that is launched.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode:
        """
        Get the workspace name
        @return the name
        """
        ...

    def getTools(self) -> List[ghidra.framework.plugintool.PluginTool]:
        """
        Get the running tools in the workspace.
        @return list of running tools or zero-length array if there are no tools in the workspace
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def runTool(self, template: ghidra.framework.model.ToolTemplate) -> ghidra.framework.plugintool.PluginTool:
        """
        Run the tool specified by the tool template object.
        @param template the template
        @return launched tool that is now running.
        """
        ...

    def setActive(self) -> None:
        """
        Set this workspace to be the active workspace, i.e.,
         all tools become visible.
         The currently active workspace becomes inactive, and
         this workspace becomes active.
        """
        ...

    def setName(self, newName: unicode) -> None:
        """
        Rename this workspace.
        @param newName new workspace name
        @throws DuplicateNameException if newName is already the
         name of a workspace.
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
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def tools(self) -> List[ghidra.framework.plugintool.PluginTool]: ...
