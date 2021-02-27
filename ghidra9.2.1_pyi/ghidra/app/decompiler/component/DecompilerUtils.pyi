from typing import List
import docking.widgets.fieldpanel.field
import docking.widgets.fieldpanel.support
import ghidra.app.decompiler
import ghidra.app.plugin.core.decompile
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.program.model.pcode
import java.lang
import java.util


class DecompilerUtils(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def findAddressBefore(lines: List[docking.widgets.fieldpanel.field.Field], token: ghidra.app.decompiler.ClangToken) -> ghidra.program.model.address.Address: ...

    @staticmethod
    def findClosestAddressSet(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.AddressSpace, __a2: List[object]) -> ghidra.program.model.address.AddressSet: ...

    @staticmethod
    def findIndexOfFirstField(__a0: List[object], __a1: List[docking.widgets.fieldpanel.field.Field]) -> int: ...

    @staticmethod
    def getBackwardSlice(seed: ghidra.program.model.pcode.Varnode) -> java.util.Set: ...

    @staticmethod
    def getBackwardSliceToPCodeOps(seed: ghidra.program.model.pcode.Varnode) -> java.util.Set: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getClosestAddress(program: ghidra.program.model.listing.Program, token: ghidra.app.decompiler.ClangToken) -> ghidra.program.model.address.Address: ...

    @staticmethod
    def getDataType(context: ghidra.app.plugin.core.decompile.DecompilerActionContext) -> ghidra.program.model.data.DataType:
        """
        Returns the data type for the given context if the context pertains to a data type
        @param context the context
        @return the data type or null
        """
        ...

    @staticmethod
    def getFieldSelection(__a0: List[object]) -> docking.widgets.fieldpanel.support.FieldSelection: ...

    @staticmethod
    def getForwardSlice(seed: ghidra.program.model.pcode.Varnode) -> java.util.Set:
        """
        Construct the set of varnodes making up a simple forward slice of seed
        @param seed Varnode where the slice starts
        @return set of Varnodes in the slice
        """
        ...

    @staticmethod
    def getForwardSliceToPCodeOps(seed: ghidra.program.model.pcode.Varnode) -> java.util.Set: ...

    @staticmethod
    def getFunction(program: ghidra.program.model.listing.Program, token: ghidra.app.decompiler.ClangFuncNameToken) -> ghidra.program.model.listing.Function:
        """
        Returns the function represented by the given token.  This will be either the
         decompiled function or a function referenced within the decompiled function.
        @param program the program
        @param token the token
        @return the function
        """
        ...

    @staticmethod
    def getGoToTargetToken(root: ghidra.app.decompiler.ClangTokenGroup, label: ghidra.app.decompiler.ClangLabelToken) -> ghidra.app.decompiler.ClangLabelToken: ...

    @staticmethod
    def getMatchingBrace(startToken: ghidra.app.decompiler.ClangSyntaxToken) -> ghidra.app.decompiler.ClangSyntaxToken: ...

    @overload
    @staticmethod
    def getTokens(root: ghidra.app.decompiler.ClangNode, address: ghidra.program.model.address.Address) -> List[ghidra.app.decompiler.ClangToken]: ...

    @overload
    @staticmethod
    def getTokens(root: ghidra.app.decompiler.ClangNode, addressSet: ghidra.program.model.address.AddressSetView) -> List[ghidra.app.decompiler.ClangToken]:
        """
        Find all ClangNodes that have a minimum address in the AddressSetView
        @param root the root of the token tree
        @param addressSet the addresses to restrict
        @return the list of tokens
        """
        ...

    @staticmethod
    def getTokensFromView(fields: List[docking.widgets.fieldpanel.field.Field], address: ghidra.program.model.address.Address) -> List[ghidra.app.decompiler.ClangToken]:
        """
        Similar to {@link #getTokens(ClangNode, AddressSetView)}, but uses the tokens from
         the given view fields.  Sometimes the tokens in the model (represented by the
         {@link ClangNode}) are different than the fields in the view (such as when a list of
         comment tokens are condensed into a single comment token).
        @param fields the fields to check
        @param address the address each returned token must match
        @return the matching tokens
        """
        ...

    @staticmethod
    def getTokensInSelection(selection: docking.widgets.fieldpanel.support.FieldSelection, lines: List[docking.widgets.fieldpanel.field.Field]) -> List[ghidra.app.decompiler.ClangToken]: ...

    @staticmethod
    def getVarnodeRef(token: ghidra.app.decompiler.ClangToken) -> ghidra.program.model.pcode.Varnode:
        """
        If the token refers to an individual Varnode, return it. Otherwise return null
        @param token the token to check
        @return the Varnode or null otherwise
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isBrace(token: ghidra.app.decompiler.ClangSyntaxToken) -> bool: ...

    @staticmethod
    def isGoToStatement(token: ghidra.app.decompiler.ClangToken) -> bool: ...

    @staticmethod
    def isMatchingBrace(braceToken: ghidra.app.decompiler.ClangSyntaxToken, otherBraceToken: ghidra.app.decompiler.ClangSyntaxToken) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def toLines(group: ghidra.app.decompiler.ClangTokenGroup) -> List[ghidra.app.decompiler.ClangLine]: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
