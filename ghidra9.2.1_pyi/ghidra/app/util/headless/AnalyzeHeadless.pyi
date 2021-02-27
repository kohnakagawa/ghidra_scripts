from typing import List
import ghidra
import java.lang


class AnalyzeHeadless(object, ghidra.GhidraLaunchable):
    """
    Launcher entry point for running headless Ghidra.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def launch(self, layout: ghidra.GhidraApplicationLayout, args: List[unicode]) -> None:
        """
        The entry point of 'analyzeHeadless.bat'. Parses the command line arguments to the script
         and takes the appropriate headless actions.
        @param args Detailed list of arguments is in 'analyzeHeadlessREADME.html'
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @staticmethod
    def usage(execCmd: unicode) -> None:
        """
        Prints out the usage details and exits the Java application with an exit code that
         indicates error.
        @param execCmd the command used to run the headless analyzer from the calling method.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
