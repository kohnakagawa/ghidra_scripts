from typing import List
import ghidra.app.decompiler
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.pcode
import ghidra.xml
import java.awt
import java.lang


class ClangFieldToken(ghidra.app.decompiler.ClangToken):
    """
    A C code token representing a structure field.
    """





    def __init__(self, par: ghidra.app.decompiler.ClangNode): ...



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

    def getDataType(self) -> ghidra.program.model.data.DataType:
        """
        @return the structure datatype associated with this field token
        """
        ...

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

    def getOffset(self) -> int:
        """
        @return the byte offset of this field with its structure
        """
        ...

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
    def dataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def offset(self) -> int: ...