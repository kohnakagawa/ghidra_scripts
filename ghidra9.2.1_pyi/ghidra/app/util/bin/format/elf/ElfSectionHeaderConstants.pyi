import java.lang


class ElfSectionHeaderConstants(object):
    SHF_ALLOC: int = 2
    SHF_EXCLUDE: int = -2147483648
    SHF_EXECINSTR: int = 4
    SHF_GROUP: int = 512
    SHF_INFO_LINK: int = 64
    SHF_LINK_ORDER: int = 128
    SHF_MASKOS: int = 267386880
    SHF_MASKPROC: int = -268435456
    SHF_MERGE: int = 16
    SHF_OS_NONCONFORMING: int = 256
    SHF_STRINGS: int = 32
    SHF_TLS: int = 1024
    SHF_WRITE: int = 1
    SHN_ABS: int = -15
    SHN_COMMON: int = -14
    SHN_HIOS: int = -193
    SHN_HIPROC: int = -225
    SHN_HIRESERVE: int = -1
    SHN_LOOS: int = -224
    SHN_LOPROC: int = -256
    SHN_LORESERVE: int = -256
    SHN_UNDEF: int = 0
    SHN_XINDEX: int = -1
    SHT_ANDROID_REL: int = 1610612737
    SHT_ANDROID_RELA: int = 1610612738
    SHT_ANDROID_RELR: int = 1879047936
    SHT_CHECKSUM: int = 1879048184
    SHT_DYNAMIC: int = 6
    SHT_DYNSYM: int = 11
    SHT_FINI_ARRAY: int = 15
    SHT_GNU_ATTRIBUTES: int = 1879048181
    SHT_GNU_HASH: int = 1879048182
    SHT_GNU_LIBLIST: int = 1879048183
    SHT_GNU_verdef: int = 1879048189
    SHT_GNU_verneed: int = 1879048190
    SHT_GNU_versym: int = 1879048191
    SHT_GROUP: int = 17
    SHT_HASH: int = 5
    SHT_INIT_ARRAY: int = 14
    SHT_NOBITS: int = 8
    SHT_NOTE: int = 7
    SHT_NULL: int = 0
    SHT_PREINIT_ARRAY: int = 16
    SHT_PROGBITS: int = 1
    SHT_REL: int = 9
    SHT_RELA: int = 4
    SHT_RELR: int = 19
    SHT_SHLIB: int = 10
    SHT_STRTAB: int = 3
    SHT_SUNW_COMDAT: int = 1879048187
    SHT_SUNW_move: int = 1879048186
    SHT_SUNW_syminfo: int = 1879048188
    SHT_SYMTAB: int = 2
    SHT_SYMTAB_SHNDX: int = 18
    dot_bss: unicode = u'.bss'
    dot_comment: unicode = u'.comment'
    dot_data: unicode = u'.data'
    dot_data1: unicode = u'.data1'
    dot_debug: unicode = u'.debug'
    dot_dynamic: unicode = u'.dynamic'
    dot_dynstr: unicode = u'.dynstr'
    dot_dynsym: unicode = u'.dynsym'
    dot_fini: unicode = u'.fini'
    dot_got: unicode = u'.got'
    dot_hash: unicode = u'.hash'
    dot_init: unicode = u'.init'
    dot_interp: unicode = u'.interp'
    dot_line: unicode = u'.line'
    dot_note: unicode = u'.note'
    dot_plt: unicode = u'.plt'
    dot_rodata: unicode = u'.rodata'
    dot_rodata1: unicode = u'.rodata1'
    dot_shstrtab: unicode = u'.shstrtab'
    dot_strtab: unicode = u'.strtab'
    dot_symtab: unicode = u'.symtab'
    dot_tbss: unicode = u'.tbss'
    dot_tdata: unicode = u'.tdata'
    dot_tdata1: unicode = u'.tdata1'
    dot_text: unicode = u'.text'







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
