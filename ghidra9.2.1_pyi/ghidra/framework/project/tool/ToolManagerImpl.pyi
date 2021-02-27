from typing import List
import ghidra.framework.model
import ghidra.framework.plugintool
import java.beans
import java.lang
import org.jdom


class ToolManagerImpl(object, ghidra.framework.model.ToolManager, java.beans.PropertyChangeListener):
    """
    Tool manager that knows about all the running tools for each workspace
     in the project; the tool manager is responsible for launching new tools,
     and managing connections among tools.
    """

    DEFAULT_WORKSPACE_NAME: unicode = u'Workspace'
    WORKSPACE_NAME_PROPERTY: unicode = u'WorkspaceName'



    def __init__(self, project: ghidra.framework.model.Project): ...



    def addWorkspaceChangeListener(self, l: ghidra.framework.model.WorkspaceChangeListener) -> None: ...

    def canAutoSave(self, tool: ghidra.framework.plugintool.PluginTool) -> bool: ...

    def clearWorkspaceChanged(self) -> None:
        """
        Clear the flag so the user does not get prompted to save the
         project; flag gets set to true when a workspace is created, and
         a workspace is created when a new project is created.
        """
        ...

    def close(self) -> None:
        """
        Close all running tools in the project.
        """
        ...

    def createWorkspace(self, name: unicode) -> ghidra.framework.model.Workspace: ...

    def disconnectTool(self, tool: ghidra.framework.plugintool.PluginTool) -> None: ...

    def dispose(self) -> None: ...

    def dumpConnectionList(self) -> None:
        """
        Debug method for printing out the list of connections.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getActiveWorkspace(self) -> ghidra.framework.model.Workspace: ...

    def getClass(self) -> java.lang.Class: ...

    def getConnection(self, producer: ghidra.framework.plugintool.PluginTool, consumer: ghidra.framework.plugintool.PluginTool) -> ghidra.framework.model.ToolConnection: ...

    def getConsumerTools(self) -> List[ghidra.framework.plugintool.PluginTool]: ...

    def getProducerTools(self) -> List[ghidra.framework.plugintool.PluginTool]: ...

    def getRunningTools(self) -> List[ghidra.framework.plugintool.PluginTool]: ...

    def getTool(self, toolName: unicode) -> ghidra.framework.plugintool.PluginTool:
        """
        Called by WorkspaceImpl when it is restoring its state.
        @param toolName the name of the tool
        @return the tool
        """
        ...

    def getToolServices(self) -> ghidra.framework.model.ToolServices:
        """
        Get any tool services available from this tool
        @return ToolServices list of tool services this tool can provide.
        """
        ...

    def getWorkspaces(self) -> List[ghidra.framework.model.Workspace]: ...

    def hasChanged(self) -> bool:
        """
        Return whether any tools have changed, or if any tools were
         added or removed from any of the workspaces.
        @return true if any tools in this workspace have changed
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def propertyChange(self, evt: java.beans.PropertyChangeEvent) -> None: ...

    def removeWorkspace(self, ws: ghidra.framework.model.Workspace) -> None: ...

    def removeWorkspaceChangeListener(self, l: ghidra.framework.model.WorkspaceChangeListener) -> None: ...

    def restoreFromXml(self, root: org.jdom.Element) -> None:
        """
        restores the object from an XML element
        @param root root element of saved XML state
        """
        ...

    def saveSessionTools(self) -> bool:
        """
        Save the tools that are opened and changed, that will be brought back up when the project
         is reopened
        @return true if the session was saved
        """
        ...

    def saveToXml(self) -> org.jdom.Element:
        """
        Saves this object to an XML element
        @return the element containing the tool XML
        """
        ...

    def toString(self) -> unicode: ...

    def toolChanged(self, tool: ghidra.framework.plugintool.PluginTool) -> None: ...

    def toolSaved(self, tool: ghidra.framework.plugintool.PluginTool, toolChanged: bool) -> None: ...

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
    def toolServices(self) -> ghidra.framework.model.ToolServices: ...

    @property
    def workspaces(self) -> List[ghidra.framework.model.Workspace]: ...
