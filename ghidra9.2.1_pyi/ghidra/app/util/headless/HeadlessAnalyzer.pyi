from typing import List
import ghidra.app.util.headless
import java.io
import java.lang
import java.net


class HeadlessAnalyzer(object):
    """
    The class used kick-off and interact with headless processing.  All headless options have been
     broken out into their own class: HeadlessOptions.  This class is intended to be used
     one of two ways:

       Used by AnalyzeHeadless to perform headless analysis based on arguments specified
       on the command line.
       Used by another tool as a library to perform headless analysis.


     Note: This class is not thread safe.
    """









    def checkAnalysisTimedOut(self) -> bool:
        """
        Checks to see if the most recent analysis timed out.
        @return true if the most recent analysis timed out; otherwise, false.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getInstance() -> ghidra.app.util.headless.HeadlessAnalyzer:
        """
        Gets a headless analyzer instance, with the assumption that the application has already been
         initialized.  If this is called before the application has been initialized, it will
         initialize the application with no logging.
        @return An instance of a new headless analyzer.
        @throws IOException if there was a problem reading the application.properties file (only possible
             if the application had not be initialized).
        """
        ...

    @staticmethod
    def getLoggableInstance(logFile: java.io.File, scriptLogFile: java.io.File, useLog4j: bool) -> ghidra.app.util.headless.HeadlessAnalyzer:
        """
        Gets a headless analyzer, initializing the application if necessary with the specified
         logging parameters.  An {@link IllegalStateException} will be thrown if the application has
         already been initialized or a headless analyzer has already been retrieved.  In these cases,
         the headless analyzer should be gotten with {@link HeadlessAnalyzer#getInstance()}.
        @param logFile The desired application log file.  If null, no application logging will take place.
        @param scriptLogFile The desired scripting log file.  If null, no script logging will take place.
        @param useLog4j true if log4j is to be used; otherwise, false.  If this class is being used by
             another tool as a library, using log4j might interfere with that tool.
        @return An instance of a new headless analyzer.
        @throws IllegalStateException if an application or headless analyzer instance has already been initialized.
        @throws IOException if there was a problem reading the application.properties file.
        """
        ...

    def getOptions(self) -> ghidra.app.util.headless.HeadlessOptions:
        """
        Gets the headless analyzer's options.
        @return The headless analyer's options.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def processLocal(self, __a0: unicode, __a1: unicode, __a2: unicode, __a3: List[object]) -> None: ...

    def processURL(self, __a0: java.net.URL, __a1: List[object]) -> None: ...

    def reset(self) -> None:
        """
        Resets the state of the headless analyzer to the default settings.
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
    def options(self) -> ghidra.app.util.headless.HeadlessOptions: ...
