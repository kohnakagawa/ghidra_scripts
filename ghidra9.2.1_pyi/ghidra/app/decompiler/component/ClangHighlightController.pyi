import docking.widgets
import docking.widgets.fieldpanel.field
import docking.widgets.fieldpanel.support
import ghidra.app.decompiler
import ghidra.app.decompiler.component
import ghidra.app.plugin.core.decompile.actions
import ghidra.program.model.listing
import java.awt
import java.lang
import java.util
import java.util.function


class ClangHighlightController(object):
    """
    Class to handle highlights for a decompiled function.

     This class does not painting directly.  Rather, this class tracks the currently highlighted
     tokens and then sets the highlight color on the token when it is highlighted and clears the
     highlight color when the highlight is removed.

     This class maintains the notion of 'primary' highlights and 'secondary' highlights.
     Primary highlights are considered transient and get cleared whenever the location changes.
     Secondary highlights will stay until they are manually cleared by a user action.  Primary
     highlights happen when the user clicks around the Decompiler.  They show state such as the
     current field, impact of a variable (via a slicing action), or related syntax (such as
     matching braces).  Secondary highlights are triggered by the user to show all occurrences of
     a particular variable.  Further,  the user can apply multiple secondary highlights at the
     same time, with different colors for each highlight.
    """

    DEFAULT_HIGHLIGHT_COLOR: java.awt.Color



    def __init__(self): ...



    def addHighlightBrace(self, token: ghidra.app.decompiler.ClangSyntaxToken, highlightColor: java.awt.Color) -> None: ...

    def addListener(self, listener: ghidra.app.decompiler.component.ClangHighlightListener) -> None: ...

    @overload
    def addPrimaryHighlights(self, parentNode: ghidra.app.decompiler.ClangNode, colorProvider: ghidra.app.plugin.core.decompile.actions.TokenHighlightColorProvider) -> None: ...

    @overload
    def addPrimaryHighlights(self, tokens: java.util.function.Supplier, hlColor: java.awt.Color) -> None: ...

    @overload
    def addPrimaryHighlights(self, parentNode: ghidra.app.decompiler.ClangNode, ops: java.util.Set, hlColor: java.awt.Color) -> None: ...

    @overload
    def addSecondaryHighlights(self, tokenText: unicode, tokens: java.util.function.Supplier) -> None: ...

    @overload
    def addSecondaryHighlights(self, tokens: java.util.function.Supplier, hlColor: java.awt.Color) -> None: ...

    def clearAllHighlights(self) -> None: ...

    def clearPrimaryHighlights(self) -> None: ...

    @staticmethod
    def dummyIfNull(c: ghidra.app.decompiler.component.ClangHighlightController) -> ghidra.app.decompiler.component.ClangHighlightController: ...

    def equals(self, __a0: object) -> bool: ...

    def fieldLocationChanged(self, location: docking.widgets.fieldpanel.support.FieldLocation, field: docking.widgets.fieldpanel.field.Field, trigger: docking.widgets.EventTrigger) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getCombinedColor(self, t: ghidra.app.decompiler.ClangToken) -> java.awt.Color: ...

    def getHighlightedText(self) -> unicode: ...

    def getPrimaryHighlightedTokens(self) -> ghidra.app.decompiler.component.TokenHighlights: ...

    def getSecondaryHighlightColors(self) -> ghidra.app.decompiler.component.TokenHighlightColors: ...

    def getSecondaryHighlightedTokens(self) -> ghidra.app.decompiler.component.TokenHighlights: ...

    def getSecondaryHighlightsByFunction(self, f: ghidra.program.model.listing.Function) -> java.util.Set: ...

    def getUpdateId(self) -> long: ...

    def hasPrimaryHighlight(self, token: ghidra.app.decompiler.ClangToken) -> bool: ...

    def hasSecondaryHighlight(self, token: ghidra.app.decompiler.ClangToken) -> bool: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeListener(self, listener: ghidra.app.decompiler.component.ClangHighlightListener) -> None: ...

    @overload
    def removeSecondaryHighlights(self, token: ghidra.app.decompiler.ClangToken) -> None: ...

    @overload
    def removeSecondaryHighlights(self, f: ghidra.program.model.listing.Function) -> None: ...

    @overload
    def removeSecondaryHighlights(self, tokens: java.util.function.Supplier) -> None: ...

    def toString(self) -> unicode: ...

    def togglePrimaryHighlights(self, hlColor: java.awt.Color, tokens: java.util.function.Supplier) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def highlightedText(self) -> unicode: ...

    @property
    def primaryHighlightedTokens(self) -> ghidra.app.decompiler.component.TokenHighlights: ...

    @property
    def secondaryHighlightColors(self) -> ghidra.app.decompiler.component.TokenHighlightColors: ...

    @property
    def secondaryHighlightedTokens(self) -> ghidra.app.decompiler.component.TokenHighlights: ...

    @property
    def updateId(self) -> long: ...
