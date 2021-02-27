import ghidra.app.util.cparser.CPP
import java.io
import java.lang


class PreProcessorTokenManager(object, ghidra.app.util.cparser.CPP.PreProcessorConstants):
    AND: int = 102
    BEGITEM: int = 116
    CMT: int = 26
    COD: int = 30
    COLON: int = 112
    COMMA: int = 81
    COMMENT: int = 19
    CONLINE: int = 166
    CONSTANT: int = 17
    CONSTITUENT: int = 162
    CONTARG: int = 26
    CP: int = 37
    DECIMAL_LITERAL: int = 55
    DEFAULT: int = 0
    DEFD: int = 34
    DEFINE: int = 16
    DEFINED: int = 92
    DIR: int = 24
    DIRECTIVE: int = 1
    DIRECTIVECOMMENT: int = 21
    DIRLINE: int = 77
    ECMT: int = 27
    EIFLINE: int = 83
    ELIF: int = 86
    ELSE: int = 87
    ENDCMT: int = 28
    ENDIF: int = 88
    ENDITEM: int = 117
    ENDL: int = 31
    ENDREL: int = 36
    EOF: int = 0
    EQ: int = 96
    ERRLINE: int = 152
    ERROR: int = 12
    ERROR_EXPRN: int = 151
    ESTD: int = 136
    EXPATH: int = 128
    EXPONENT: int = 60
    FP_LITERAL: int = 59
    FP_NUMERIC: int = 114
    GE: int = 101
    GT: int = 99
    HASINCLUDE: int = 93
    HASINCLUDENEXT: int = 94
    HEX_DIGIT: int = 57
    HEX_LITERAL: int = 56
    IF: int = 85
    IFDEF: int = 10
    IFDEFED: int = 89
    IFDEF_EXPRN: int = 143
    IFDLINE: int = 146
    IFNDEF: int = 11
    IFNDEFED: int = 90
    IFNDEF_EXPRN: int = 147
    IFNDLINE: int = 150
    IGNORETOEOL: int = 2
    INCDEF: int = 3
    INCLINE: int = 130
    INCLUDE: int = 6
    INFO: int = 14
    INFOLINE: int = 158
    INFO_EXPRN: int = 157
    INTEGER_LITERAL: int = 54
    ITEM: int = 115
    LE: int = 100
    LEADIN3: int = 202
    LINE: int = 18
    LINECOMMENT: int = 20
    LINEINFO: int = 171
    LINLINE: int = 170
    LOG_AND: int = 105
    LOG_OR: int = 104
    LSH: int = 106
    LT: int = 98
    MACEXPPATH: int = 131
    MACROARGS: int = 25
    MACROMV: int = 187
    MACRORV: int = 196
    MACROVALS: int = 27
    MACROVALS_COMMENT: int = 29
    MANIFEST: int = 169
    MCVLINE: int = 201
    MINUS: int = 108
    MOREARG: int = 195
    MOREVAL: int = 182
    MQUOTED_VAL: int = 28
    MQUOTED_VALUE: int = 204
    NEQ: int = 97
    NEWLINE: int = 64
    NOPAR: int = 39
    NOT: int = 91
    NOTCHR: int = 61
    NOTCMT: int = 46
    NOTCMTCOD: int = 47
    NOTENDL: int = 43
    NOTENDLC: int = 44
    NOTENDLSTAR: int = 45
    NOTVALCMT: int = 53
    NOTWQC: int = 50
    NOTWS: int = 48
    NOTWSQ: int = 49
    NOTWSQLT: int = 52
    NOTWWSQLT: int = 51
    NUMERIC: int = 113
    OCTAL_LITERAL: int = 58
    OP: int = 38
    OPTD: int = 35
    OPTIONED: int = 95
    OR: int = 103
    OTHER_TEXT: int = 65
    OUTER_TEXT: int = 63
    PLUS: int = 109
    PRAGMA: int = 9
    PRAGMA_EXPRN: int = 140
    PRGLINE: int = 141
    QMARK: int = 111
    QUOTED_TEXT: int = 66
    QUOTED_VAL: int = 24
    QUOTED_VALUE: int = 186
    REL: int = 42
    RELATIVE: int = 139
    RELPATH: int = 8
    RSH: int = 107
    RVALUES: int = 22
    RVALUES_COMMENT: int = 23
    RVSLINE: int = 180
    STANDARD: int = 137
    STARTCMT: int = 29
    STD: int = 41
    STDPATH: int = 7
    TIMES: int = 110
    UNDEFINE: int = 15
    UNDIR: int = 32
    UNDIRALL: int = 33
    UNDLINE: int = 160
    VALUES: int = 181
    WARNING: int = 13
    WARNING_EXPRN: int = 154
    WARNLINE: int = 155
    WS: int = 62
    WSP: int = 40
    XSYM: int = 25
    XSYMLINK: int = 4
    XSYMLINKPATH: int = 129
    XSYMPATH: int = 5
    _AND: int = 14
    _BLANKLINE: int = 5
    _CMT: int = 4
    _CMT0: int = 84
    _CMT11: int = 120
    _CMT3: int = 173
    _CMT4: int = 176
    _CMT5: int = 189
    _COD: int = 132
    _COD1: int = 79
    _COD2: int = 179
    _COD3: int = 192
    _COD4: int = 198
    _CODC: int = 168
    _COLON: int = 23
    _COMMENT: int = 7
    _CTRL: int = 1
    _ECMT10: int = 174
    _ECMT3: int = 172
    _ECMT5: int = 188
    _ECMT7: int = 183
    _ECMT8: int = 199
    _ECMT9: int = 205
    _EECMT7: int = 184
    _EECMT9: int = 207
    _EEECMT9: int = 206
    _ENDREL: int = 138
    _EQ: int = 8
    _EQT: int = 185
    _EQT1: int = 203
    _EWSP: int = 191
    _GE: int = 13
    _GT: int = 11
    _HEX: int = 126
    _INCCOD: int = 121
    _INCCP: int = 123
    _INCOP: int = 124
    _INCSTANDARD: int = 125
    _INCWSP: int = 122
    _LCMT: int = 3
    _LCMT0: int = 82
    _LCMT11: int = 119
    _LCMT20: int = 144
    _LCMT21: int = 148
    _LCMT4: int = 175
    _LCMT7: int = 197
    _LE: int = 12
    _LEADIN1: int = 161
    _LEADIN2: int = 163
    _LINECOMMENT: int = 6
    _LOG_AND: int = 15
    _LOG_OR: int = 17
    _LSH: int = 18
    _LT: int = 10
    _MACWSP: int = 193
    _MINUS: int = 20
    _MWSP: int = 190
    _NEQ: int = 9
    _OR: int = 16
    _PLUS: int = 21
    _QMARK: int = 22
    _QTE: int = 135
    _QTE0: int = 177
    _QTE1: int = 200
    _RSH: int = 19
    _TOEOL: int = 118
    _WSP: int = 133
    _WSP0: int = 78
    _WSP1: int = 142
    _WSP2: int = 80
    _WSP3: int = 145
    _WSP4: int = 149
    _WSP5: int = 153
    _WSP6: int = 156
    _WSP7: int = 167
    _WSP8: int = 178
    _WSP_INFO: int = 159
    _XSYM: int = 2
    _XSYMENDL: int = 127
    __LT: int = 134
    debugStream: java.io.PrintStream
    jjnewLexState: List[int] = array('i', [-1, 1, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 6, 6, 6, 9, 12, 13, 14, 16, 15, 18, 0, -1, -1, -1, -1, 20, 0, 21, -1, -1, -1, -1, 10, 11, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 21, -1, -1, 1, -1, -1, 5, -1, 0, -1, -1, 0, -1, -1, 7, 8, 0, -1, 0, -1, 0, 0, -1, 0, 20, -1, 0, 0, 20, -1, 0, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, -1, 0, 17, 25, 27, 0, 22, 22, -1, 0, -1, 0, 0, 1, 20, 23, 24, -1, -1, 0, -1, -1, -1, 22, 22, -1, -1, -1, -1, -1, 27, -1, -1, 27, -1, -1, 20, -1, 29, 28, 0, -1, 27, -1, -1, 27, 0])
    jjstrLiteralImages: List[unicode] = array(java.lang.String, [u'', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, u'if', u'elif', u'else', u'endif', u'ifdef', u'ifndef', None, None, u'__has_include', u'__has_include_next', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])
    lexStateNames: List[unicode] = array(java.lang.String, [u'DEFAULT', u'DIRECTIVE', u'IGNORETOEOL', u'INCDEF', u'XSYMLINK', u'XSYMPATH', u'INCLUDE', u'STDPATH', u'RELPATH', u'PRAGMA', u'IFDEF', u'IFNDEF', u'ERROR', u'WARNING', u'INFO', u'UNDEFINE', u'DEFINE', u'CONSTANT', u'LINE', u'COMMENT', u'LINECOMMENT', u'DIRECTIVECOMMENT', u'RVALUES', u'RVALUES_COMMENT', u'QUOTED_VAL', u'MACROARGS', u'CONTARG', u'MACROVALS', u'MQUOTED_VAL', u'MACROVALS_COMMENT'])
    tokenImage: List[unicode] = array(java.lang.String, [u'<EOF>', u'<_CTRL>', u'<_XSYM>', u'<_LCMT>', u'<_CMT>', u'<_BLANKLINE>', u'<_LINECOMMENT>', u'<_COMMENT>', u'"=="', u'"!="', u'"<"', u'">"', u'"<="', u'">="', u'"&&"', u'"&"', u'"||"', u'"|"', u'"<<"', u'">>"', u'"-"', u'"+"', u'"?"', u'":"', u'"#"', u'"XSym"', u'"/"', u'"*"', u'"*/"', u'"/*"', u'<COD>', u'<ENDL>', u'<UNDIR>', u'<UNDIRALL>', u'"defined"', u'"__option"', u'"\\""', u'")"', u'"("', u'<NOPAR>', u'<WSP>', u'<STD>', u'<REL>', u'<NOTENDL>', u'<NOTENDLC>', u'<NOTENDLSTAR>', u'<NOTCMT>', u'<NOTCMTCOD>', u'<NOTWS>', u'<NOTWSQ>', u'<NOTWQC>', u'<NOTWWSQLT>', u'<NOTWSQLT>', u'"/##/"', u'<INTEGER_LITERAL>', u'<DECIMAL_LITERAL>', u'<HEX_LITERAL>', u'<HEX_DIGIT>', u'<OCTAL_LITERAL>', u'<FP_LITERAL>', u'<EXPONENT>', u'"!"', u'<WS>', u'<OUTER_TEXT>', u'<NEWLINE>', u'<OTHER_TEXT>', u'<QUOTED_TEXT>', u'"include"', u'"import"', u'"include_next"', u'"pragma"', u'"error"', u'"warning"', u'"info"', u'"define"', u'"undef"', u'"line"', u'<DIRLINE>', u'<_WSP0>', u'<_COD1>', u'<_WSP2>', u'","', u'<_LCMT0>', u'<EIFLINE>', u'<_CMT0>', u'"if"', u'"elif"', u'"else"', u'"endif"', u'"ifdef"', u'"ifndef"', u'<NOT>', u'<DEFINED>', u'"__has_include"', u'"__has_include_next"', u'<OPTIONED>', u'<EQ>', u'<NEQ>', u'<LT>', u'<GT>', u'<LE>', u'<GE>', u'<AND>', u'<OR>', u'<LOG_OR>', u'<LOG_AND>', u'<LSH>', u'<RSH>', u'<MINUS>', u'<PLUS>', u'<TIMES>', u'<QMARK>', u'<COLON>', u'<NUMERIC>', u'<FP_NUMERIC>', u'<ITEM>', u'<BEGITEM>', u'<ENDITEM>', u'<_TOEOL>', u'<_LCMT11>', u'<_CMT11>', u'<_INCCOD>', u'<_INCWSP>', u'<_INCCP>', u'<_INCOP>', u'<_INCSTANDARD>', u'<_HEX>', u'<_XSYMENDL>', u'<EXPATH>', u'<XSYMLINKPATH>', u'<INCLINE>', u'<MACEXPPATH>', u'<_COD>', u'<_WSP>', u'<__LT>', u'<_QTE>', u'<ESTD>', u'<STANDARD>', u'<_ENDREL>', u'<RELATIVE>', u'<PRAGMA_EXPRN>', u'<PRGLINE>', u'<_WSP1>', u'<IFDEF_EXPRN>', u'<_LCMT20>', u'<_WSP3>', u'<IFDLINE>', u'<IFNDEF_EXPRN>', u'<_LCMT21>', u'<_WSP4>', u'<IFNDLINE>', u'<ERROR_EXPRN>', u'<ERRLINE>', u'<_WSP5>', u'<WARNING_EXPRN>', u'<WARNLINE>', u'<_WSP6>', u'<INFO_EXPRN>', u'<INFOLINE>', u'<_WSP_INFO>', u'<UNDLINE>', u'<_LEADIN1>', u'<CONSTITUENT>', u'<_LEADIN2>', u'"("', u'")"', u'<CONLINE>', u'<_WSP7>', u'<_CODC>', u'<MANIFEST>', u'<LINLINE>', u'<LINEINFO>', u'<_ECMT3>', u'<_CMT3>', u'<_ECMT10>', u'<_LCMT4>', u'<_CMT4>', u'<_QTE0>', u'<_WSP8>', u'<_COD2>', u'<RVSLINE>', u'<VALUES>', u'<MOREVAL>', u'<_ECMT7>', u'<_EECMT7>', u'<_EQT>', u'<QUOTED_VALUE>', u'<MACROMV>', u'<_ECMT5>', u'<_CMT5>', u'","', u'")"', u'<_COD3>', u'<_MACWSP>', u'")"', u'<MOREARG>', u'<MACRORV>', u'<_LCMT7>', u'<_COD4>', u'<_ECMT8>', u'<_QTE1>', u'<MCVLINE>', u'<LEADIN3>', u'<_EQT1>', u'<MQUOTED_VALUE>', u'<_ECMT9>', u'<_EEECMT9>', u'<_EECMT9>'])



    @overload
    def __init__(self, __a0: ghidra.app.util.cparser.CPP.JavaCharStream): ...

    @overload
    def __init__(self, __a0: ghidra.app.util.cparser.CPP.JavaCharStream, __a1: int): ...



    @overload
    def ReInit(self, __a0: ghidra.app.util.cparser.CPP.JavaCharStream) -> None: ...

    @overload
    def ReInit(self, __a0: ghidra.app.util.cparser.CPP.JavaCharStream, __a1: int) -> None: ...

    def SwitchTo(self, __a0: int) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getNextToken(self) -> ghidra.app.util.cparser.CPP.Token: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setDebugStream(self, __a0: java.io.PrintStream) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def nextToken(self) -> ghidra.app.util.cparser.CPP.Token: ...
