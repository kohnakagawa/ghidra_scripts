import ghidra.framework.plugintool
import ghidra.program.model.listing
import java.lang


class GhidraProgramUtilities(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getCurrentProgram(tool: ghidra.framework.plugintool.PluginTool) -> ghidra.program.model.listing.Program:
        """
        returns the current program, given a tool, if a program is opened;
         otherwise returns null.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def removeAnalyzedFlag(program: ghidra.program.model.listing.Program) -> None:
        """
        Removes the analyzed flag from the program properties.
         With this property removed, the user will be prompted to analyze the
         program the next time it is opened.
        @param program the program containing the property to be removed
        """
        ...

    @staticmethod
    def setAnalyzedFlag(program: ghidra.program.model.listing.Program, analyzed: bool) -> None:
        """
        Sets the analyzed flag to the specified value.
        @param program the program to set property
        @param analyzed the analyzed flag
        """
        ...

    @staticmethod
    def shouldAskToAnalyze(program: ghidra.program.model.listing.Program) -> bool:
        """
        Returns true if the program does not contain the analyzed flag.
        @param program the program to check for the property
        @return true if the program does not contain the analyzed flag
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
