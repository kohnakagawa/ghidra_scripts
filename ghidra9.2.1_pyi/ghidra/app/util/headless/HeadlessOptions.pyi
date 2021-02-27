from typing import List
import java.lang


class HeadlessOptions(object):
    """
    Options for headless analyzer.

     Option state may be adjusted to reflect assumed options
     during processing.  If multiple invocations of either
     HeadlessAnalyzer#processLocal(String, String, String, List) or
     HeadlessAnalyzer#processURL(java.net.URL, List) are performed,
     these options should be reset and adjusted as necessary.
    """









    def enableAnalysis(self, enabled: bool) -> None:
        """
        Auto-analysis is enabled by default following import.  This method can be
         used to change the enablement of auto-analysis.
        @param enabled True if auto-analysis should be enabled; otherwise, false.
        """
        ...

    def enableOverwriteOnConflict(self, enabled: bool) -> None:
        """
        During import, the default behavior is to skip the import if a conflict occurs
         within the destination folder.  This method can be used to force the original
         conflicting file to be removed prior to import.
         If the pre-existing file is versioned, the commit option must also be
         enabled to have the overwrite remove the versioned file.
        @param enabled if true conflicting domain files will be removed from the
         project prior to importing the new file.
        """
        ...

    def enableReadOnlyProcessing(self, enabled: bool) -> None:
        """
        When readOnly processing is enabled, any changes made by script or analyzers
         are discarded when the Headless Analyzer exits.  When used with import mode,
         the imported program file will not be saved to the project or repository.
        @param enabled if true, enables readOnly processing or import
        """
        ...

    def enableRecursiveProcessing(self, enabled: bool) -> None:
        """
        This method can be used to enable recursive processing of files during
         <code>-import</code> or <code>-process</code> modes.  In order for recursive processing of files to
         occur, the user must have specified a directory (and not a specific file)
         for the Headless Analyzer to import or process.
        @param enabled if true, enables recursive processing
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def reset(self) -> None:
        """
        Resets the options to its default settings.
        """
        ...

    def setClientCredentials(self, userID: unicode, keystorePath: unicode, allowPasswordPrompt: bool) -> None:
        """
        Set Ghidra Server client credentials to be used with "shared" projects.
        @param userID optional userId to use if server permits the user to use
         a userId which differs from the process owner name.
        @param keystorePath file path to keystore file containing users private key
         to be used with PKI or SSH based authentication.
        @param allowPasswordPrompt if true the user may be prompted for passwords
         via the console (stdin).  Please note that the Java console will echo
         the password entry to the terminal which may be undesirable.
        @throws IOException if an error occurs while opening the specified keystorePath.
        """
        ...

    def setCommitFiles(self, commit: bool, comment: unicode) -> None:
        """
        Enable committing of processed files to the repository which backs the specified
         project.
        @param commit if true imported files will be committed
        @param comment optional comment to use when committing
        """
        ...

    def setDeleteCreatedProjectOnClose(self, enabled: bool) -> None:
        """
        Set project delete flag which allows temporary projects created
         to be deleted upon completion.  This option has no effect if a
         Ghidra URL or an existing project was specified.  This option
         will be assumed when importing with the readOnly option enabled.
        @param enabled if true a created project will be deleted when
         processing is complete.
        """
        ...

    def setLanguageAndCompiler(self, languageId: unicode, compilerSpecId: unicode) -> None:
        """
        Sets the language and compiler spec from the provided input. Any null value will attempt
         a "best-guess" if possible.
        @param languageId The language to set.
        @param compilerSpecId The compiler spec to set.
        @throws InvalidInputException if the language and compiler spec combination is not valid.
        """
        ...

    def setLoader(self, __a0: unicode, __a1: List[object]) -> None: ...

    def setMaxCpu(self, cpu: int) -> None:
        """
        Sets the maximum number of cpu cores to use during headless processing.
        @param cpu The maximum number of cpu cores to use during headless processing.
             Setting it to 0 or a negative integer is equivalent to setting it to 1.
        """
        ...

    def setOkToDelete(self, deleteOk: bool) -> None: ...

    @overload
    def setPerFileAnalysisTimeout(self, secs: int) -> None: ...

    @overload
    def setPerFileAnalysisTimeout(self, stringInSecs: unicode) -> None:
        """
        Set analyzer timeout on a per-file basis.
        @param stringInSecs timeout value in seconds (as a String)
        @throws InvalidInputException if the timeout value was not a valid value
        """
        ...

    def setPostScripts(self, __a0: List[object]) -> None: ...

    def setPostScriptsWithArgs(self, __a0: List[object]) -> None: ...

    def setPreScripts(self, __a0: List[object]) -> None: ...

    def setPreScriptsWithArgs(self, __a0: List[object]) -> None: ...

    @overload
    def setPropertiesFileDirectories(self, paths: unicode) -> None:
        """
        List of valid .properties file directory paths, separated by a ';'.

         Typically, .properties files should be located in the same directory as their corresponding
         scripts. However, this method may need to be used when circumstances make it impossible to
         have both files in the same directory (i.e., if the scripts are included in ghidra.jar).
        @param paths String representation of directories (each separated by ';')
        """
        ...

    @overload
    def setPropertiesFileDirectories(self, __a0: List[object]) -> None: ...

    def setPropertiesFileDirectory(self, path: unicode) -> None:
        """
        Sets a single location for .properties files associated with GhidraScripts.

         Typically, .properties files should be located in the same directory as their corresponding
         scripts. However, this method may need to be used when circumstances make it impossible to
         have both files in the same directory (i.e., if the scripts are included in ghidra.jar).
        @param path location of .properties file(s)
        """
        ...

    def setRunScriptsNoImport(self, runScriptsOnly: bool, filename: unicode) -> None:
        """
        Set to run scripts (and optionally, analysis) without importing a
         program.  Scripts will run on specified folder or program that already
         exists in the project.
        @param runScriptsOnly if true, no imports will occur and scripts
         						 (and analysis, if enabled) will run on the specified existing program
         					     or directory of programs.
        @param filename name of specific project file or folder to be processed (the location
         					 is passed in elsewhere by the user).  If null, user has not specified
         					 a file to process -- therefore, the entire directory will be processed.
         					 The filename should not include folder path elements which should be
                           specified separately via project or URL specification.
        @throws IllegalArgumentException if the specified filename is invalid and contains the
         path separator character '/'.
        """
        ...

    @overload
    def setScriptDirectories(self, paths: unicode) -> None:
        """
        List of valid script directory paths separated by a ';'.
         The default set of enabled script directories within the Ghidra installation
         will be appended to the specified list of newPaths.
         Individual Paths may be constructed relative to Ghidra installation directory,
         User home directory, or absolute system paths.  Examples:
         <pre>
         		Path.GHIDRA_HOME + "/Ghidra/Features/Base/ghidra_scripts"
              Path.USER_HOME + "/Ghidra/Features/Base/ghidra_scripts"
        		"/shared/ghidra_scripts"
         </pre>
        @param paths semicolon (';') separated list of directory paths
        """
        ...

    @overload
    def setScriptDirectories(self, __a0: List[object]) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def deleteCreatedProjectOnClose(self) -> None: ...  # No getter available.

    @deleteCreatedProjectOnClose.setter
    def deleteCreatedProjectOnClose(self, value: bool) -> None: ...

    @property
    def maxCpu(self) -> None: ...  # No getter available.

    @maxCpu.setter
    def maxCpu(self, value: int) -> None: ...

    @property
    def okToDelete(self) -> None: ...  # No getter available.

    @okToDelete.setter
    def okToDelete(self, value: bool) -> None: ...

    @property
    def perFileAnalysisTimeout(self) -> None: ...  # No getter available.

    @perFileAnalysisTimeout.setter
    def perFileAnalysisTimeout(self, value: int) -> None: ...

    @property
    def postScripts(self) -> None: ...  # No getter available.

    @postScripts.setter
    def postScripts(self, value: List[object]) -> None: ...

    @property
    def postScriptsWithArgs(self) -> None: ...  # No getter available.

    @postScriptsWithArgs.setter
    def postScriptsWithArgs(self, value: List[object]) -> None: ...

    @property
    def preScripts(self) -> None: ...  # No getter available.

    @preScripts.setter
    def preScripts(self, value: List[object]) -> None: ...

    @property
    def preScriptsWithArgs(self) -> None: ...  # No getter available.

    @preScriptsWithArgs.setter
    def preScriptsWithArgs(self, value: List[object]) -> None: ...

    @property
    def propertiesFileDirectories(self) -> None: ...  # No getter available.

    @propertiesFileDirectories.setter
    def propertiesFileDirectories(self, value: unicode) -> None: ...

    @property
    def propertiesFileDirectory(self) -> None: ...  # No getter available.

    @propertiesFileDirectory.setter
    def propertiesFileDirectory(self, value: unicode) -> None: ...

    @property
    def scriptDirectories(self) -> None: ...  # No getter available.

    @scriptDirectories.setter
    def scriptDirectories(self, value: unicode) -> None: ...
