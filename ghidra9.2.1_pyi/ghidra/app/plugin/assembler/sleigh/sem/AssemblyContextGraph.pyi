import ghidra.app.plugin.assembler.sleigh.sem
import ghidra.app.plugin.assembler.sleigh.sem.AssemblyContextGraph
import ghidra.graph
import java.lang
import java.util


class AssemblyContextGraph(object, ghidra.graph.GImplicitDirectedGraph):
    """
    A graph of possible context changes via the application of various constructors

     This is used primarily to find optimal paths for the application of recursive rules, i.e., those
     of the form I = I. These cannot be resolved without some form of semantic analysis. The most
     notable disadvantage to all of this is that you no longer get all of the possible assemblies,
     but only those with the fewest rule applications.

     Conceivably, this may also be used to prune some possibilities during semantic resolution of a
     parse tree. Even better, it may be possible to derive a grammar which accounts for the context
     changes already; however, it's unclear how many rules this will generate, and consequently, how
     much larger its LALR(1) parser would become.
    """





    def __init__(self, lang: ghidra.app.plugin.processors.sleigh.SleighLanguage, grammar: ghidra.app.plugin.assembler.sleigh.grammars.AssemblyGrammar):
        """
        Build the context change graph for a given language and grammar

         The grammar must have been constructed from the given language. The language is used just to
         obtain the most common default context.

         At the moment, this graph only expands the recursive rules at the root constructor table,
         i.e., "instruction". Thus, the assembler will not be able to process any language that has
         <i>purely</i>-recursive rules at subconstructors.
        @param lang the language
        @param grammar the grammar derived from the given language
        """
        ...



    def computeOptimalApplications(self, src: ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock, srcTable: unicode, dst: ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock, dstTable: unicode) -> java.util.Collection:
        """
        Compute the optimal, i.e., fewest, sequences of applications to resolve a given context to
         the language's default context.
        @param src presumably, the language's default context
        @param srcTable the name of the SLEIGH constructor table, presumably "instruction"
        @param dst the context block being resolved
        @param dstTable the name of the SLEIGH constructor table being resolved
        @return a collection of sequences of constructor applications from {@code src} to
                 {@code dst}

         NOTE: For assembly, the sequences will need to be applied right-to-left.
        """
        ...

    def copy(self) -> ghidra.graph.GDirectedGraph:
        """
        Returns a copy of the graph explored so far
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getInEdges(self, v: ghidra.app.plugin.assembler.sleigh.sem.AssemblyContextGraph.Vertex) -> java.util.Collection:
        """
        This operation is not supported.

         I could implement this using the cached edges, but that may not be semantically, what a path
         computation algorithm actually requires. Instead, I will assume the algorithm only explores
         the graph in the same direction as its edges. If not, I will hear about it quickly.
        """
        ...

    @overload
    def getInEdges(self, __a0: object) -> java.util.Collection: ...

    @overload
    def getOutEdges(self, v: ghidra.app.plugin.assembler.sleigh.sem.AssemblyContextGraph.Vertex) -> java.util.Collection: ...

    @overload
    def getOutEdges(self, __a0: object) -> java.util.Collection: ...

    def getPredecessors(self, __a0: object) -> java.util.Collection: ...

    def getSuccessors(self, __a0: object) -> java.util.Collection: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
