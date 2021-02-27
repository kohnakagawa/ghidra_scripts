import ghidra.framework.model
import ghidra.framework.plugintool
import java.beans
import java.lang


class WorkspaceChangeListener(java.beans.PropertyChangeListener, object):
    """
    Listener that is notified when a tool is added or removed from a
     workspace, or when workspace properties change.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def propertyChange(self, __a0: java.beans.PropertyChangeEvent) -> None: ...

    def toString(self) -> unicode: ...

    def toolAdded(self, ws: ghidra.framework.model.Workspace, tool: ghidra.framework.plugintool.PluginTool) -> None:
        """
        Notification that a tool was added to the given workspace.
        @param ws workspace the affected workspace
        @param tool tool that was added
        """
        ...

    def toolRemoved(self, ws: ghidra.framework.model.Workspace, tool: ghidra.framework.plugintool.PluginTool) -> None:
        """
        Notification that a tool was removed from the given workspace.
        @param ws workspace the affected workspace
        @param tool tool that was removed from the workspace
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def workspaceAdded(self, ws: ghidra.framework.model.Workspace) -> None:
        """
        Notification that the given workspace was added by the ToolManager.
        @param ws workspace the affected workspace
        """
        ...

    def workspaceRemoved(self, ws: ghidra.framework.model.Workspace) -> None:
        """
        Notification that the given workspace was removed by the ToolManager.
        @param ws workspace the affected workspace
        """
        ...

    def workspaceSetActive(self, ws: ghidra.framework.model.Workspace) -> None:
        """
        Notification that the given workspace is the current one.
        @param ws workspace the affected workspace
        """
        ...
