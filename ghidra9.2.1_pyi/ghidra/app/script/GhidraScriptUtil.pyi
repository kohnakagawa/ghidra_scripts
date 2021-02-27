from typing import List
import generic.jar
import ghidra.app.plugin.core.osgi
import ghidra.app.script
import java.lang


class GhidraScriptUtil(object):
    """
    A utility class for managing script directories and ScriptInfo objects.
    """

    USER_SCRIPTS_DIR: unicode



    def __init__(self): ...



    @staticmethod
    def acquireBundleHostReference() -> ghidra.app.plugin.core.osgi.BundleHost:
        """
        When running the GUI, {@link GhidraScriptUtil} manages a single {@link BundleHost} instance.
        @return the BundleHost singleton
        """
        ...

    @staticmethod
    def createNewScript(__a0: ghidra.app.script.GhidraScriptProvider, __a1: generic.jar.ResourceFile, __a2: List[object]) -> generic.jar.ResourceFile: ...

    @staticmethod
    def dispose() -> None:
        """
        dispose of the bundle host and providers list
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def findScriptByName(scriptName: unicode) -> generic.jar.ResourceFile:
        """
        Search the currently managed scripts for one with the given name.
        @param scriptName the name
        @return the first file found or null if none are found
        """
        ...

    @staticmethod
    def findSourceDirectoryContaining(sourceFile: generic.jar.ResourceFile) -> generic.jar.ResourceFile:
        """
        Search the currently managed source directories for the given script file.
        @param sourceFile the source file
        @return the source directory if found, or null if not
        """
        ...

    @staticmethod
    def getBaseName(script: generic.jar.ResourceFile) -> unicode:
        """
        Returns the base name give a script file.
         For example, given "C:\Temp\SomeClass.java",
         it will return "SomeClass".
        @param script the script
        @return the base name
        """
        ...

    @staticmethod
    def getBundleHost() -> ghidra.app.plugin.core.osgi.BundleHost:
        """
        @return the bundle host used for scripting
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getExplodedCompiledSourceBundlePaths() -> List[generic.jar.ResourceFile]:
        """
        Returns the list of exploded bundle directories
        @return the list
        @deprecated accessing class file directly precludes OSGi wiring according to requirements and capabilities
        """
        ...

    @staticmethod
    def getProvider(scriptFile: generic.jar.ResourceFile) -> ghidra.app.script.GhidraScriptProvider:
        """
        Returns the corresponding Ghidra script providers
         for the specified script file.
        @param scriptFile the script file
        @return the Ghidra script provider
        """
        ...

    @staticmethod
    def getProviders() -> List[ghidra.app.script.GhidraScriptProvider]:
        """
        Returns a list of all Ghidra script providers
        @return a list of all Ghidra script providers
        """
        ...

    @staticmethod
    def getScriptSourceDirectories() -> List[generic.jar.ResourceFile]:
        """
        Returns a list of the current script directories.
        @return a list of the current script directories
        """
        ...

    @staticmethod
    def getSystemScriptDirectories() -> List[generic.jar.ResourceFile]:
        """
        Returns a list of the default script directories.
        @return a list of the default script directories
        """
        ...

    @staticmethod
    def getUserScriptDirectory() -> generic.jar.ResourceFile: ...

    @staticmethod
    def hasScriptProvider(scriptFile: generic.jar.ResourceFile) -> bool:
        """
        Returns true if a provider exists that can process the specified file.
        @param scriptFile the script file
        @return true if a provider exists that can process the specified file
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def initialize(__a0: ghidra.app.plugin.core.osgi.BundleHost, __a1: List[object]) -> None: ...

    @staticmethod
    def isSystemScript(file: generic.jar.ResourceFile) -> bool:
        """
        Determine if the specified file is contained within the Ghidra installation.
        @param file script file or directory
        @return true if file contained within Ghidra installation area
        """
        ...

    @staticmethod
    def newScriptInfo(file: generic.jar.ResourceFile) -> ghidra.app.script.ScriptInfo: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def releaseBundleHostReference() -> None:
        """
        release the reference the BundleHost reference.  When no references remain,
         {@link #dispose()} is called.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
