import generic.jar
import ghidra.app.script
import java.lang


class GhidraScriptInfoManager(object):
    """
    A utility class for managing script directories and ScriptInfo objects.
    """





    def __init__(self): ...



    def alreadyExists(self, scriptName: unicode) -> bool:
        """
        Looks through all of the current {@link ScriptInfo}s to see if one already exists with
         the given name.
        @param scriptName The name to check
        @return true if the name is not taken by an existing {@link ScriptInfo}.
        """
        ...

    def clearMetadata(self) -> None:
        """
        clear ScriptInfo metadata cached by GhidraScriptUtil
        """
        ...

    def containsMetadata(self, scriptFile: generic.jar.ResourceFile) -> bool:
        """
        Returns true if a ScriptInfo object exists for
         the specified script file.
        @param scriptFile the script file
        @return true if a ScriptInfo object exists
        """
        ...

    def dispose(self) -> None:
        """
        clear stored metadata
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def findScriptInfoByName(self, scriptName: unicode) -> ghidra.app.script.ScriptInfo:
        """
        Uses the given name to find a matching script.  This method only works because of the
         limitation that all script names in Ghidra must be unique.  If the given name has multiple
         script matches, then a warning will be logged.
        @param scriptName The name for which to find a script
        @return The ScriptInfo that has the given name
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getExistingScriptInfo(self, scriptName: unicode) -> ghidra.app.script.ScriptInfo:
        """
        Returns the existing script info for the given name.  The script environment limits
         scripts such that names are unique.  If this method returns a non-null value, then the
         name given name is taken.
        @param scriptName the name of the script for which to get a ScriptInfo
        @return a ScriptInfo matching the given name; null if no script by that name is known to
                 the script manager
        """
        ...

    @overload
    def getExistingScriptInfo(self, script: generic.jar.ResourceFile) -> ghidra.app.script.ScriptInfo:
        """
        Get {@link ScriptInfo} for {@code script} under the assumption that it's already managed.
        @param script the script
        @return info or null if the assumption was wrong. If null is returned, an error dialog is shown
        """
        ...

    def getScriptInfo(self, scriptFile: generic.jar.ResourceFile) -> ghidra.app.script.ScriptInfo:
        """
        Returns the script info object for the specified script file,
         construct a new one if necessary.

         <p>Only call this method if you expect to be creating ScriptInfo objects.
         Prefer getExistingScriptInfo instead.
        @param scriptFile the script file
        @return the script info object for the specified script file
        """
        ...

    def getScriptInfoIterable(self) -> java.lang.Iterable:
        """
        get all scripts
        @return an iterable over all script info objects
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def refreshDuplicates(self) -> None:
        """
        Updates every known script's duplicate value.
        """
        ...

    def removeMetadata(self, scriptFile: generic.jar.ResourceFile) -> None:
        """
        Removes the ScriptInfo object for the specified file
        @param scriptFile the script file
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
    def scriptInfoIterable(self) -> java.lang.Iterable: ...
