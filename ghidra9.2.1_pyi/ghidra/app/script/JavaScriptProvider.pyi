import generic.jar
import ghidra.app.plugin.core.osgi
import ghidra.app.script
import java.io
import java.lang


class JavaScriptProvider(ghidra.app.script.GhidraScriptProvider):




    def __init__(self):
        """
        Create a new {@link JavaScriptProvider} associated with the current bundle host used by scripting.
        """
        ...



    @overload
    def compareTo(self, that: ghidra.app.script.GhidraScriptProvider) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def createNewScript(self, newScript: generic.jar.ResourceFile, category: unicode) -> None: ...

    def deleteScript(self, sourceFile: generic.jar.ResourceFile) -> bool: ...

    def equals(self, obj: object) -> bool: ...

    def getBundleForSource(self, sourceFile: generic.jar.ResourceFile) -> ghidra.app.plugin.core.osgi.GhidraSourceBundle:
        """
        Get the {@link GhidraSourceBundle} containing the given source file, assuming it already exists.
        @param sourceFile the source file
        @return the bundle
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getCommentCharacter(self) -> unicode: ...

    def getDescription(self) -> unicode: ...

    def getExtension(self) -> unicode: ...

    def getScriptInstance(self, sourceFile: generic.jar.ResourceFile, writer: java.io.PrintWriter) -> ghidra.app.script.GhidraScript: ...

    def hashCode(self) -> int: ...

    def loadClass(self, sourceFile: generic.jar.ResourceFile, writer: java.io.PrintWriter) -> java.lang.Class:
        """
        Activate and build the {@link GhidraSourceBundle} containing {@code sourceFile}
         then load the script's class from its class loader.
        @param sourceFile the source file
        @param writer the target for build messages
        @return the loaded {@link Class} object
        @throws Exception if build, activation, or class loading fail
        """
        ...

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
