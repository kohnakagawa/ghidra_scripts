from typing import List
import docking
import ghidra.app.services
import ghidra.formats.gfilesystem
import ghidra.framework.plugintool
import ghidra.plugins.fsbrowser
import java.lang


class FSBUtils(object):
    """
    FileSystemBrowserPlugin utility methods that other things might find useful.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def fsrlHasContainer(fsFSRL: ghidra.formats.gfilesystem.FSRLRoot) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getFSRLFromContext(context: docking.ActionContext, dirsOk: bool) -> ghidra.formats.gfilesystem.FSRL: ...

    @staticmethod
    def getFileFSRLFromContext(context: docking.ActionContext) -> ghidra.formats.gfilesystem.FSRL: ...

    @staticmethod
    def getNodesRoot(node: ghidra.plugins.fsbrowser.FSBNode) -> ghidra.plugins.fsbrowser.FSBRootNode: ...

    @staticmethod
    def getProgramManager(tool: ghidra.framework.plugintool.PluginTool, allowUserPrompt: bool) -> ghidra.app.services.ProgramManager:
        """
        Returns the {@link ProgramManager} associated with this fs browser plugin.
         <p>
         When this FS Browser plugin is part of the front-end tool, this will search
         for an open CodeBrowser tool that can be used to handle programs.
         <p>
         When this FS Browser plugin is part of a CodeBrowser tool, this will just return
         the local ProgramManager / CodeBrowser.
        @param tool The plugin tool.
        @param allowUserPrompt boolean flag to allow this method to query the user to select
         a CodeBrowser.
        @return null if front-end and no open CodeBrowser, otherwise returns the local
         CodeBrowser ProgramManager service.
        """
        ...

    @staticmethod
    def getRunningProgramManagerTools(tool: ghidra.framework.plugintool.PluginTool) -> List[ghidra.framework.plugintool.PluginTool]: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
