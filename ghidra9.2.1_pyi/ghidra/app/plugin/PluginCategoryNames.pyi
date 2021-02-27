import java.lang


class PluginCategoryNames(object):
    ANALYSIS: unicode = u'Analysis'
    BYTE_VIEWER: unicode = u'Byte Viewer'
    CODE_VIEWER: unicode = u'Code Viewer'
    COMMON: unicode = u'Common'
    DEBUGGER: unicode = u'Debugger'
    DECOMPILER: unicode = u'Decompiler'
    DIFF: unicode = u'Code Difference'
    EXAMPLES: unicode = u'Examples'
    GRAPH: unicode = u'Graph'
    INTERPRETERS: unicode = u'Interpreters'
    MISC: unicode = u'Miscellaneous'
    NAVIGATION: unicode = u'Navigation'
    PATCHING: unicode = u'Patching'
    SEARCH: unicode = u'Search'
    SELECTION: unicode = u'Selection'
    SUPPORT: unicode = u'Support'
    TESTING: unicode = u'Testing'
    TREE: unicode = u'Program Tree'
    UNMANAGED: unicode = u'Unmanaged'
    USER_ANNOTATION: unicode = u'User Annotation'







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
