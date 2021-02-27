import java.lang


class PluginConstants(object):
    """
    Miscellaneous defined constants
    """

    ANYSINGLECHAR_WILDCARD_CHAR: int = '?'
    ANYSUBSTRING_WILDCARD_CHAR: int = '*'
    AUTO_RESTRICT_SELECTION: unicode = u'Auto Restrict Memory Search on Selection'
    BOOKMARKS: unicode = u'Bookmarks'
    BYTE_VIEWER: unicode = u'ByteViewerPlugin'
    CATEGORY_DELIMITER: unicode = u'.'
    CODE_BROWSER: unicode = u'Listing'
    DEFAULT_SEARCH_LIMIT: int = 500
    DEFAULT_TREE_NAME: unicode = u'Program Tree'
    DEVELOP: unicode = u'(Develop)'
    MEMORY_MAP: unicode = u'Memory Map'
    PRE_POPULATE_MEM_SEARCH: unicode = u'Pre-populate Memory Search'
    PROTOTYPE: unicode = u' (Prototype)'
    SEARCH_HIGHLIGHT_COLOR: java.awt.Color = java.awt.Color[r=255,g=255,b=200]
    SEARCH_HIGHLIGHT_COLOR_NAME: unicode = u' Highlight Color'
    SEARCH_HIGHLIGHT_CURRENT_ADDR_COLOR: java.awt.Color = java.awt.Color[r=255,g=255,b=0]
    SEARCH_HIGHLIGHT_CURRENT_COLOR_NAME: unicode = u'Highlight Color for Current Match'
    SEARCH_HIGHLIGHT_NAME: unicode = u'Highlight Search Results'
    SEARCH_OPTION_NAME: unicode = u'Search'







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
