from typing import List
import ghidra.app.decompiler
import java.lang


class ClangLine(object):
    """
    A line of C code. This is an independent grouping
     of C tokens from the statement, vardecl retype groups
    """





    def __init__(self, lineNumber: int, indent: int): ...



    def addToken(self, tok: ghidra.app.decompiler.ClangToken) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getAllTokens(self) -> List[ghidra.app.decompiler.ClangToken]: ...

    def getClass(self) -> java.lang.Class: ...

    def getIndent(self) -> int: ...

    def getIndentString(self) -> unicode: ...

    def getLineNumber(self) -> int: ...

    def getNumTokens(self) -> int: ...

    def getToken(self, i: int) -> ghidra.app.decompiler.ClangToken: ...

    def hashCode(self) -> int: ...

    def indexOfToken(self, token: ghidra.app.decompiler.ClangToken) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def toDebugString(self, __a0: List[object]) -> unicode: ...

    @overload
    def toDebugString(self, __a0: List[object], __a1: unicode, __a2: unicode) -> unicode: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def allTokens(self) -> java.util.ArrayList: ...

    @property
    def indent(self) -> int: ...

    @property
    def indentString(self) -> unicode: ...

    @property
    def lineNumber(self) -> int: ...

    @property
    def numTokens(self) -> int: ...
