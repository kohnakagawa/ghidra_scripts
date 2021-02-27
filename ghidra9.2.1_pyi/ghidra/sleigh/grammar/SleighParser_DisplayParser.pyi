from typing import List
import ghidra.sleigh.grammar
import ghidra.sleigh.grammar.SleighParser_DisplayParser
import java.lang
import org.antlr.runtime
import org.antlr.runtime.tree


class SleighParser_DisplayParser(ghidra.sleigh.grammar.AbstractSleighParser):
    ALPHA: int = 4
    ALPHAUP: int = 5
    AMPERSAND: int = 6
    ASSIGN: int = 7
    ASTERISK: int = 8
    BINDIGIT: int = 9
    BIN_INT: int = 10
    BOOL_AND: int = 11
    BOOL_OR: int = 12
    BOOL_XOR: int = 13
    CARET: int = 14
    COLON: int = 15
    COMMA: int = 16
    CPPCOMMENT: int = 17
    DEC_INT: int = 18
    DIGIT: int = 19
    DISPCHAR: int = 20
    ELLIPSIS: int = 21
    EOF: int = -1
    EOL: int = 22
    EQUAL: int = 23
    ESCAPE: int = 24
    EXCLAIM: int = 25
    FDIV: int = 26
    FEQUAL: int = 27
    FGREAT: int = 28
    FGREATEQUAL: int = 29
    FLESS: int = 30
    FLESSEQUAL: int = 31
    FMINUS: int = 32
    FMULT: int = 33
    FNOTEQUAL: int = 34
    FOLLOW_AMPERSAND_in_special582: org.antlr.runtime.BitSet = {1}
    FOLLOW_ASSIGN_in_special437: org.antlr.runtime.BitSet = {1}
    FOLLOW_ASTERISK_in_special491: org.antlr.runtime.BitSet = {1}
    FOLLOW_BIN_INT_in_special854: org.antlr.runtime.BitSet = {1}
    FOLLOW_BOOL_AND_in_special545: org.antlr.runtime.BitSet = {1}
    FOLLOW_BOOL_OR_in_special509: org.antlr.runtime.BitSet = {1}
    FOLLOW_BOOL_XOR_in_special527: org.antlr.runtime.BitSet = {1}
    FOLLOW_CARET_in_concatenate126: org.antlr.runtime.BitSet = {1}
    FOLLOW_COLON_in_display32: org.antlr.runtime.BitSet = {6,7,8,10,11,12,13,14,15,16,18,20,21,23,25,36,37,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,208,209,210,213,214,215,217,219,220,222,225,228,229,230,233,238}
    FOLLOW_COLON_in_special455: org.antlr.runtime.BitSet = {1}
    FOLLOW_COMMA_in_special473: org.antlr.runtime.BitSet = {1}
    FOLLOW_DEC_INT_in_special818: org.antlr.runtime.BitSet = {1}
    FOLLOW_DISPCHAR_in_special168: org.antlr.runtime.BitSet = {1}
    FOLLOW_ELLIPSIS_in_special312: org.antlr.runtime.BitSet = {1}
    FOLLOW_EQUAL_in_special330: org.antlr.runtime.BitSet = {1}
    FOLLOW_EXCLAIM_in_special709: org.antlr.runtime.BitSet = {1}
    FOLLOW_GREATEQUAL_in_special420: org.antlr.runtime.BitSet = {1}
    FOLLOW_GREAT_in_special385: org.antlr.runtime.BitSet = {1}
    FOLLOW_HEX_INT_in_special836: org.antlr.runtime.BitSet = {1}
    FOLLOW_LBRACE_in_special204: org.antlr.runtime.BitSet = {1}
    FOLLOW_LBRACKET_in_special240: org.antlr.runtime.BitSet = {1}
    FOLLOW_LEFT_in_special599: org.antlr.runtime.BitSet = {1}
    FOLLOW_LESSEQUAL_in_special403: org.antlr.runtime.BitSet = {1}
    FOLLOW_LESS_in_special366: org.antlr.runtime.BitSet = {1}
    FOLLOW_LINECOMMENT_in_special186: org.antlr.runtime.BitSet = {1}
    FOLLOW_LPAREN_in_special276: org.antlr.runtime.BitSet = {1}
    FOLLOW_MINUS_in_special655: org.antlr.runtime.BitSet = {1}
    FOLLOW_NOTEQUAL_in_special348: org.antlr.runtime.BitSet = {1}
    FOLLOW_PERCENT_in_special691: org.antlr.runtime.BitSet = {1}
    FOLLOW_PIPE_in_special563: org.antlr.runtime.BitSet = {1}
    FOLLOW_PLUS_in_special636: org.antlr.runtime.BitSet = {1}
    FOLLOW_RBRACE_in_special222: org.antlr.runtime.BitSet = {1}
    FOLLOW_RBRACKET_in_special258: org.antlr.runtime.BitSet = {1}
    FOLLOW_RES_IS_in_display36: org.antlr.runtime.BitSet = {1}
    FOLLOW_RIGHT_in_special618: org.antlr.runtime.BitSet = {1}
    FOLLOW_RPAREN_in_special294: org.antlr.runtime.BitSet = {1}
    FOLLOW_SEMI_in_special745: org.antlr.runtime.BitSet = {1}
    FOLLOW_SLASH_in_special673: org.antlr.runtime.BitSet = {1}
    FOLLOW_SPEC_AND_in_special782: org.antlr.runtime.BitSet = {1}
    FOLLOW_SPEC_OR_in_special764: org.antlr.runtime.BitSet = {1}
    FOLLOW_SPEC_XOR_in_special800: org.antlr.runtime.BitSet = {1}
    FOLLOW_TILDE_in_special727: org.antlr.runtime.BitSet = {1}
    FOLLOW_WS_in_whitespace102: org.antlr.runtime.BitSet = {1}
    FOLLOW_concatenate_in_printpiece79: org.antlr.runtime.BitSet = {1}
    FOLLOW_identifier_in_printpiece69: org.antlr.runtime.BitSet = {1}
    FOLLOW_pieces_in_display34: org.antlr.runtime.BitSet = {217}
    FOLLOW_printpiece_in_pieces57: org.antlr.runtime.BitSet = {1,6,7,8,10,11,12,13,14,15,16,18,20,21,23,25,36,37,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,208,209,210,213,214,215,219,220,222,225,228,229,230,233,238}
    FOLLOW_qstring_in_printpiece84: org.antlr.runtime.BitSet = {1}
    FOLLOW_special_in_printpiece89: org.antlr.runtime.BitSet = {1}
    FOLLOW_whitespace_in_printpiece74: org.antlr.runtime.BitSet = {1}
    FPLUS: int = 35
    GREAT: int = 36
    GREATEQUAL: int = 37
    HEXDIGIT: int = 38
    HEX_INT: int = 39
    IDENTIFIER: int = 40
    KEY_ALIGNMENT: int = 41
    KEY_ATTACH: int = 42
    KEY_BIG: int = 43
    KEY_BITRANGE: int = 44
    KEY_BUILD: int = 45
    KEY_CALL: int = 46
    KEY_CONTEXT: int = 47
    KEY_CROSSBUILD: int = 48
    KEY_DEC: int = 49
    KEY_DEFAULT: int = 50
    KEY_DEFINE: int = 51
    KEY_ENDIAN: int = 52
    KEY_EXPORT: int = 53
    KEY_GOTO: int = 54
    KEY_HEX: int = 55
    KEY_LITTLE: int = 56
    KEY_LOCAL: int = 57
    KEY_MACRO: int = 58
    KEY_NAMES: int = 59
    KEY_NOFLOW: int = 60
    KEY_OFFSET: int = 61
    KEY_PCODEOP: int = 62
    KEY_RETURN: int = 63
    KEY_SIGNED: int = 64
    KEY_SIZE: int = 65
    KEY_SPACE: int = 66
    KEY_TOKEN: int = 67
    KEY_TYPE: int = 68
    KEY_UNIMPL: int = 69
    KEY_VALUES: int = 70
    KEY_VARIABLES: int = 71
    KEY_WORDSIZE: int = 72
    LBRACE: int = 73
    LBRACKET: int = 74
    LEFT: int = 75
    LESS: int = 76
    LESSEQUAL: int = 77
    LINECOMMENT: int = 78
    LPAREN: int = 79
    MINUS: int = 80
    NOTEQUAL: int = 81
    OCTAL_ESCAPE: int = 82
    OP_ADD: int = 83
    OP_ADDRESS_OF: int = 84
    OP_ALIGNMENT: int = 85
    OP_AND: int = 86
    OP_APPLY: int = 87
    OP_ARGUMENTS: int = 88
    OP_ASSIGN: int = 89
    OP_BIG: int = 90
    OP_BIN_CONSTANT: int = 91
    OP_BITRANGE: int = 92
    OP_BITRANGE2: int = 93
    OP_BITRANGES: int = 94
    OP_BIT_PATTERN: int = 95
    OP_BOOL_AND: int = 96
    OP_BOOL_OR: int = 97
    OP_BOOL_XOR: int = 98
    OP_BUILD: int = 99
    OP_CALL: int = 100
    OP_CONCATENATE: int = 101
    OP_CONSTRUCTOR: int = 102
    OP_CONTEXT: int = 103
    OP_CONTEXT_BLOCK: int = 104
    OP_CROSSBUILD: int = 105
    OP_CTLIST: int = 106
    OP_DEC: int = 107
    OP_DECLARATIVE_SIZE: int = 108
    OP_DEC_CONSTANT: int = 109
    OP_DEFAULT: int = 110
    OP_DEREFERENCE: int = 111
    OP_DISPLAY: int = 112
    OP_DIV: int = 113
    OP_ELLIPSIS: int = 114
    OP_ELLIPSIS_RIGHT: int = 115
    OP_EMPTY_LIST: int = 116
    OP_ENDIAN: int = 117
    OP_EQUAL: int = 118
    OP_EXPORT: int = 119
    OP_FADD: int = 120
    OP_FDIV: int = 121
    OP_FEQUAL: int = 122
    OP_FGREAT: int = 123
    OP_FGREATEQUAL: int = 124
    OP_FIELDDEF: int = 125
    OP_FIELDDEFS: int = 126
    OP_FIELD_MODS: int = 127
    OP_FLESS: int = 128
    OP_FLESSEQUAL: int = 129
    OP_FMULT: int = 130
    OP_FNEGATE: int = 131
    OP_FNOTEQUAL: int = 132
    OP_FSUB: int = 133
    OP_GOTO: int = 134
    OP_GREAT: int = 135
    OP_GREATEQUAL: int = 136
    OP_HEX: int = 137
    OP_HEX_CONSTANT: int = 138
    OP_IDENTIFIER: int = 139
    OP_IDENTIFIER_LIST: int = 140
    OP_IF: int = 141
    OP_INTBLIST: int = 142
    OP_INVERT: int = 143
    OP_JUMPDEST_ABSOLUTE: int = 144
    OP_JUMPDEST_DYNAMIC: int = 145
    OP_JUMPDEST_LABEL: int = 146
    OP_JUMPDEST_RELATIVE: int = 147
    OP_JUMPDEST_SYMBOL: int = 148
    OP_LABEL: int = 149
    OP_LEFT: int = 150
    OP_LESS: int = 151
    OP_LESSEQUAL: int = 152
    OP_LITTLE: int = 153
    OP_LOCAL: int = 154
    OP_MACRO: int = 155
    OP_MULT: int = 156
    OP_NAMES: int = 157
    OP_NEGATE: int = 158
    OP_NIL: int = 159
    OP_NOFLOW: int = 160
    OP_NOP: int = 161
    OP_NOT: int = 162
    OP_NOTEQUAL: int = 163
    OP_NOT_DEFAULT: int = 164
    OP_NO_CONTEXT_BLOCK: int = 165
    OP_NO_FIELD_MOD: int = 166
    OP_OR: int = 167
    OP_PARENTHESIZED: int = 168
    OP_PCODE: int = 169
    OP_PCODEOP: int = 170
    OP_QSTRING: int = 171
    OP_REM: int = 172
    OP_RETURN: int = 173
    OP_RIGHT: int = 174
    OP_SDIV: int = 175
    OP_SECTION_LABEL: int = 176
    OP_SEMANTIC: int = 177
    OP_SEQUENCE: int = 178
    OP_SGREAT: int = 179
    OP_SGREATEQUAL: int = 180
    OP_SIGNED: int = 181
    OP_SIZE: int = 182
    OP_SIZING_SIZE: int = 183
    OP_SLESS: int = 184
    OP_SLESSEQUAL: int = 185
    OP_SPACE: int = 186
    OP_SPACEMODS: int = 187
    OP_SREM: int = 188
    OP_SRIGHT: int = 189
    OP_STRING: int = 190
    OP_STRING_OR_IDENT_LIST: int = 191
    OP_SUB: int = 192
    OP_SUBTABLE: int = 193
    OP_TABLE: int = 194
    OP_TOKEN: int = 195
    OP_TOKEN_ENDIAN: int = 196
    OP_TRUNCATION_SIZE: int = 197
    OP_TYPE: int = 198
    OP_UNIMPL: int = 199
    OP_VALUES: int = 200
    OP_VARIABLES: int = 201
    OP_VARNODE: int = 202
    OP_WHITESPACE: int = 203
    OP_WILDCARD: int = 204
    OP_WITH: int = 205
    OP_WORDSIZE: int = 206
    OP_XOR: int = 207
    PERCENT: int = 208
    PIPE: int = 209
    PLUS: int = 210
    PP_ESCAPE: int = 211
    PP_POSITION: int = 212
    QSTRING: int = 213
    RBRACE: int = 214
    RBRACKET: int = 215
    RES_IF: int = 216
    RES_IS: int = 217
    RES_WITH: int = 218
    RIGHT: int = 219
    RPAREN: int = 220
    SDIV: int = 221
    SEMI: int = 222
    SGREAT: int = 223
    SGREATEQUAL: int = 224
    SLASH: int = 225
    SLESS: int = 226
    SLESSEQUAL: int = 227
    SPEC_AND: int = 228
    SPEC_OR: int = 229
    SPEC_XOR: int = 230
    SREM: int = 231
    SRIGHT: int = 232
    TILDE: int = 233
    Tokens: int = 234
    UNDERSCORE: int = 235
    UNICODE_ESCAPE: int = 236
    UNKNOWN: int = 237
    WS: int = 238
    gParent: ghidra.sleigh.grammar.SleighParser
    gSleighParser: ghidra.sleigh.grammar.SleighParser
    input: org.antlr.runtime.TokenStream




    class display_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



        def __init__(self): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getStart(self) -> object: ...

        def getStop(self) -> object: ...

        def getTemplate(self) -> object: ...

        def getTree(self) -> object: ...

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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class whitespace_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



        def __init__(self): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getStart(self) -> object: ...

        def getStop(self) -> object: ...

        def getTemplate(self) -> object: ...

        def getTree(self) -> object: ...

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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class special_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



        def __init__(self): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getStart(self) -> object: ...

        def getStop(self) -> object: ...

        def getTemplate(self) -> object: ...

        def getTree(self) -> object: ...

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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class concatenate_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



        def __init__(self): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getStart(self) -> object: ...

        def getStop(self) -> object: ...

        def getTemplate(self) -> object: ...

        def getTree(self) -> object: ...

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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class printpiece_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



        def __init__(self): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getStart(self) -> object: ...

        def getStop(self) -> object: ...

        def getTemplate(self) -> object: ...

        def getTree(self) -> object: ...

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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class pieces_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



        def __init__(self): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getStart(self) -> object: ...

        def getStop(self) -> object: ...

        def getTemplate(self) -> object: ...

        def getTree(self) -> object: ...

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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...

    @overload
    def __init__(self, input: org.antlr.runtime.TokenStream, gSleighParser: ghidra.sleigh.grammar.SleighParser): ...

    @overload
    def __init__(self, input: org.antlr.runtime.TokenStream, state: org.antlr.runtime.RecognizerSharedState, gSleighParser: ghidra.sleigh.grammar.SleighParser): ...



    def alreadyParsedRule(self, __a0: org.antlr.runtime.IntStream, __a1: int) -> bool: ...

    def beginResync(self) -> None: ...

    def concatenate(self) -> ghidra.sleigh.grammar.SleighParser_DisplayParser.concatenate_return: ...

    @overload
    def consumeUntil(self, __a0: org.antlr.runtime.IntStream, __a1: int) -> None: ...

    @overload
    def consumeUntil(self, __a0: org.antlr.runtime.IntStream, __a1: org.antlr.runtime.BitSet) -> None: ...

    def display(self) -> ghidra.sleigh.grammar.SleighParser_DisplayParser.display_return: ...

    def displayRecognitionError(self, __a0: List[unicode], __a1: org.antlr.runtime.RecognitionException) -> None: ...

    def emitErrorMessage(self, msg: unicode) -> None: ...

    def endResync(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def failed(self) -> bool: ...

    def getBacktrackingLevel(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getDelegates(self) -> List[ghidra.sleigh.grammar.AbstractSleighParser]: ...

    def getErrorHeader(self, e: org.antlr.runtime.RecognitionException) -> unicode: ...

    def getErrorMessage(self, e: org.antlr.runtime.RecognitionException, tokenNames: List[unicode]) -> unicode: ...

    def getGrammarFileName(self) -> unicode: ...

    def getNumberOfSyntaxErrors(self) -> int: ...

    @overload
    def getRuleInvocationStack(self) -> List[object]: ...

    @overload
    @staticmethod
    def getRuleInvocationStack(__a0: java.lang.Throwable, __a1: unicode) -> List[object]: ...

    def getRuleMemoization(self, __a0: int, __a1: int) -> int: ...

    def getRuleMemoizationCacheSize(self) -> int: ...

    def getSourceName(self) -> unicode: ...

    def getTokenErrorDisplay(self, t: org.antlr.runtime.Token) -> unicode: ...

    def getTokenNames(self) -> List[unicode]: ...

    def getTokenStream(self) -> org.antlr.runtime.TokenStream: ...

    def getTreeAdaptor(self) -> org.antlr.runtime.tree.TreeAdaptor: ...

    def hashCode(self) -> int: ...

    def match(self, __a0: org.antlr.runtime.IntStream, __a1: int, __a2: org.antlr.runtime.BitSet) -> object: ...

    def matchAny(self, __a0: org.antlr.runtime.IntStream) -> None: ...

    def memoize(self, __a0: org.antlr.runtime.IntStream, __a1: int, __a2: int) -> None: ...

    def mismatchIsMissingToken(self, __a0: org.antlr.runtime.IntStream, __a1: org.antlr.runtime.BitSet) -> bool: ...

    def mismatchIsUnwantedToken(self, __a0: org.antlr.runtime.IntStream, __a1: int) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def pieces(self) -> ghidra.sleigh.grammar.SleighParser_DisplayParser.pieces_return: ...

    def printpiece(self) -> ghidra.sleigh.grammar.SleighParser_DisplayParser.printpiece_return: ...

    def recover(self, __a0: org.antlr.runtime.IntStream, __a1: org.antlr.runtime.RecognitionException) -> None: ...

    def recoverFromMismatchedSet(self, __a0: org.antlr.runtime.IntStream, __a1: org.antlr.runtime.RecognitionException, __a2: org.antlr.runtime.BitSet) -> object: ...

    def reportError(self, __a0: org.antlr.runtime.RecognitionException) -> None: ...

    def reset(self) -> None: ...

    def setBacktrackingLevel(self, __a0: int) -> None: ...

    def setEnv(self, env: ghidra.sleigh.grammar.ParsingEnvironment) -> None: ...

    def setLexer(self, lexer: ghidra.sleigh.grammar.SleighLexer) -> None: ...

    def setTokenStream(self, __a0: org.antlr.runtime.TokenStream) -> None: ...

    def setTreeAdaptor(self, adaptor: org.antlr.runtime.tree.TreeAdaptor) -> None: ...

    def special(self) -> ghidra.sleigh.grammar.SleighParser_DisplayParser.special_return: ...

    def toString(self) -> unicode: ...

    def toStrings(self, __a0: List[object]) -> List[object]: ...

    @overload
    def traceIn(self, __a0: unicode, __a1: int) -> None: ...

    @overload
    def traceIn(self, __a0: unicode, __a1: int, __a2: object) -> None: ...

    @overload
    def traceOut(self, __a0: unicode, __a1: int) -> None: ...

    @overload
    def traceOut(self, __a0: unicode, __a1: int, __a2: object) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def whitespace(self) -> ghidra.sleigh.grammar.SleighParser_DisplayParser.whitespace_return: ...

    @property
    def delegates(self) -> List[ghidra.sleigh.grammar.AbstractSleighParser]: ...

    @property
    def grammarFileName(self) -> unicode: ...

    @property
    def tokenNames(self) -> List[unicode]: ...

    @property
    def treeAdaptor(self) -> org.antlr.runtime.tree.TreeAdaptor: ...

    @treeAdaptor.setter
    def treeAdaptor(self, value: org.antlr.runtime.tree.TreeAdaptor) -> None: ...
