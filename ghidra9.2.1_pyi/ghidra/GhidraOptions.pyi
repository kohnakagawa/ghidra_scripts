from typing import List
import ghidra
import java.lang


class GhidraOptions(object):
    """
    Contains miscellaneous defines used for options.
    """

    APPLY_ENABLED: unicode = u'apply.enabled'
    CATEGORY_AUTO_ANALYSIS: unicode = u'Auto Analysis'
    CATEGORY_BROWSER_DISPLAY: unicode = u'Listing Display'
    CATEGORY_BROWSER_FIELDS: unicode = u'Listing Fields'
    CATEGORY_BROWSER_NAVIGATION_MARKERS: unicode = u'Navigation Markers'
    CATEGORY_BROWSER_POPUPS: unicode = u'Listing Popups'
    CATEGORY_DECOMPILER_POPUPS: unicode = u'Decompiler Popups'
    CATEGORY_FLOW_OPTIONS: unicode = u'Selection by Flow'
    CURSOR_HIGHLIGHT_BUTTON_NAME: unicode = u'Cursor Text Highlight.Mouse Button To Activate'
    CURSOR_HIGHLIGHT_GROUP: unicode = u'Cursor Text Highlight'
    DEFAULT_CURSOR_LINE_COLOR: java.awt.Color = java.awt.Color[r=232,g=242,b=254]
    DEFAULT_HIGHLIGHT_COLOR: java.awt.Color = java.awt.Color[r=255,g=255,b=180]
    DEFAULT_SELECTION_COLOR: java.awt.Color = java.awt.Color[r=180,g=255,b=180]
    DELIMITER: int = '.'
    DISPLAY_NAMESPACE: unicode = u'Display Namespace'
    EXTERNAL_NAVIGATION_OPTION: unicode = u'External Navigation'
    FOLLOW_INDIRECTION_NAVIGATION_OPTION: unicode = u'Follow Indirection'
    HIGHLIGHT_COLOR_NAME: unicode = u'Cursor Text Highlight.Highlight Color'
    HIGHLIGHT_CURSOR_LINE: unicode = u'Cursor.Highlight Cursor Line'
    HIGHLIGHT_CURSOR_LINE_COLOR: unicode = u'Cursor.Highlight Cursor Line Color'
    HIGHLIGHT_CURSOR_LINE_COLOR_OPTION_NAME: unicode = u'Highlight Cursor Line Color'
    HIGHLIGHT_CURSOR_LINE_OPTION_NAME: unicode = u'Highlight Cursor Line'
    LABEL_GROUP_TITLE: unicode = u'Label Field'
    MNEMONIC_GROUP_TITLE: unicode = u'Mnemonic Field'
    NAVIGATION_OPTIONS: unicode = u'Navigation'
    NAVIGATION_RANGE_OPTION: unicode = u'Range Navigation'
    OLD_CATEGORY_BROWSER_DISPLAY: unicode = u'Browser Display'
    OLD_CATEGORY_BROWSER_FIELDS: unicode = u'Browser Fields'
    OLD_CATEGORY_BROWSER_POPUPS: unicode = u'Browser Popups'
    OPERAND_GROUP_TITLE: unicode = u'Operands Field'
    OPTION_BASE_FONT: unicode = u'BASE FONT'
    OPTION_FOLLOW_COMPUTED_CALL: unicode = u'Follow computed call'
    OPTION_FOLLOW_COMPUTED_JUMP: unicode = u'Follow computed jump'
    OPTION_FOLLOW_CONDITIONAL_CALL: unicode = u'Follow conditional call'
    OPTION_FOLLOW_CONDITIONAL_JUMP: unicode = u'Follow conditional jump'
    OPTION_FOLLOW_POINTERS: unicode = u'Follow pointers'
    OPTION_FOLLOW_UNCONDITIONAL_CALL: unicode = u'Follow unconditional call'
    OPTION_FOLLOW_UNCONDITIONAL_JUMP: unicode = u'Follow unconditional jump'
    OPTION_HIGHLIGHT_COLOR: unicode = u'Selection Colors.Highlight Color'
    OPTION_MAX_GO_TO_ENTRIES: unicode = u'Max Goto Entries'
    OPTION_NUMERIC_FORMATTING: unicode = u'Use C-like Numeric Formatting for Addresses'
    OPTION_SEARCH_LIMIT: unicode = u'Search Limit'
    OPTION_SEARCH_TITLE: unicode = u'Search'
    OPTION_SELECTION_COLOR: unicode = u'Selection Colors.Selection Color'
    OPTION_SHOW_BLOCK_NAME: unicode = u'Show Block Names'
    SHOW_BLOCK_NAME_OPTION: unicode = u'Operands Field.Show Block Names'




    class CURSOR_MOUSE_BUTTON_NAMES(java.lang.Enum):
        LEFT: ghidra.GhidraOptions.CURSOR_MOUSE_BUTTON_NAMES = LEFT
        MIDDLE: ghidra.GhidraOptions.CURSOR_MOUSE_BUTTON_NAMES = MIDDLE
        RIGHT: ghidra.GhidraOptions.CURSOR_MOUSE_BUTTON_NAMES = RIGHT







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def getMouseEventID(self) -> int: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.GhidraOptions.CURSOR_MOUSE_BUTTON_NAMES: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.GhidraOptions.CURSOR_MOUSE_BUTTON_NAMES]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...

        @property
        def mouseEventID(self) -> int: ...





    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

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
