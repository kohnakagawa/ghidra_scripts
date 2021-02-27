from typing import List
import ghidra.program.model.data
import ghidra.program.model.listing
import java.lang


class FunctionSignature(object):
    """
    Interface describing all the things about a function that are portable
     from one program to another.
    """

    VAR_ARGS_DISPLAY_STRING: unicode = u'...'
    VOID_PARAM_DISPLAY_STRING: unicode = u'void'







    def equals(self, __a0: object) -> bool: ...

    def getArguments(self) -> List[ghidra.program.model.data.ParameterDefinition]:
        """
        Return an array of parameters for the function
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self) -> unicode:
        """
        Return the comment string
        """
        ...

    def getGenericCallingConvention(self) -> ghidra.program.model.data.GenericCallingConvention:
        """
        Returns the generic calling convention associated with this function definition.
         The "unknown" convention should be returned instead of null.
        """
        ...

    def getName(self) -> unicode:
        """
        Return the name of this function
        """
        ...

    @overload
    def getPrototypeString(self) -> unicode:
        """
        Return a string representation of the function signature without the
         calling convention specified.
        """
        ...

    @overload
    def getPrototypeString(self, includeCallingConvention: bool) -> unicode:
        """
        Return a string representation of the function signature
        @param includeCallingConvention if true prototype will include call convention
         declaration if known.
        """
        ...

    def getReturnType(self) -> ghidra.program.model.data.DataType:
        """
        Return the return data type
        """
        ...

    def hasVarArgs(self) -> bool:
        """
        Returns true if this function signature has a variable argument list (VarArgs).
        """
        ...

    def hashCode(self) -> int: ...

    def isEquivalentSignature(self, signature: ghidra.program.model.listing.FunctionSignature) -> bool:
        """
        Returns true if the given signature is equivalent to this signature.  The
         precise meaning of "equivalent" is dependent upon return/parameter dataTypes.
        @param signature the function signature being tested for equivalence.
        @return true if the if the given signature is equivalent to this signature.
        """
        ...

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
    def arguments(self) -> List[ghidra.program.model.data.ParameterDefinition]: ...

    @property
    def comment(self) -> unicode: ...

    @property
    def genericCallingConvention(self) -> ghidra.program.model.data.GenericCallingConvention: ...

    @property
    def name(self) -> unicode: ...

    @property
    def prototypeString(self) -> unicode: ...

    @property
    def returnType(self) -> ghidra.program.model.data.DataType: ...
