from typing import List
import docking
import generic.jar
import ghidra.base.project
import ghidra.framework.main
import ghidra.framework.model
import ghidra.framework.plugintool
import ghidra.program.database
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.test
import ghidra.util.task
import java.awt
import java.io
import java.lang


class TestEnv(object):




    @overload
    def __init__(self):
        """
        Constructor for Ghidra
         A new test project is established.
         If it already exists it will first be deleted.
        @throws IOException if there is an issue creating a test project
        """
        ...

    @overload
    def __init__(self, projectName: unicode):
        """
        Constructor for Ghidra
         A new test project is established using the specified projectName.
         If it already exists it will first be deleted.
         If the test environment is not disposed within 1 minute the tests iwll be aborted
        @param projectName the name of the project
        @throws IOException if there is an issue creating a test project
        """
        ...

    @overload
    def __init__(self, abortTimeout: long, projectName: unicode):
        """
        Constructor for Ghidra
         A new test project is established using the specified projectName.
         If it already exists it will first be deleted.
        @param abortTimeout number of minutes within which this test environment must be
         		  disposed.  If not disposed in a timely manner, System.exit will be invoked.
        @param projectName the name of the project
        @throws IOException if there is an issue creating a test project
        """
        ...



    def addPlugin(self, c: java.lang.Class) -> object:
        """
        Adds and returns the plugin to this env's tool for the given class.

         <P>If you have not created a tool using this env, then the default
         tool from {@link #lazyTool()} is used.  If you have launched a tool, then that tool
         is used.   In the following example, the given plugin is added to the default tool:
         <pre>
         		TestEnv env = new TestEnv();
         		env.launchDefaultTool();
         		FooPlugin foo = env.addPlugin(FooPlugin.class);
         </pre>
        @param c the plugin class
        @return the plugin instance
        @throws PluginException if there is an exception adding the given tool
        """
        ...

    def close(self, p: ghidra.program.model.listing.Program) -> None:
        """
        Closes the given program, ignoring all changes, for each tool known to this TestEnv.
        @param p the program to close
        """
        ...

    def closeAndReopenProject(self) -> None:
        """
        A convenience method to close and then reopen the default project created by this TestEnv
         instance.  This will not delete the project between opening and closing and will restore
         the project to its previous state.
        @throws IOException if any exception occurs while saving and reopening
        """
        ...

    @overload
    def closeTool(self) -> None:
        """
        Closes the TestEnv's default tool.  This method is asynchronous, so you
         must wait for the Swing thread to perform the work yourself.
         Watch out for modal dialogs.
        """
        ...

    @overload
    def closeTool(self, toolToClose: ghidra.framework.plugintool.PluginTool) -> None:
        """
        Closes the given tool.  This method is asynchronous, so you must wait for the Swing thread
         to perform the work yourself.  Watch out for modal dialogs.
        @param toolToClose The tool to close.
        """
        ...

    @overload
    def closeTool(self, toolToClose: ghidra.framework.plugintool.PluginTool, ignoreChanges: bool) -> None: ...

    def connectTools(self, producer: ghidra.framework.plugintool.PluginTool, consumer: ghidra.framework.plugintool.PluginTool) -> ghidra.framework.model.ToolConnection: ...

    def createDefaultTool(self) -> ghidra.framework.plugintool.PluginTool:
        """
        This method differs from {@link #launchDefaultTool()} in that this method does not set the
         <code>tool</code> variable in of this <code>TestEnv</code> instance.
        @return the tool
        """
        ...

    def disconnectTools(self, producer: ghidra.framework.plugintool.PluginTool, consumer: ghidra.framework.plugintool.PluginTool) -> None: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def findProvidedDataTypeArchive(relativePathName: unicode) -> generic.jar.ResourceFile: ...

    def getClass(self) -> java.lang.Class: ...

    def getFrontEndProvider(self) -> docking.ComponentProvider: ...

    def getFrontEndTool(self) -> ghidra.framework.main.FrontEndTool: ...

    def getGhidraCreatedTools(self) -> List[ghidra.framework.plugintool.PluginTool]:
        """
        Returns an array of tools spawned by the Ghidra environment.
         NOTE: This array will not contain any of the TestTools!
        @return an array of tools spawned by the Ghidra environment
        """
        ...

    def getGhidraProject(self) -> ghidra.base.project.GhidraProject:
        """
        Returns GhidraProject associated with this environment
        @return the project
        """
        ...

    def getPlugin(self, c: java.lang.Class) -> object: ...

    def getProgram(self, programName: unicode) -> ghidra.program.database.ProgramDB:
        """
        Open a read-only test program from the test data directory.
         This program must be released prior to disposing this test environment.
         NOTE: Some tests rely on this method returning null when file does
         not yet exist within the resource area (e.g., test binaries for P-Code Tests)
        @param programName name of program database within the test data directory.
        @return program or null if program file not found
        """
        ...

    def getProject(self) -> ghidra.framework.model.Project: ...

    def getProjectManager(self) -> ghidra.framework.model.ProjectManager: ...

    def getTool(self) -> ghidra.framework.plugintool.PluginTool:
        """
        Get the tool associated with this test environment.
        @return the default test tool for this environment
        """
        ...

    def hashCode(self) -> int: ...

    def isProgramCached(self, programName: unicode) -> bool:
        """
        Determine if specified program already exists with the program cache
        @param programName the name
        @return true if specified program already exists with the program cache
        """
        ...

    def launchAnotherDefaultTool(self) -> ghidra.framework.plugintool.PluginTool:
        """
        Launches another default tool, not overwriting this env's current tool.
        @return the new tool
        """
        ...

    @overload
    def launchDefaultTool(self) -> ghidra.framework.plugintool.PluginTool:
        """
        Launches the default tool of the test system ("CodeBrowser").
         This method will load the tool from resources and <b>not from the
         user's Ghidra settings</b>.
         <p>
         <b>Note:</b> Calling this method also changes the tool that this
         instance of the TestEnv is using, which is the reason for the existence
         of this method.
        @return the tool that is launched
        """
        ...

    @overload
    def launchDefaultTool(self, program: ghidra.program.model.listing.Program) -> ghidra.framework.plugintool.PluginTool:
        """
        Launches the default tool of the test system ("CodeBrowser") using the
         given program.   This method will load the tool from resources and <b>not from the
         user's Ghidra settings</b>.
         <p>
         <b>Note:</b> Calling this method also changes the tool that this
         instance of the TestEnv is using, which is the reason for the existence
         of this method.
        @param program The program to load into the default tool; may be null
        @return the tool that is launched
        """
        ...

    @overload
    def launchTool(self, toolName: unicode) -> ghidra.framework.plugintool.PluginTool:
        """
        Launches a tool of the given name using the given domain file.
         <p>
         Note: the tool returned will have auto save disabled by default.
        @param toolName the tool's name
        @return the tool that is launched
        """
        ...

    @overload
    def launchTool(self, toolName: unicode, domainFile: ghidra.framework.model.DomainFile) -> ghidra.framework.plugintool.PluginTool:
        """
        Launches a tool of the given name using the given domain file.
         <p>
         Note: the tool returned will have auto save disabled by default.
        @param toolName the name of the tool to launch
        @param domainFile The domain file used to launch the tool; may be null
        @return the tool that is launched
        """
        ...

    def loadAnalyzedNotepad(self) -> ghidra.program.database.ProgramDB: ...

    @overload
    def loadResourceProgramAsBinary(self, programName: unicode, processor: ghidra.program.model.lang.Processor) -> ghidra.program.model.listing.Program: ...

    @overload
    def loadResourceProgramAsBinary(self, programName: unicode, language: ghidra.program.model.lang.Language, compilerSpec: ghidra.program.model.lang.CompilerSpec) -> ghidra.program.model.listing.Program: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def open(self, program: ghidra.program.model.listing.Program) -> None:
        """
        Opens the given program in the test tool.
        @param program the program to open
        """
        ...

    def release(self, program: ghidra.program.model.listing.Program) -> None:
        """
        Release a program which was obtained from this test environment.
        @param program the program
        """
        ...

    def removeFromProgramCache(self, programName: unicode) -> None:
        """
        Remove specified program from cache
        @param programName the name
        """
        ...

    def resetDefaultTools(self) -> None: ...

    def restartTool(self) -> ghidra.framework.plugintool.PluginTool: ...

    def restoreDataTypeArchive(self, relativePathName: unicode, domainFolder: ghidra.framework.model.DomainFolder) -> ghidra.framework.model.DomainFile:
        """
        Creates a project data type archive in the indicated test project folder from the ".gdt"
         file indicated by the relative pathname.
        @param relativePathName This should be a pathname relative to the "test_resources/testdata"
         		  director or relative to the "typeinfo" directory. The name should
                include the ".gdt" suffix.
        @param domainFolder the folder in the test project where the archive should be created
        @return the domain file  that was created in the project
        @throws Exception if an exception occurs
        """
        ...

    def restoreProgram(self, programName: unicode) -> ghidra.framework.model.DomainFile:
        """
        Copies the specified program zip file to the JUnit test project's root folder. <b>This
         means that the program will appear in the FrontEndTool as part of the project.</b>  That is
         the only reason to use this method vice openProgram().
        @param programName the name of the program zip file without the ".gzf" extension.
        @return the restored domain file
        @throws FileNotFoundException if the program file cannot be found
        """
        ...

    def runScript(self, scriptFile: java.io.File) -> ghidra.test.ScriptTaskListener: ...

    def saveRestoreToolState(self) -> None: ...

    def saveToCache(self, progName: unicode, program: ghidra.program.database.ProgramDB, replace: bool, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Save a program to the cached program store.  A SaveAs will be performed on the
         program to its cached storage location.
        @param progName program name
        @param program program object
        @param replace if true any existing cached database with the same name will be replaced
        @param monitor task monitor
        @throws Exception if already cached
        """
        ...

    def setAutoSaveEnabled(self, enabled: bool) -> None:
        """
        Sets the auto-save feature for all tool instances running under the {@link FrontEndTool}
         created by this TestEnv instance.  Auto-save is off by default when testing.
        @param enabled true enables auto-save
        """
        ...

    def showFrontEndTool(self) -> ghidra.framework.main.FrontEndTool: ...

    @overload
    def showTool(self) -> ghidra.framework.plugintool.PluginTool:
        """
        Shows any previously created tool, creating a simple empty tool if not tool has yet
         been created.

         <P>This method is considered sub-standard and users should prefer instead
         {@link #launchDefaultTool()} or {@link #launchDefaultTool(Program)}.
        @return the newly shown tool
        """
        ...

    @overload
    def showTool(self, p: ghidra.program.model.listing.Program) -> ghidra.framework.plugintool.PluginTool:
        """
        Shows any previously created tool, creating a simple empty tool if not tool has yet
         been created.  The given program will be opened in the tool.

         <P>This method is considered sub-standard and users should prefer instead
         {@link #launchDefaultTool()} or {@link #launchDefaultTool(Program)}.
        @param p the program
        @return the newly shown tool
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def waitForDialogComponent(self, ghidraClass: java.lang.Class, maxTimeMS: int) -> object:
        """
        Waits for the first window of the given class.  This method is the same as
         {@link #waitForDialogComponent(Class, int)} with the exception that the parent
         window is assumed to be this instance's tool frame.
        @param ghidraClass The class of the dialog the user desires
        @param maxTimeMS The max amount of time in milliseconds to wait for the requested dialog
                to appear.
        @return The first occurrence of a dialog that extends the given <code>ghirdraClass</code>
        @deprecated use instead {@link AbstractDockingTest#waitForDialogComponent(Class)}
        """
        ...

    def waitForWindow(self, title: unicode, timeoutMS: int) -> java.awt.Window: ...

    @property
    def autoSaveEnabled(self) -> None: ...  # No getter available.

    @autoSaveEnabled.setter
    def autoSaveEnabled(self, value: bool) -> None: ...

    @property
    def frontEndProvider(self) -> docking.ComponentProvider: ...

    @property
    def frontEndTool(self) -> ghidra.framework.main.FrontEndTool: ...

    @property
    def ghidraCreatedTools(self) -> List[ghidra.framework.plugintool.PluginTool]: ...

    @property
    def ghidraProject(self) -> ghidra.base.project.GhidraProject: ...

    @property
    def project(self) -> ghidra.framework.model.Project: ...

    @property
    def projectManager(self) -> ghidra.framework.model.ProjectManager: ...

    @property
    def tool(self) -> ghidra.framework.plugintool.PluginTool: ...
