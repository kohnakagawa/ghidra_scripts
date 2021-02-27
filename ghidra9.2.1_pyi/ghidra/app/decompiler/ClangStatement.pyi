from typing import List
import ghidra.app.decompiler
import ghidra.program.model.address
import ghidra.program.model.pcode
import ghidra.xml
import java.awt
import java.lang


class ClangStatement(ghidra.app.decompiler.ClangTokenGroup):
    """
    A C code statement. What typically appears between the ';' '{' and '}' characters.
     A statement must have a pcode operation associated with it. In the case of conditional
     flow control operations, there are usually two lines associated with the statement one
     containing the '{' and one containing '}'. The one containing the actual conditional branch
     is considered a C statement, while the other one is just considered a blank line.
     I.e.
     	if (expression) {
     is a C statement, while the line containing the closing '}' by itself is considered blank
    """





    def __init__(self, par: ghidra.app.decompiler.ClangNode): ...



    def AddTokenGroup(self, obj: object) -> None: ...

    def Child(self, i: int) -> ghidra.app.decompiler.ClangNode: ...

    def Parent(self) -> ghidra.app.decompiler.ClangNode: ...

    def equals(self, __a0: object) -> bool: ...

    def flatten(self, __a0: List[object]) -> None: ...

    def getClangFunction(self) -> ghidra.app.decompiler.ClangFunction: ...

    def getClass(self) -> java.lang.Class: ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address: ...

    def getMinAddress(self) -> ghidra.program.model.address.Address: ...

    def getPcodeOp(self) -> ghidra.program.model.pcode.PcodeOp: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def numChildren(self) -> int: ...

    def restoreFromXML(self, parser: ghidra.xml.XmlPullParser, pfactory: ghidra.program.model.pcode.PcodeFactory) -> None: ...

    def setHighlight(self, val: java.awt.Color) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def pcodeOp(self) -> ghidra.program.model.pcode.PcodeOp: ...
