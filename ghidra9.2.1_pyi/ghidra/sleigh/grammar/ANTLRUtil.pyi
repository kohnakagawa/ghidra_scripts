import ghidra.sleigh.grammar
import java.io
import java.lang
import org.antlr.runtime
import org.antlr.runtime.tree


class ANTLRUtil(object):




    def __init__(self): ...



    @staticmethod
    def debugNodeStream(nodes: org.antlr.runtime.tree.BufferedTreeNodeStream, out: java.io.PrintStream) -> None: ...

    @staticmethod
    def debugTokenStream(tokens: org.antlr.runtime.CommonTokenStream, out: java.io.PrintStream) -> None: ...

    @staticmethod
    def debugTree(tree: org.antlr.runtime.tree.Tree, out: java.io.PrintStream) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def generateArrow(charPositionInLine: int) -> unicode: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    @staticmethod
    def getLine(writer: ghidra.sleigh.grammar.LineArrayListWriter, lineno: int) -> unicode: ...

    @overload
    @staticmethod
    def getLine(reader: java.io.Reader, lineno: int) -> unicode: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def tabCompensate(line: unicode, charPositionInLine: int) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
