import generic.stl
import ghidra.pcodeCPort.context
import ghidra.pcodeCPort.semantics
import ghidra.pcodeCPort.translate
import java.io
import java.lang
import org.jdom


class VarnodeTpl(object):
    location: ghidra.sleigh.grammar.Location



    @overload
    def __init__(self, __a0: ghidra.sleigh.grammar.Location): ...

    @overload
    def __init__(self, __a0: ghidra.sleigh.grammar.Location, __a1: ghidra.pcodeCPort.semantics.VarnodeTpl): ...

    @overload
    def __init__(self, __a0: ghidra.sleigh.grammar.Location, __a1: int, __a2: bool): ...

    @overload
    def __init__(self, __a0: ghidra.sleigh.grammar.Location, __a1: ghidra.pcodeCPort.semantics.ConstTpl, __a2: ghidra.pcodeCPort.semantics.ConstTpl, __a3: ghidra.pcodeCPort.semantics.ConstTpl): ...



    def adjustTruncation(self, __a0: int, __a1: bool) -> bool: ...

    def changeHandleIndex(self, __a0: generic.stl.VectorSTL) -> None: ...

    def compareTo(self, __a0: ghidra.pcodeCPort.semantics.VarnodeTpl) -> int: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getOffset(self) -> ghidra.pcodeCPort.semantics.ConstTpl: ...

    def getSize(self) -> ghidra.pcodeCPort.semantics.ConstTpl: ...

    def getSpace(self) -> ghidra.pcodeCPort.semantics.ConstTpl: ...

    def hashCode(self) -> int: ...

    def isDynamic(self, __a0: ghidra.pcodeCPort.context.ParserWalker) -> bool: ...

    def isLocalTemp(self) -> bool: ...

    def isRelative(self) -> bool: ...

    def isUnnamed(self) -> bool: ...

    def isZeroSize(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreXml(self, __a0: org.jdom.Element, __a1: ghidra.pcodeCPort.translate.Translate) -> None: ...

    def saveXml(self, __a0: java.io.PrintStream) -> None: ...

    def setOffset(self, __a0: long) -> None: ...

    def setRelative(self, __a0: long) -> None: ...

    def setSize(self, __a0: ghidra.pcodeCPort.semantics.ConstTpl) -> None: ...

    def setUnnamed(self, __a0: bool) -> None: ...

    def toString(self) -> unicode: ...

    def transfer(self, __a0: generic.stl.VectorSTL) -> int: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def localTemp(self) -> bool: ...

    @property
    def offset(self) -> ghidra.pcodeCPort.semantics.ConstTpl: ...

    @property
    def relative(self) -> bool: ...

    @property
    def size(self) -> ghidra.pcodeCPort.semantics.ConstTpl: ...

    @size.setter
    def size(self, value: ghidra.pcodeCPort.semantics.ConstTpl) -> None: ...

    @property
    def space(self) -> ghidra.pcodeCPort.semantics.ConstTpl: ...

    @property
    def unnamed(self) -> bool: ...

    @unnamed.setter
    def unnamed(self, value: bool) -> None: ...

    @property
    def zeroSize(self) -> bool: ...
