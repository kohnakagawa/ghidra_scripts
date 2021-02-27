from typing import List
import ghidra.app.decompiler
import ghidra.program.model.address
import ghidra.program.model.pcode
import ghidra.xml
import java.awt
import java.lang


class ClangToken(object, ghidra.app.decompiler.ClangNode):
    """
    Class representing a C code language token
     May contain links back to pcode object
    """

    COMMENT_COLOR: int = 3
    CONST_COLOR: int = 5
    DEFAULT_COLOR: int = 8
    FUNCTION_COLOR: int = 2
    GLOBAL_COLOR: int = 7
    KEYWORD_COLOR: int = 0
    PARAMETER_COLOR: int = 6
    TYPE_COLOR: int = 1
    VARIABLE_COLOR: int = 4



    @overload
    def __init__(self, par: ghidra.app.decompiler.ClangNode): ...

    @overload
    def __init__(self, par: ghidra.app.decompiler.ClangNode, txt: unicode): ...

    @overload
    def __init__(self, par: ghidra.app.decompiler.ClangNode, txt: unicode, col: unicode): ...



    def Child(self, i: int) -> ghidra.app.decompiler.ClangNode: ...

    def Parent(self) -> ghidra.app.decompiler.ClangNode: ...

    @staticmethod
    def buildSpacer(par: ghidra.app.decompiler.ClangNode, indent: int, indentStr: unicode) -> ghidra.app.decompiler.ClangToken: ...

    @staticmethod
    def buildToken(par: ghidra.app.decompiler.ClangNode, parser: ghidra.xml.XmlPullParser, pfactory: ghidra.program.model.pcode.PcodeFactory) -> ghidra.app.decompiler.ClangToken: ...

    def equals(self, __a0: object) -> bool: ...

    def flatten(self, __a0: List[object]) -> None: ...

    def getClangFunction(self) -> ghidra.app.decompiler.ClangFunction: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getColor(col: unicode) -> int: ...

    def getHighVariable(self) -> ghidra.program.model.pcode.HighVariable:
        """
        Get the high-level variable associate with this
         token or null otherwise
        @return HighVariable
        """
        ...

    def getHighlight(self) -> java.awt.Color: ...

    def getLineParent(self) -> ghidra.app.decompiler.ClangLine: ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address: ...

    def getMinAddress(self) -> ghidra.program.model.address.Address: ...

    def getPcodeOp(self) -> ghidra.program.model.pcode.PcodeOp:
        """
        Many tokens directly represent a pcode operator in the data-flow
        @return the operation (PcodeOp) associated with this token or null
        """
        ...

    def getSyntaxType(self) -> int: ...

    def getText(self) -> unicode: ...

    def getVarnode(self) -> ghidra.program.model.pcode.Varnode:
        """
        Many tokens directly represent a variable in the data-flow
        @return the variable (Varnode) associated with this token or null
        """
        ...

    def hashCode(self) -> int: ...

    def isMatchingToken(self) -> bool: ...

    def isVariableRef(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def numChildren(self) -> int: ...

    def restoreFromXML(self, el: ghidra.xml.XmlElement, end: ghidra.xml.XmlElement, pfactory: ghidra.program.model.pcode.PcodeFactory) -> None: ...

    def setHighlight(self, val: java.awt.Color) -> None: ...

    def setLineParent(self, line: ghidra.app.decompiler.ClangLine) -> None: ...

    def setMatchingToken(self, matchingToken: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def clangFunction(self) -> ghidra.app.decompiler.ClangFunction: ...

    @property
    def highVariable(self) -> ghidra.program.model.pcode.HighVariable: ...

    @property
    def highlight(self) -> java.awt.Color: ...

    @highlight.setter
    def highlight(self, value: java.awt.Color) -> None: ...

    @property
    def lineParent(self) -> ghidra.app.decompiler.ClangLine: ...

    @lineParent.setter
    def lineParent(self, value: ghidra.app.decompiler.ClangLine) -> None: ...

    @property
    def matchingToken(self) -> bool: ...

    @matchingToken.setter
    def matchingToken(self, value: bool) -> None: ...

    @property
    def maxAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def minAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def pcodeOp(self) -> ghidra.program.model.pcode.PcodeOp: ...

    @property
    def syntaxType(self) -> int: ...

    @property
    def text(self) -> unicode: ...

    @property
    def variableRef(self) -> bool: ...

    @property
    def varnode(self) -> ghidra.program.model.pcode.Varnode: ...
