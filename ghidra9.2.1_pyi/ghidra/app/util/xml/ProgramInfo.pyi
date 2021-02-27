import java.lang


class ProgramInfo(object):
    """
    This class stores values pulled from the
     PROGRAM, INFO_SOURCE, and LANGUAGE tag inside a ghidra program XML file.

     Please see PROGRAM.DTD
    """

    addressModel: unicode
    compilerSpecID: ghidra.program.model.lang.CompilerSpecID
    endian: unicode
    exeFormat: unicode
    exePath: unicode
    family: unicode
    imageBase: unicode
    languageID: ghidra.program.model.lang.LanguageID
    processorName: unicode
    programName: unicode
    timestamp: unicode
    user: unicode
    version: unicode



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getNormalizedExternalToolName(self) -> unicode:
        """
        Returns normalizedExternalToolName field.  This is the name of the tool normalized into known categories ("IDA-PRO" or "GHIDRA") if appropriate.
        @return normalizedExternalToolName
        """
        ...

    def getTool(self) -> unicode:
        """
        Returns tool field.  This is the name of the tool exactly as written in the XML being imported.
        @return tool field
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setCompilerSpecID(self, compiler: unicode) -> None: ...

    def setTool(self, tool: unicode) -> None:
        """
        Sets tool field.
         Also sets normalizedExternalToolName to normalized tool names "IDA-PRO" or "GHIDRA" if appropriate, or just sets it to the value of tool.
        """
        ...

    def shouldProcessStack(self) -> bool:
        """
        whether the XmlMgr should process stack frames and references.
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
    def normalizedExternalToolName(self) -> unicode: ...

    @property
    def tool(self) -> unicode: ...

    @tool.setter
    def tool(self, value: unicode) -> None: ...
