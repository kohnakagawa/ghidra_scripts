import ghidra.app.plugin.assembler
import ghidra.app.plugin.assembler.sleigh
import ghidra.app.plugin.processors.sleigh
import ghidra.program.model.lang
import ghidra.program.model.listing
import java.lang


class SleighAssemblerBuilder(object, ghidra.app.plugin.assembler.AssemblerBuilder):
    """
    An AssemblerBuilder capable of supporting almost any SleighLanguage

     To build an assembler, please use a static method of the Assemblers class.

     SLEIGH-based assembly is a bit of an experimental feature at this time. Nevertheless, it seems to
     have come along quite nicely. It's not quite as fast as disassembly, since after all, that's what
     SLEIGH was designed to do.

     Overall, the method is fairly simple, though its implementation is a bit more complex. First, we
     gather every pair of pattern and constructor by traversing the decision tree used by disassembly.
     We then use the "print pieces" to construct a context-free grammar. Each production is associated
     with the one-or-more constructors with the same sequence of print pieces. We then build a LALR(1)
     parser for the generated grammar. This now constitutes a generic parser for the given language.
     Note that this step takes some time, and may be better suited as a build-time step. Because
     SLEIGH specifications are not generally concerned with eliminating ambiguity of printed
     instructions (rather, it only does so for instruction bytes), we must consider that the grammar
     could be ambiguous. To handle this, the action/goto table is permitted multiple entries per cell,
     and we allow backtracking. There are also cases where tokens are not actually separated by
     spaces. For example, in the  file, there is JMP ... and J^cc, meaning, the lexer
     must consider J as a token as well as JMP, introducing another source of possible backtracking.
     Despite that, parsing is completed fairly quickly.

     To assemble, we first parse the textual instruction, yielding zero or more parse trees. No parse
     trees implies an error. For each parse tree, we attempt to resolve the instruction bytes,
     starting at the leaves and working upwards while tracking and solving context changes. The
     context changes must be considered in reverse. We read the context register of the
     children (a disassembler would write). We then assume there is at most one variable in the
     expression, solve for it, and write the solution to the appropriate field (a
     disassembler would read). If no solution exists, a semantic error is logged. Since it's possible
     a production in the parse tree is associated with multiple constructors, different combinations
     of constructors are explored as we move upward in the tree. If all possible combinations yield
     semantic errors, then the overall result is an error.

     Some productions are "purely recursive," e.g.,  lines in the SLEIGH. These
     are ignored during parser construction. Let such a production be given as I = I. When resolving
     the parse tree to bytes, and we encounter a production with I on the left hand side, we then
     consider the possible application of the production I = I and its consequential constructors.
     Ideally, we could repeat this indefinitely, stopping when all further applications result in
     semantic errors; however, there is no guarantee in the SLEIGH specification that such an
     algorithm will actually halt, so a maximum number (default of 1) of applications are attempted.

     After all the context changes and operands are resolved, we apply the constructor patterns and
     proceed up the tree. Thus, each branch yields zero or more "resolved constructors," which each
     specify two masked blocks of data: one for the instruction, and one for the context. These are
     passed up to the parent production, which, having obtained results from all its children,
     attempts to apply the corresponding constructors.

     Once we've resolved the root node, any resolved constructors returned are taken as successfully
     assembled instruction bytes. If applicable, the corresponding context registers are compared to
     the context at the target address in the program and filtered for compatibility.
    """





    def __init__(self, lang: ghidra.app.plugin.processors.sleigh.SleighLanguage):
        """
        Construct an assembler builder for the given SLEIGH language
        @param lang the language
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    @overload
    def getAssembler(self, selector: ghidra.app.plugin.assembler.AssemblySelector) -> ghidra.app.plugin.assembler.sleigh.SleighAssembler: ...

    @overload
    def getAssembler(self, selector: ghidra.app.plugin.assembler.AssemblySelector, program: ghidra.program.model.listing.Program) -> ghidra.app.plugin.assembler.sleigh.SleighAssembler: ...

    def getClass(self) -> java.lang.Class: ...

    def getLanguage(self) -> ghidra.app.plugin.processors.sleigh.SleighLanguage: ...

    def getLanguageID(self) -> ghidra.program.model.lang.LanguageID: ...

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

    @property
    def language(self) -> ghidra.app.plugin.processors.sleigh.SleighLanguage: ...

    @property
    def languageID(self) -> ghidra.program.model.lang.LanguageID: ...
