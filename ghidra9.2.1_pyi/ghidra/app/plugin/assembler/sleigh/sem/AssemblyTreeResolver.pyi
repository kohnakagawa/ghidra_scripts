import ghidra.app.plugin.assembler.sleigh.sem
import ghidra.app.plugin.processors.sleigh
import ghidra.app.plugin.processors.sleigh.symbol
import java.lang
import java.util


class AssemblyTreeResolver(object):
    """
    The workhorse of semantic resolution for the assembler

     This class takes a parse tree and some additional information (start address, context, etc.) and
     attempts to determine possible encodings using the semantics associated with each branch of the
     given parse tree. Details of this process are described in SleighAssemblerBuilder.
    """

    INST_NEXT: unicode = u'inst_next'
    INST_START: unicode = u'inst_start'



    def __init__(self, lang: ghidra.app.plugin.processors.sleigh.SleighLanguage, instStart: long, tree: ghidra.app.plugin.assembler.sleigh.tree.AssemblyParseBranch, context: ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock, ctxGraph: ghidra.app.plugin.assembler.sleigh.sem.AssemblyContextGraph):
        """
        Construct a resolver for the given parse tree
        @param lang
        @param instStart the byte offset where the instruction will start
        @param tree the parse tree
        @param context the context expected at {@code instStart}
        @param ctxGraph the context transition graph used to resolve purely-recursive productions
        """
        ...



    @staticmethod
    def computeOffset(opsym: ghidra.app.plugin.processors.sleigh.symbol.OperandSymbol, cons: ghidra.app.plugin.processors.sleigh.Constructor, res: java.util.Map) -> int:
        """
        Compute the offset of an operand encoded in the instruction block
        @param opsym the operand symbol
        @param cons the constructor containing the operand
        @param res the selected subconstructor encodings
        @return the offset (right shift) to apply to the encoded operand
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def resolve(self) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolutionResults:
        """
        Resolve the tree for the given parameters
        @return a set of resolutions (encodings and errors)
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
