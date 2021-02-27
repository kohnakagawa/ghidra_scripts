from typing import List
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.symbol
import java.lang


class CodeUnitInfo(object):
    """
    Container object to keep a relative index, label, and comments. Used
     in a list for copying/pasting labels and comments from one program to
     another.
    """





    def __init__(self, index: int):
        """
        Constructor a new CodeUnitInfo.
        @param index relative index added to a base address
         for where this information will be placed
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEOLComment(self) -> List[unicode]:
        """
        Get the EOL comment.
        """
        ...

    def getFunctionComments(self) -> List[unicode]:
        """
        Get the function comments.
        """
        ...

    def getFunctionName(self) -> unicode:
        """
        Get the function name.
        """
        ...

    def getFunctionScopeSymbolNames(self) -> List[unicode]:
        """
        Get the names of the function scope symbols.
        """
        ...

    def getFunctionScopeSymbolSources(self) -> List[ghidra.program.model.symbol.SourceType]:
        """
        Get the sources of the function scope symbols.
        """
        ...

    def getIndex(self) -> int:
        """
        Get the relative index for this CodeUnitInfo to add to a base address.
        """
        ...

    def getOtherSymbolNames(self) -> List[unicode]:
        """
        Get the names of the other symbols not in a function scope.
        """
        ...

    def getOtherSymbolSources(self) -> List[ghidra.program.model.symbol.SourceType]:
        """
        Get the sources of the other symbols not in a function scope.
        """
        ...

    def getPlateComment(self) -> List[unicode]:
        """
        Get the plate comment.
        """
        ...

    def getPostComment(self) -> List[unicode]:
        """
        Get the post comment.
        """
        ...

    def getPreComment(self) -> List[unicode]:
        """
        Get the pre comment.
        """
        ...

    def getPrimarySymbolName(self) -> unicode:
        """
        Get the label; may be null.
        """
        ...

    def getPrimarySymbolSource(self) -> ghidra.program.model.symbol.SourceType:
        """
        Get the label source
        """
        ...

    def getRepeatableComment(self) -> List[unicode]:
        """
        Get the repeatable comment.
        """
        ...

    def getStackOffsets(self) -> List[int]:
        """
        Get the stack offsets.
        """
        ...

    def getStackVarFirstUseOffsets(self) -> List[int]:
        """
        Get the stack variable "First Use Offsets"
        """
        ...

    def getStackVariableComments(self) -> List[unicode]:
        """
        Get the stack variable comments.
        """
        ...

    def getStackVariableNames(self) -> List[unicode]:
        """
        Get the stack variable names.
        """
        ...

    def getStackVariableSources(self) -> List[ghidra.program.model.symbol.SourceType]:
        """
        Get the stack variable sources.
        """
        ...

    def getVarAddresses(self) -> List[ghidra.program.model.address.Address]:
        """
        Get the storage addresses corresponding to each non-stack variable.
        """
        ...

    def getVarFirstUseOffsets(self) -> List[int]:
        """
        Get the non-stack variable "First Use Offsets"
        """
        ...

    def getVariableComments(self) -> List[unicode]:
        """
        Get the non-stack variable comments.
        """
        ...

    def getVariableNames(self) -> List[unicode]:
        """
        Get the non-stack variable names.
        """
        ...

    def getVariableSources(self) -> List[ghidra.program.model.symbol.SourceType]:
        """
        Get the non-stack variable sources.
        """
        ...

    def hasDynamicSymbol(self) -> bool:
        """
        Return whether this CodeUnitInfo has a dynamic symbol.
        """
        ...

    def hasSymbols(self) -> bool:
        """
        Return whether this CodeUnitInfo has symbols to copy.
        """
        ...

    def hashCode(self) -> int: ...

    def isPrimarySymbolInFunctionScope(self) -> bool:
        """
        Is primary symbol in a function scope
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setComment(self, commentType: int, comment: List[unicode]) -> None:
        """
        Set the comment to be transferred.
        @param commentType CodeUnit.PRE_COMMENT, POST_COMMENT,
         PLATE_COMMENT, EOL_COMMENT, or REPEATABLE.
        @param comment comment
        """
        ...

    def setFunction(self, function: ghidra.program.model.listing.Function) -> None:
        """
        Set the function info.
        @param function function used to get function info to transfer
        """
        ...

    def setSymbols(self, symbols: List[ghidra.program.model.symbol.Symbol]) -> None:
        """
        Set the symbols to be transferred.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def EOLComment(self) -> List[unicode]: ...

    @property
    def function(self) -> None: ...  # No getter available.

    @function.setter
    def function(self, value: ghidra.program.model.listing.Function) -> None: ...

    @property
    def functionComments(self) -> List[unicode]: ...

    @property
    def functionName(self) -> unicode: ...

    @property
    def functionScopeSymbolNames(self) -> List[unicode]: ...

    @property
    def functionScopeSymbolSources(self) -> List[ghidra.program.model.symbol.SourceType]: ...

    @property
    def index(self) -> int: ...

    @property
    def otherSymbolNames(self) -> List[unicode]: ...

    @property
    def otherSymbolSources(self) -> List[ghidra.program.model.symbol.SourceType]: ...

    @property
    def plateComment(self) -> List[unicode]: ...

    @property
    def postComment(self) -> List[unicode]: ...

    @property
    def preComment(self) -> List[unicode]: ...

    @property
    def primarySymbolInFunctionScope(self) -> bool: ...

    @property
    def primarySymbolName(self) -> unicode: ...

    @property
    def primarySymbolSource(self) -> ghidra.program.model.symbol.SourceType: ...

    @property
    def repeatableComment(self) -> List[unicode]: ...

    @property
    def stackOffsets(self) -> List[int]: ...

    @property
    def stackVarFirstUseOffsets(self) -> List[int]: ...

    @property
    def stackVariableComments(self) -> List[unicode]: ...

    @property
    def stackVariableNames(self) -> List[unicode]: ...

    @property
    def stackVariableSources(self) -> List[ghidra.program.model.symbol.SourceType]: ...

    @property
    def symbols(self) -> None: ...  # No getter available.

    @symbols.setter
    def symbols(self, value: List[ghidra.program.model.symbol.Symbol]) -> None: ...

    @property
    def varAddresses(self) -> List[ghidra.program.model.address.Address]: ...

    @property
    def varFirstUseOffsets(self) -> List[int]: ...

    @property
    def variableComments(self) -> List[unicode]: ...

    @property
    def variableNames(self) -> List[unicode]: ...

    @property
    def variableSources(self) -> List[ghidra.program.model.symbol.SourceType]: ...
