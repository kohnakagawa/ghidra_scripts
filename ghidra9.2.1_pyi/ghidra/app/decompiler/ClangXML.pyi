import ghidra.app.decompiler
import ghidra.program.model.pcode
import ghidra.xml
import java.lang


class ClangXML(object):
    """
    To change the template for this generated type comment go to

    """

    BLOCK: unicode = u'block'
    BLOCKREF: unicode = u'blockref'
    BREAK: unicode = u'break'
    COLOR: unicode = u'color'
    COMMENT: unicode = u'comment'
    COMMENT_COLOR: unicode = u'comment'
    CONST_COLOR: unicode = u'const'
    DOCUMENT: unicode = u'clang_document'
    FIELD: unicode = u'field'
    FUNCNAME: unicode = u'funcname'
    FUNCNAME_COLOR: unicode = u'funcname'
    FUNCPROTO: unicode = u'funcproto'
    FUNCTION: unicode = u'function'
    GLOBAL_COLOR: unicode = u'global'
    INDENT: unicode = u'indent'
    KEYWORD_COLOR: unicode = u'keyword'
    LABEL: unicode = u'label'
    OFFSET: unicode = u'off'
    OP: unicode = u'op'
    OPREF: unicode = u'opref'
    PARAMETER_COLOR: unicode = u'param'
    PCOFFSET: unicode = u'pcoff'
    PCSPACE: unicode = u'pcspace'
    RETURN_TYPE: unicode = u'return_type'
    SPACE: unicode = u'space'
    STATEMENT: unicode = u'statement'
    SYMREF: unicode = u'symref'
    SYNTAX: unicode = u'syntax'
    TYPE: unicode = u'type'
    TYPE_COLOR: unicode = u'type'
    VARDECL: unicode = u'vardecl'
    VARIABLE: unicode = u'variable'
    VARIABLE_COLOR: unicode = u'var'
    VARNODEREF: unicode = u'varref'



    def __init__(self): ...



    @staticmethod
    def buildClangTree(parser: ghidra.xml.XmlPullParser, hfunc: ghidra.program.model.pcode.HighFunction) -> ghidra.app.decompiler.ClangTokenGroup: ...

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
