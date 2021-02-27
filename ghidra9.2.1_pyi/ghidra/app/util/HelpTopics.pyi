import java.lang


class HelpTopics(object):
    """
    Topics for Help. The strings correspond to a folder under the "topics"
     resource.
    """

    ABOUT: unicode = u'About'
    AUTO_ANALYSIS: unicode = u'AutoAnalysisPlugin'
    BLOCK_MODEL: unicode = u'BlockModel'
    BOOKMARKS: unicode = u'BookmarkPlugin'
    BYTE_VIEWER: unicode = u'ByteViewerPlugin'
    CODE_BROWSER: unicode = u'CodeBrowserPlugin'
    COMMENTS: unicode = u'CommentsPlugin'
    DATA: unicode = u'DataPlugin'
    DATA_MANAGER: unicode = u'DataManagerPlugin'
    DATA_TYPE_EDITORS: unicode = u'DataTypeEditors'
    DECOMPILER: unicode = u'DecompilePlugin'
    DIFF: unicode = u'Diff'
    EQUATES: unicode = u'EquatePlugin'
    EXPORTER: unicode = u'ExporterPlugin'
    FIND_REFERENCES: unicode = u'LocationReferencesPlugin'
    FRONT_END: unicode = u'FrontEndPlugin'
    GLOSSARY: unicode = u'Glossary'
    HIGHLIGHT: unicode = u'SetHighlightPlugin'
    IMPORTER: unicode = u'ImporterPlugin'
    INTRO: unicode = u'Intro'
    LABEL: unicode = u'LabelMgrPlugin'
    MEMORY_MAP: unicode = u'MemoryMapPlugin'
    NAVIGATION: unicode = u'Navigation'
    PE2XML: unicode = u'PE2XMLPlugin'
    PROGRAM: unicode = u'ProgramManagerPlugin'
    PROGRAM_TREE: unicode = u'ProgramTreePlugin'
    REFERENCES: unicode = u'ReferencesPlugin'
    RELOCATION_TABLE: unicode = u'RelocationTablePlugin'
    REPOSITORY: unicode = u'Repository'
    SEARCH: unicode = u'Search'
    SELECTION: unicode = u'Selection'
    SYMBOL_TABLE: unicode = u'SymbolTablePlugin'
    SYMBOL_TREE: unicode = u'SymbolTreePlugin'
    TOOL: unicode = u'Tool'







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
