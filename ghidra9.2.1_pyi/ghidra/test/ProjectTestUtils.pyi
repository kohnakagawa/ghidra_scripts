import ghidra.framework.model
import ghidra.framework.plugintool
import ghidra.program.model.lang
import java.lang


class ProjectTestUtils(object):
    """
    Ghidra framework and program test utilities
    """





    def __init__(self): ...



    @staticmethod
    def createProgramFile(proj: ghidra.framework.model.Project, progName: unicode, language: ghidra.program.model.lang.Language, compilerSpec: ghidra.program.model.lang.CompilerSpec, folder: ghidra.framework.model.DomainFolder) -> ghidra.framework.model.DomainFile:
        """
        Create an empty program file within the specified project folder.
        @param proj active project.
        @param progName name of program and domain file to be created.
        @param language a specified language, or 0 if it does not matter.
        @param compilerSpec the compiler spec
        @param folder domain folder within the specified project which the
         user has permission to write.  If null, the root data folder will be used.
        @return new domain file.
        @throws InvalidNameException if the filename is invalid
        @throws CancelledException if the opening is cancelled
        @throws LanguageNotFoundException if the language cannot be found
        @throws IOException if there is an exception creating the program or domain file
        """
        ...

    @staticmethod
    def deleteProject(directory: unicode, name: unicode) -> bool:
        """
        Remove entire project.  Note: this will not remove the parent <code>directory</code> of
         the project.
        @param directory directory of the project.
        @param name The name of the project to delete
        @return True if the project was deleted.
        """
        ...

    @staticmethod
    def deleteTool(project: ghidra.framework.model.Project, toolName: unicode) -> bool:
        """
        Remove the specified tool if it exists.
        @param project the project
        @param toolName the tool name
        @return true if it existed and was removed from the local tool chest.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getProject(directory: unicode, name: unicode) -> ghidra.framework.model.Project:
        """
        Open the project for the given directory and name.
         If the project does not exist, create one.
         Only once instance of a given project may be open at any given
         point in time.  Be sure to close the project if you will be
         re-opening.
        @param directory directory for the project
        @param name name of the project
        @return the project
        @throws IOException if there was a problem creating the project
        @throws LockException if the project is already open
        @throws IllegalArgumentException if the name has illegal characters such that a URL could
         not be created
        """
        ...

    @staticmethod
    def getTool(project: ghidra.framework.model.Project, toolName: unicode) -> ghidra.framework.plugintool.PluginTool:
        """
        Launch a tool.
        @param project the project to which the tool belongs
        @param toolName name of the tool to get from the active workspace.
         If null, launch a new empty tool in the active workspace.
        @return the tool
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def saveTool(project: ghidra.framework.model.Project, tool: ghidra.framework.plugintool.PluginTool) -> ghidra.framework.model.ToolTemplate:
        """
        Save a tool to the project tool chest.
        @param project The project which with the tool is associated.
        @param tool The tool to be saved
        @return The tool template for the given tool.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
