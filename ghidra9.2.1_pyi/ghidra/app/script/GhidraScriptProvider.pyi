import generic.jar
import ghidra.app.script
import ghidra.util.classfinder
import java.io
import java.lang


class GhidraScriptProvider(object, ghidra.util.classfinder.ExtensionPoint, java.lang.Comparable):
    """
    NOTE:  ALL GhidraScriptProvider CLASSES MUST END IN "ScriptProvider".  If not,
     the ClassSearcher will not find them.
    """





    def __init__(self): ...



    @overload
    def compareTo(self, that: ghidra.app.script.GhidraScriptProvider) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def createNewScript(self, newScript: generic.jar.ResourceFile, category: unicode) -> None:
        """
        Creates a new script using the specified file.
        @param newScript the new script file
        @param category the script category
        @throws IOException if an error occurs writing the file
        """
        ...

    def deleteScript(self, scriptSource: generic.jar.ResourceFile) -> bool:
        """
        Deletes the script file and unloads the script from the script manager.
        @param scriptSource the script source file
        @return true if the script was completely deleted and cleaned up
        """
        ...

    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCommentCharacter(self) -> unicode:
        """
        Returns the comment character.
         For example, "//" or "#".
        @return the comment character
        """
        ...

    def getDescription(self) -> unicode:
        """
        Returns a description for this type of script.
        @return a description for this type of script
        """
        ...

    def getExtension(self) -> unicode:
        """
        Returns the file extension for this type of script.
         For example, ".java" or ".py".
        @return the file extension for this type of script
        """
        ...

    def getScriptInstance(self, sourceFile: generic.jar.ResourceFile, writer: java.io.PrintWriter) -> ghidra.app.script.GhidraScript:
        """
        Returns a GhidraScript instance for the specified source file.
        @param sourceFile the source file
        @param writer the print writer to write warning/error messages
        @return a GhidraScript instance for the specified source file
        """
        ...

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

    @property
    def commentCharacter(self) -> unicode: ...

    @property
    def description(self) -> unicode: ...

    @property
    def extension(self) -> unicode: ...
