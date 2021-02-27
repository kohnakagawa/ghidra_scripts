from typing import List
import ghidra.framework.model
import ghidra.framework.plugintool
import java.io
import java.lang
import java.util


class ToolServices(object):
    """
    Services that the Tool uses.
    """

    DEFAULT_TOOLNAME: unicode = u'DefaultTool'







    def addDefaultToolChangeListener(self, listener: ghidra.framework.model.DefaultToolChangeListener) -> None:
        """
        Add a listener that will be notified when the default tool specification changes
        @param listener the listener
        """
        ...

    def canAutoSave(self, tool: ghidra.framework.plugintool.PluginTool) -> bool:
        """
        Returns true if this tool should be saved base on the state of other running instances of
         the same tool
        @param tool the tool to check for saving
        @return true if the tool should be saved
        """
        ...

    def closeTool(self, tool: ghidra.framework.plugintool.PluginTool) -> None:
        """
        Notify the framework that the tool is closing.
        @param tool tool that is closing
        """
        ...

    def displaySimilarTool(self, tool: ghidra.framework.plugintool.PluginTool, domainFile: ghidra.framework.model.DomainFile, event: ghidra.framework.plugintool.PluginEvent) -> None:
        """
        Find a running tool like the one specified that has the named domain file.
         If it finds a matching tool, then it is brought to the front.
         Otherwise, it creates one and runs it.
         It then invokes the specified event on the running tool.
        @param tool find/create a tool like this one.
        @param domainFile open this file in the found/created tool.
        @param event invoke this event on the found/created tool
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def exportTool(self, tool: ghidra.framework.model.ToolTemplate) -> java.io.File:
        """
        Save the tool to the given location on the local file system.
        @param tool the tool template to write
        @return the file to which the tool was saved
        @throws FileNotFoundException thrown if the file's directory doesn't exist.
        @throws IOException thrown if there is an error writing the file.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getCompatibleTools(self, domainClass: java.lang.Class) -> java.util.Set:
        """
        Returns a set of tools that can open the given domain file class.
        @param domainClass The domain file class type for which to get tools
        @return the tools
        """
        ...

    def getContentTypeToolAssociations(self) -> java.util.Set:
        """
        Returns the {@link ToolAssociationInfo associations}, which describe content
         types and the tools used to open them, for all content types known to the system.
        @return the associations
        @see #setContentTypeToolAssociations(Set)
        """
        ...

    def getDefaultToolTemplate(self, domainFile: ghidra.framework.model.DomainFile) -> ghidra.framework.model.ToolTemplate:
        """
        Returns the default tool template used to open the tool.  Here <b>default</b> means the
         tool that should be used to open the given file, whether defined by the user or the
         system default.
        @param domainFile The file for which to find the preferred tool.
        @return The preferred tool that should be used to open the given file.
        """
        ...

    def getRunningTools(self) -> List[ghidra.framework.plugintool.PluginTool]:
        """
        Return array of running tools
        @return array of Tools
        """
        ...

    def getToolChest(self) -> ghidra.framework.model.ToolChest:
        """
        Get the tool chest for the project
        @return the tool chest
        """
        ...

    def hashCode(self) -> int: ...

    def launchDefaultTool(self, domainFile: ghidra.framework.model.DomainFile) -> ghidra.framework.plugintool.PluginTool:
        """
        Launch the default tool; if domainFile is not null, this file will
         be opened in the tool.
        @param domainFile the file to open; may be null
        @return the tool
        """
        ...

    def launchTool(self, toolName: unicode, domainFile: ghidra.framework.model.DomainFile) -> ghidra.framework.plugintool.PluginTool:
        """
        Launch the tool with the given name
        @param toolName name of the tool to launch
        @param domainFile the file to open; may be null
        @return the tool
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeDefaultToolChangeListener(self, listener: ghidra.framework.model.DefaultToolChangeListener) -> None:
        """
        Remove the listener
        @param listener the listener
        """
        ...

    def saveTool(self, tool: ghidra.framework.plugintool.PluginTool) -> None:
        """
        Saves the tool's configuration in the standard
         tool location.
        @param tool tool to save.
        """
        ...

    def setContentTypeToolAssociations(self, infos: java.util.Set) -> None:
        """
        Sets the  {@link ToolAssociationInfo associations}, which describe content
         types and the tools used to open them, for the system.
        @param infos The associations to be applied
        @see #getContentTypeToolAssociations()
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
    def contentTypeToolAssociations(self) -> java.util.Set: ...

    @contentTypeToolAssociations.setter
    def contentTypeToolAssociations(self, value: java.util.Set) -> None: ...

    @property
    def runningTools(self) -> List[ghidra.framework.plugintool.PluginTool]: ...

    @property
    def toolChest(self) -> ghidra.framework.model.ToolChest: ...
