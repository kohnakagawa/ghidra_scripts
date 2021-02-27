import java.lang


class SectionNames(object):
    DATA: unicode = u'__data'
    DATA_CONST: unicode = u'__const'
    DATA_DYLD: unicode = u'__dyld'
    DATA_LA_SYMBOL_PTR: unicode = u'__la_symbol_ptr'
    DATA_MOD_INIT_FUNC: unicode = u'__mod_init_func'
    DATA_MOD_TERM_FUNC: unicode = u'__mod_term_func'
    DATA_NL_SYMBOL_PTR: unicode = u'__nl_symbol_ptr'
    IMPORT_JUMP_TABLE: unicode = u'__jump_table'
    IMPORT_POINTERS: unicode = u'__pointers'
    OBJC_MODULES: unicode = u'__module_info'
    OBJC_REFS: unicode = u'__selector_refs'
    OBJC_STRINGS: unicode = u'__selector_strs'
    OBJC_SYMBOLS: unicode = u'__symbol_table'
    PROGRAM_VARS: unicode = u'__program_vars'
    SECT_BSS: unicode = u'__bss'
    SECT_COMMON: unicode = u'__common'
    SECT_GOT: unicode = u'__got'
    TEXT: unicode = u'__text'
    TEXT_CONST: unicode = u'__const'
    TEXT_CSTRING: unicode = u'__cstring'
    TEXT_FVMLIB_INIT0: unicode = u'__fvmlib_init0'
    TEXT_FVMLIB_INIT1: unicode = u'__fvmlib_init1'
    TEXT_LITERAL4: unicode = u'__literal4'
    TEXT_LITERAL8: unicode = u'__literal8'
    TEXT_PICSYMBOL_STUB: unicode = u'__picsymbol_stub'
    TEXT_SYMBOL_STUB: unicode = u'__symbol_stub'



    def __init__(self): ...



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
