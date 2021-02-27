from typing import List
import ghidra.app.plugin.assembler.sleigh.expr
import ghidra.app.plugin.assembler.sleigh.sem
import ghidra.app.plugin.processors.sleigh.expression
import ghidra.app.plugin.processors.sleigh.pattern
import java.lang
import java.util


class AssemblyResolvedError(ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolution):
    """
    A AssemblyResolution indicating the occurrence of a (usually semantic) error

     The description should indicate where the error occurred. The error message should explain the
     actual error. To help the user diagnose the nature of the error, errors in sub-constructors
     should be placed as children of an error given by the parent constructor.
    """









    @staticmethod
    def backfill(exp: ghidra.app.plugin.processors.sleigh.expression.PatternExpression, goal: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong, res: java.util.Map, inslen: int, description: unicode) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolvedBackfill:
        """
        Build a backfill record to attach to a successful resolution result
        @param exp the expression depending on a missing symbol
        @param goal the desired value of the expression
        @param res the resolution result for child constructors
        @param inslen the length of instruction portion expected in the future solution
        @param description a description of the backfill record
        @return the new record
        """
        ...

    @overload
    def compareTo(self, that: ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolution) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    @staticmethod
    def contextOnly(__a0: ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock, __a1: unicode, __a2: List[object]) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolvedConstructor: ...

    def equals(self, obj: object) -> bool: ...

    @overload
    @staticmethod
    def error(error: unicode, res: ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolvedConstructor) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolution:
        """
        Build an error resolution record, based on an intermediate SLEIGH constructor record
        @param error a description of the error
        @param res the constructor record that was being populated when the error ocurred
        @return the new error resolution
        """
        ...

    @overload
    @staticmethod
    def error(__a0: unicode, __a1: unicode, __a2: List[object]) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolvedError: ...

    @staticmethod
    def fromPattern(pat: ghidra.app.plugin.processors.sleigh.pattern.DisjointPattern, minLen: int, description: unicode) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolvedConstructor:
        """
        Build a successful resolution result from a SLEIGH constructor's patterns
        @param pat the constructor's pattern
        @param description a description of the resolution
        @return the new resolution
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getError(self) -> unicode:
        """
        Get a description of the error
        @return the description
        """
        ...

    def hasChildren(self) -> bool:
        """
        Check if this record has children

         If a subclass has another, possibly additional, notion of children that it would like to
         include in {@link #toString()}, it must override this method to return true when such
         children are present.
        @see #childrenToString(String)
        @return true if this record has children
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def instrOnly(__a0: ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock, __a1: unicode, __a2: List[object]) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolvedConstructor: ...

    def isBackfill(self) -> bool: ...

    def isError(self) -> bool: ...

    def lineToString(self) -> unicode: ...

    @staticmethod
    def nop(__a0: unicode, __a1: List[object]) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolvedConstructor: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def resolved(__a0: ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock, __a1: ghidra.app.plugin.assembler.sleigh.sem.AssemblyPatternBlock, __a2: unicode, __a3: List[object]) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolvedConstructor: ...

    @overload
    def toString(self) -> unicode:
        """
        Describe this record including indented children, grandchildren, etc., each on its own line
        """
        ...

    @overload
    def toString(self, indent: unicode) -> unicode:
        """
        Used only by parents: get a multi-line description of this record, indented
        @param indent the current indentation
        @return the indented description
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
