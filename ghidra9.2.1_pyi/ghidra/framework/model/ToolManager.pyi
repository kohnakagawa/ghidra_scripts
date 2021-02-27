from typing import List
import ghidra.framework.model
import ghidra.framework.plugintool
import java.lang


class ToolManager(object):
    """
    Interface to define methods to manage running tools and tools in
     the Tool Chest. The ToolManager also keeps track of the workspaces, and
     what tools are running in workspace, as well as the connections among tools
     across all workspaces.
    """

    DEFAULT_WORKSPACE_NAME: unicode = u'Workspace'
    WORKSPACE_NAME_PROPERTY: unicode = u'WorkspaceName'







    def addWorkspaceChangeListener(self, listener: ghidra.framework.model.WorkspaceChangeListener) -> None:
        """
        Add the listener that will be notified when a tool is added
         or removed.
        @param listener workspace listener to add
        """
        ...

    def createWorkspace(self, name: unicode) -> ghidra.framework.model.Workspace:
        """
        Create a workspace with the given name.
        @param name name of workspace
        @return the workspace
        @throws DuplicateNameException if a workspace with this name already exists
        """
        ...

    def disconnectTool(self, tool: ghidra.framework.plugintool.PluginTool) -> None:
        """
        Removes all connections involving tool
        @param tool tool for which to remove all connections
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getActiveWorkspace(self) -> ghidra.framework.model.Workspace:
        """
        Get the active workspace
        @return the active workspace
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getConnection(self, producer: ghidra.framework.plugintool.PluginTool, consumer: ghidra.framework.plugintool.PluginTool) -> ghidra.framework.model.ToolConnection:
        """
        Get the connection object for the producer and consumer tools
        @param producer tool that is producing the tool event
        @param consumer tool that is consuming the tool event
        @return the connection
        """
        ...

    def getConsumerTools(self) -> List[ghidra.framework.plugintool.PluginTool]:
        """
        Get a list of tools that consume at least one tool event.
        @return zero-length array if no tool consumes any events
        """
        ...

    def getProducerTools(self) -> List[ghidra.framework.plugintool.PluginTool]:
        """
        Get a list of tools that produce at least one tool event.
        @return zero-length array if no tool produces any events
        """
        ...

    def getRunningTools(self) -> List[ghidra.framework.plugintool.PluginTool]:
        """
        Get a list running tools across all workspaces.
        @return zero-length array if there are no running tools.
        """
        ...

    def getWorkspaces(self) -> List[ghidra.framework.model.Workspace]:
        """
        Get list of known workspaces.
        @return an array of known workspaces
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeWorkspace(self, ws: ghidra.framework.model.Workspace) -> None:
        """
        Remove the workspace.
        @param ws workspace to remove
        """
        ...

    def removeWorkspaceChangeListener(self, l: ghidra.framework.model.WorkspaceChangeListener) -> None:
        """
        Remove the workspace listener.
        @param l workspace listener to remove
        """
        ...

    def toString(self) -> unicode: ...

    def toolChanged(self, tool: ghidra.framework.plugintool.PluginTool) -> None:
        """
        A configuration change was made to the tool; a plugin was added
         or removed.
        @param tool tool that changed
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def activeWorkspace(self) -> ghidra.framework.model.Workspace: ...

    @property
    def consumerTools(self) -> List[ghidra.framework.plugintool.PluginTool]: ...

    @property
    def producerTools(self) -> List[ghidra.framework.plugintool.PluginTool]: ...

    @property
    def runningTools(self) -> List[ghidra.framework.plugintool.PluginTool]: ...

    @property
    def workspaces(self) -> List[ghidra.framework.model.Workspace]: ...
