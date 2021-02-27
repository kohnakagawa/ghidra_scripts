import java.lang


class CParserConstants(object):
    ASM: int = 45
    ASMBLOCK: int = 1
    ASMBLOCKB: int = 80
    ASMBLOCKP: int = 81
    ASM_SEMI: int = 82
    ATTRIBUTE: int = 42
    AUTO: int = 61
    BREAK: int = 33
    CASE: int = 50
    CDECL: int = 36
    CHAR: int = 63
    CHARACTER_LITERAL: int = 15
    CONST: int = 35
    CONTINUE: int = 17
    DECIMAL_LITERAL: int = 10
    DECLSPEC: int = 37
    DEFAULT: int = 0
    DFLT: int = 22
    DIGIT: int = 77
    DO: int = 70
    DOUBLE: int = 23
    ELSE: int = 49
    ENUM: int = 60
    EOF: int = 0
    EXPONENT: int = 14
    EXTENSION: int = 43
    EXTERN: int = 27
    FAR: int = 66
    FASTCALL: int = 41
    FLOAT: int = 47
    FLOATING_POINT_LITERAL: int = 13
    FOR: int = 67
    GOTO: int = 64
    HEX_LITERAL: int = 11
    IDENTIFIER: int = 75
    IF: int = 69
    INLINE: int = 46
    INT: int = 68
    INT16: int = 53
    INT32: int = 54
    INT64: int = 55
    INT8: int = 52
    INTEGER_LITERAL: int = 9
    INTERFACE: int = 72
    LETTER: int = 76
    LINE: int = 73
    LINEALT: int = 74
    LINEBLOCK: int = 2
    LINENUMBER_LITERAL: int = 88
    LONG: int = 51
    NEAR: int = 65
    OBJC: int = 4
    OBJC2: int = 5
    OBJC2_END: int = 131
    OBJC2_IGNORE: int = 130
    OBJC_DIGIT: int = 118
    OBJC_IDENTIFIER: int = 116
    OBJC_IGNORE: int = 115
    OBJC_LETTER: int = 117
    OBJC_SEMI: int = 119
    OCTAL_LITERAL: int = 12
    PATH_LITERAL: int = 87
    PCLOSE: int = 101
    PCOLON: int = 103
    PCOMMA: int = 104
    PDECIMAL_LITERAL: int = 106
    PDIGIT: int = 99
    PHASH: int = 102
    PHEX_LITERAL: int = 107
    PIDENTIFIER: int = 97
    PINTEGER_LITERAL: int = 105
    PLETTER: int = 98
    POCTAL_LITERAL: int = 108
    POPEN: int = 100
    PRAGMA: int = 38
    PRAGMALINE: int = 3
    PROTOCOL: int = 71
    PSTRING_LITERAL: int = 109
    PTR32: int = 57
    PTR64: int = 56
    QUOTE_C: int = 28
    READABLETO: int = 39
    REGISTER: int = 19
    RESTRICT: int = 44
    RETURN: int = 26
    SHORT: int = 48
    SIGNED: int = 31
    SIZEOF: int = 24
    STATIC: int = 30
    STDCALL: int = 40
    STRING_LITERAL: int = 16
    STRUCT: int = 29
    SWITCH: int = 25
    TYPEDEF: int = 21
    UNION: int = 34
    UNSIGNED: int = 20
    VOID: int = 62
    VOLATILE: int = 18
    W64: int = 58
    WCHAR: int = 59
    WHILE: int = 32
    tokenImage: List[unicode] = array(java.lang.String, [u'<EOF>', u'" "', u'"\\f"', u'"\\t"', u'"\\n"', u'"\\r"', u'"\\\\"', u'<token of kind 7>', u'<token of kind 8>', u'<INTEGER_LITERAL>', u'<DECIMAL_LITERAL>', u'<HEX_LITERAL>', u'<OCTAL_LITERAL>', u'<FLOATING_POINT_LITERAL>', u'<EXPONENT>', u'<CHARACTER_LITERAL>', u'<STRING_LITERAL>', u'"continue"', u'<VOLATILE>', u'"register"', u'"unsigned"', u'"typedef"', u'"default"', u'"double"', u'"sizeof"', u'"switch"', u'"return"', u'"extern"', u'"\\"C\\""', u'"struct"', u'"static"', u'<SIGNED>', u'"while"', u'"break"', u'"union"', u'<CONST>', u'<CDECL>', u'"__declspec"', u'<PRAGMA>', u'"__readableTo"', u'<STDCALL>', u'<FASTCALL>', u'<ATTRIBUTE>', u'<EXTENSION>', u'<RESTRICT>', u'<ASM>', u'<INLINE>', u'"float"', u'"short"', u'"else"', u'"case"', u'"long"', u'"__int8"', u'"__int16"', u'"__int32"', u'"__int64"', u'"__ptr64"', u'"__ptr32"', u'"__w64"', u'"wchar_t"', u'"enum"', u'"auto"', u'"void"', u'"char"', u'"goto"', u'"near"', u'"far"', u'"for"', u'"int"', u'"if"', u'"do"', u'"@protocol"', u'"@interface"', u'"#line"', u'<LINEALT>', u'<IDENTIFIER>', u'<LETTER>', u'<DIGIT>', u'" "', u'"\\t"', u'<ASMBLOCKB>', u'<ASMBLOCKP>', u'<ASM_SEMI>', u'" "', u'"\\f"', u'"\\t"', u'":"', u'<PATH_LITERAL>', u'<LINENUMBER_LITERAL>', u'" "', u'"\\f"', u'"\\t"', u'"\\n"', u'"\\r"', u'";"', u'<token of kind 95>', u'<token of kind 96>', u'<PIDENTIFIER>', u'<PLETTER>', u'<PDIGIT>', u'"("', u'")"', u'"#"', u'":"', u'","', u'<PINTEGER_LITERAL>', u'<PDECIMAL_LITERAL>', u'<PHEX_LITERAL>', u'<POCTAL_LITERAL>', u'<PSTRING_LITERAL>', u'" "', u'"\\f"', u'"\\t"', u'"\\n"', u'"\\r"', u'<OBJC_IGNORE>', u'<OBJC_IDENTIFIER>', u'<OBJC_LETTER>', u'<OBJC_DIGIT>', u'<OBJC_SEMI>', u'" "', u'"\\f"', u'"\\t"', u'"\\n"', u'"\\r"', u'"@private"', u'"@protected"', u'"@property"', u'"@optional"', u'"@required"', u'<OBJC2_IGNORE>', u'"@end"', u'";"', u'"("', u'")"', u'","', u'":"', u'"#"', u'"{"', u'"}"', u'"="', u'"["', u'"]"', u'"*"', u'"&"', u'"..."', u'"+"', u'"-"', u'"*="', u'"/="', u'"%="', u'"+="', u'"-="', u'"<<="', u'">>="', u'"&="', u'"^="', u'"|="', u'"?"', u'"||"', u'"&&"', u'"|"', u'"^"', u'"=="', u'"!="', u'"<"', u'">"', u'"<="', u'">="', u'"<<"', u'">>"', u'"/"', u'"%"', u'"++"', u'"--"', u'"~"', u'"!"', u'"."', u'"->"'])







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
