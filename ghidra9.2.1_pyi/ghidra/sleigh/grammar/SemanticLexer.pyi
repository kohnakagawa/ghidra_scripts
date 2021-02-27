from typing import List
import ghidra.sleigh.grammar
import java.lang
import org.antlr.runtime


class SemanticLexer(ghidra.sleigh.grammar.AbstractSleighLexer):
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
    gBaseLexer: ghidra.sleigh.grammar.SemanticLexer_BaseLexer



    @overload
    def __init__(self): ...

    @overload
    def __init__(self, input: org.antlr.runtime.CharStream): ...

    @overload
    def __init__(self, input: org.antlr.runtime.CharStream, state: org.antlr.runtime.RecognizerSharedState): ...



    def alreadyParsedRule(self, __a0: org.antlr.runtime.IntStream, __a1: int) -> bool: ...

    def beginResync(self) -> None: ...

    @overload
    def consumeUntil(self, __a0: org.antlr.runtime.IntStream, __a1: int) -> None: ...

    @overload
    def consumeUntil(self, __a0: org.antlr.runtime.IntStream, __a1: org.antlr.runtime.BitSet) -> None: ...

    def displayRecognitionError(self, __a0: List[unicode], __a1: org.antlr.runtime.RecognitionException) -> None: ...

    @overload
    def emit(self) -> org.antlr.runtime.Token: ...

    @overload
    def emit(self, __a0: org.antlr.runtime.Token) -> None: ...

    def emitErrorMessage(self, msg: unicode) -> None: ...

    def endResync(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def failed(self) -> bool: ...

    def getBacktrackingLevel(self) -> int: ...

    def getCharErrorDisplay(self, __a0: int) -> unicode: ...

    def getCharIndex(self) -> int: ...

    def getCharPositionInLine(self) -> int: ...

    def getCharStream(self) -> org.antlr.runtime.CharStream: ...

    def getClass(self) -> java.lang.Class: ...

    def getDelegates(self) -> List[ghidra.sleigh.grammar.AbstractSleighLexer]: ...

    def getEOFToken(self) -> org.antlr.runtime.Token: ...

    def getErrorHeader(self, e: org.antlr.runtime.RecognitionException) -> unicode: ...

    def getErrorMessage(self, e: org.antlr.runtime.RecognitionException, tokenNames: List[unicode]) -> unicode: ...

    def getGrammarFileName(self) -> unicode: ...

    def getLine(self) -> int: ...

    def getNumberOfSyntaxErrors(self) -> int: ...

    @overload
    def getRuleInvocationStack(self) -> List[object]: ...

    @overload
    @staticmethod
    def getRuleInvocationStack(__a0: java.lang.Throwable, __a1: unicode) -> List[object]: ...

    def getRuleMemoization(self, __a0: int, __a1: int) -> int: ...

    def getRuleMemoizationCacheSize(self) -> int: ...

    def getSourceName(self) -> unicode: ...

    def getText(self) -> unicode: ...

    def getTokenErrorDisplay(self, t: org.antlr.runtime.Token) -> unicode: ...

    def getTokenNames(self) -> List[unicode]: ...

    def hashCode(self) -> int: ...

    def mFDIV(self) -> None: ...

    def mFEQUAL(self) -> None: ...

    def mFGREAT(self) -> None: ...

    def mFGREATEQUAL(self) -> None: ...

    def mFLESS(self) -> None: ...

    def mFLESSEQUAL(self) -> None: ...

    def mFMINUS(self) -> None: ...

    def mFMULT(self) -> None: ...

    def mFNOTEQUAL(self) -> None: ...

    def mFPLUS(self) -> None: ...

    def mRES_IF(self) -> None: ...

    def mSDIV(self) -> None: ...

    def mSGREAT(self) -> None: ...

    def mSGREATEQUAL(self) -> None: ...

    def mSLESS(self) -> None: ...

    def mSLESSEQUAL(self) -> None: ...

    def mSREM(self) -> None: ...

    def mSRIGHT(self) -> None: ...

    def mTokens(self) -> None: ...

    @overload
    def match(self, __a0: int) -> None: ...

    @overload
    def match(self, __a0: unicode) -> None: ...

    @overload
    def match(self, __a0: org.antlr.runtime.IntStream, __a1: int, __a2: org.antlr.runtime.BitSet) -> object: ...

    @overload
    def matchAny(self) -> None: ...

    @overload
    def matchAny(self, __a0: org.antlr.runtime.IntStream) -> None: ...

    def matchRange(self, __a0: int, __a1: int) -> None: ...

    def memoize(self, __a0: org.antlr.runtime.IntStream, __a1: int, __a2: int) -> None: ...

    def mismatchIsMissingToken(self, __a0: org.antlr.runtime.IntStream, __a1: org.antlr.runtime.BitSet) -> bool: ...

    def mismatchIsUnwantedToken(self, __a0: org.antlr.runtime.IntStream, __a1: int) -> bool: ...

    def nextToken(self) -> org.antlr.runtime.Token: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def recover(self, __a0: org.antlr.runtime.RecognitionException) -> None: ...

    @overload
    def recover(self, __a0: org.antlr.runtime.IntStream, __a1: org.antlr.runtime.RecognitionException) -> None: ...

    def recoverFromMismatchedSet(self, __a0: org.antlr.runtime.IntStream, __a1: org.antlr.runtime.RecognitionException, __a2: org.antlr.runtime.BitSet) -> object: ...

    def reportError(self, __a0: org.antlr.runtime.RecognitionException) -> None: ...

    def reset(self) -> None: ...

    def setBacktrackingLevel(self, __a0: int) -> None: ...

    def setCharStream(self, __a0: org.antlr.runtime.CharStream) -> None: ...

    def setEnv(self, env: ghidra.sleigh.grammar.ParsingEnvironment) -> None: ...

    def setText(self, __a0: unicode) -> None: ...

    def skip(self) -> None: ...

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

    @property
    def delegates(self) -> List[ghidra.sleigh.grammar.AbstractSleighLexer]: ...

    @property
    def env(self) -> None: ...  # No getter available.

    @env.setter
    def env(self, value: ghidra.sleigh.grammar.ParsingEnvironment) -> None: ...

    @property
    def grammarFileName(self) -> unicode: ...
