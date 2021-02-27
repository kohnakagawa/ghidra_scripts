import ghidra.framework.model
import java.io
import java.lang
import java.util


class ToolUtils(object):
    TOOL_EXTENSION: unicode = u'.tool'







    @staticmethod
    def deleteTool(template: ghidra.framework.model.ToolTemplate) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getAllApplicationTools() -> java.util.Set:
        """
        Returns all tools found in the classpath that live under a root
         'defaultTools' directory or a root 'extraTools' directory
        @return the tools
        """
        ...

    @staticmethod
    def getApplicationToolDirPath() -> unicode:
        """
        Returns the user's personal tool chest directory path
        @return the path
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getDefaultApplicationTools() -> java.util.Set:
        """
        Returns all tools found in the classpath that live under a root
         'defaultTools' directory
        @return the default tools
        """
        ...

    @staticmethod
    def getExtraApplicationTools() -> java.util.Set:
        """
        Returns all tools found in the classpath that live under a root
         'extraTools' directory
        @return the extra tools
        """
        ...

    @staticmethod
    def getToolFile(name: unicode) -> java.io.File: ...

    @staticmethod
    def getUniqueToolName(template: ghidra.framework.model.ToolTemplate) -> unicode: ...

    @staticmethod
    def getUserToolsDirectory() -> java.io.File: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def loadUserTools() -> java.util.Map: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    @staticmethod
    def readToolTemplate(resourceFileName: unicode) -> ghidra.framework.model.ToolTemplate: ...

    @overload
    @staticmethod
    def readToolTemplate(toolFile: java.io.File) -> ghidra.framework.model.ToolTemplate: ...

    @staticmethod
    def removeInvalidPlugins(template: ghidra.framework.model.ToolTemplate) -> None: ...

    @staticmethod
    def renameToolTemplate(toolTemplate: ghidra.framework.model.ToolTemplate, newName: unicode) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @staticmethod
    def writeToolTemplate(template: ghidra.framework.model.ToolTemplate) -> bool: ...
