from typing import List
import ghidra.app.plugin.assembler.sleigh.parse
import ghidra.app.plugin.assembler.sleigh.sem
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.listing
import java.lang
import java.util


class Assembler(object):
    """
    The primary interface for performing assembly in Ghidra.

     Use the Assemblers class to obtain a suitable implementation for a given program or
     language.
    """









    def assemble(self, at: ghidra.program.model.address.Address, listing: List[unicode]) -> ghidra.program.model.lang.InstructionBlock:
        """
        Assemble a sequence of instructions and place them at the given address.

         This method is only valid if the assembler is bound to a program. An instance may optionally
         implement this method without a program binding. In that case, the returned instruction
         block will refer to pseudo instructions.

         NOTE: There must be an active transaction on the bound program for this method to succeed.
        @param at the location where the resulting instructions should be placed
        @param listing a new-line separated or array sequence of instructions
        @return the block of resulting instructions
        @throws AssemblySyntaxException a textual instruction is non well-formed
        @throws AssemblySemanticException a well-formed instruction cannot be assembled
        @throws MemoryAccessException there is an issue writing the result to program memory
        @throws AddressOverflowException the resulting block is beyond the valid address range
        """
        ...

    @overload
    def assembleLine(self, at: ghidra.program.model.address.Address, line: unicode) -> List[int]:
        """
        Assemble a line instruction at the given address.

         This method is valid with or without a bound program. Even if bound, the program is not
         modified; however, the appropriate context information is taken from the bound program.
         Without a program, the language's default context is taken at the given location.
        @param at the location of the start of the instruction
        @param line the textual assembly code
        @return the binary machine code, suitable for placement at the given address
        @throws AssemblySyntaxException the textual instruction is not well-formed
        @throws AssemblySemanticException the the well-formed instruction cannot be assembled
        """
        ...

    @overload
    def assembleLine(self, at: ghidra.program.model.address.Address, line: unicode, ctx: ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock) -> List[int]:
        """
        Assemble a line instruction at the given address, assuming the given context.

         This method works like {@link #assembleLine(Address, String)} except that it allows you to
         override the assumed context at that location.
        @param at the location of the start of the instruction
        @param line the textual assembly code
        @param ctx the context register value at the start of the instruction
        @return the results of semantic resolution (from all parse results)
        @throws AssemblySyntaxException the textual instruction is not well-formed
        @throws AssemblySemanticException the well-formed instruction cannot be assembled
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getContextAt(self, addr: ghidra.program.model.address.Address) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock:
        """
        Get the context at a given address

         If there is a program binding, this will extract the actual context at the given address.
         Otherwise, it will obtain the default context at the given address for the language.
        @param addr the address
        @return the context
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def parseLine(self, line: unicode) -> java.util.Collection:
        """
        Parse a line instruction.

         Generally, you should just use {@link #assembleLine(Address, String)}, but if you'd like
         access to the parse trees outside of an {@link AssemblySelector}, then this may be an
         acceptable option. Most notably, this is an excellent way to obtain suggestions for
         auto-completion.

         Each item in the returned collection is either a complete parse tree, or a syntax error
         Because all parse paths are attempted, it's possible to get many mixed results. For example,
         The input line may be a valid instruction; however, there may be suggestions to continue the
         line toward another valid instruction.
        @param line the line (or partial line) to parse
        @return the results of parsing
        """
        ...

    @overload
    def patchProgram(self, insbytes: List[int], at: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Instruction:
        """
        Place an instruction into the bound program.

         This method is not valid without a program binding. Also, this method must be called during
         a program database transaction.
        @param insbytes the instruction data
        @param at the location of the start of the instruction
        @return the new {@link Instruction} code unit
        @throws MemoryAccessException there is an issue writing the result to program memory
        """
        ...

    @overload
    def patchProgram(self, res: ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolvedConstructor, at: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Instruction:
        """
        Place a resolved (and fully-masked) instruction into the bound program.

         This method is not valid without a program binding. Also, this method must be called during
         a program database transaction.
        @param res the resolved and fully-masked instruction
        @param at the location of the start of the instruction
        @return the new {@link Instruction} code unit
        @throws MemoryAccessException there is an issue writing the result to program memory
        """
        ...

    @overload
    def resolveLine(self, at: ghidra.program.model.address.Address, line: unicode) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolutionResults:
        """
        Assemble a line instruction at the given address.

         This method works like {@link #resolveLine(Address, String, AssemblyPatternBlock)}, except
         that it derives the context using {@link #getContextAt(Address)}.
        @param at the location of the start of the instruction
        @param line the textual assembly code
        @return the collection of semantic resolution results
        @throws AssemblySyntaxException the textual instruction is not well-formed
        """
        ...

    @overload
    def resolveLine(self, at: ghidra.program.model.address.Address, line: unicode, ctx: ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolutionResults:
        """
        Assemble a line instruction at the given address, assuming the given context.

         This method works like {@link #assembleLine(Address, String, AssemblyPatternBlock)}, except
         that it returns all possible resolutions for the parse trees that pass the
         {@link AssemblySelector}.
        @param at the location of the start of the instruction
        @param line the textual assembly code
        @param ctx the context register value at the start of the instruction
        @return the collection of semantic resolution results
        @throws AssemblySyntaxException the textual instruction is not well-formed
        """
        ...

    @overload
    def resolveTree(self, parse: ghidra.app.plugin.assembler.sleigh.parse.AssemblyParseResult, at: ghidra.program.model.address.Address) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolutionResults:
        """
        Resolve a given parse tree at the given address.

         Each item in the returned collection is either a completely resolved instruction, or a
         semantic error. Because all resolutions are attempted, it's possible to get many mixed
         results.

         NOTE: The resolved instructions are given as masks and values. Where the mask does not
         cover, you can choose any value.
        @param parse a parse result giving a valid tree
        @param at the location of the start of the instruction
        @return the results of semantic resolution
        """
        ...

    @overload
    def resolveTree(self, parse: ghidra.app.plugin.assembler.sleigh.parse.AssemblyParseResult, at: ghidra.program.model.address.Address, ctx: ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolutionResults:
        """
        Resolve a given parse tree at the given address, assuming the given context

         Each item in the returned collection is either a completely resolved instruction, or a
         semantic error. Because all resolutions are attempted, it's possible to get many mixed
         results.

         NOTE: The resolved instructions are given as masks and values. Where the mask does not
         cover, you can choose any value.
        @param parse a parse result giving a valid tree
        @param at the location of the start of the instruction
        @param ctx the context register value at the start of the instruction
        @return the results of semantic resolution
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
