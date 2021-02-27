import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.elf
import ghidra.app.util.bin.format.elf.extend
import ghidra.program.model.address
import ghidra.util.task
import java.io
import java.lang
import java.util


class MIPS_ElfExtension(ghidra.app.util.bin.format.elf.extend.ElfExtension):
    DT_MIPS_AUX_DYNAMIC: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_AUX_DYNAMIC(0x70000031)
    DT_MIPS_BASE_ADDRESS: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_BASE_ADDRESS(0x70000006)
    DT_MIPS_COMPACT_SIZE: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_COMPACT_SIZE(0x7000002f)
    DT_MIPS_CONFLICT: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_CONFLICT(0x70000008)
    DT_MIPS_CONFLICTNO: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_CONFLICTNO(0x7000000b)
    DT_MIPS_CXX_FLAGS: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_CXX_FLAGS(0x70000022)
    DT_MIPS_DELTA_CLASS: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_DELTA_CLASS(0x70000017)
    DT_MIPS_DELTA_CLASSSYM: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_DELTA_CLASSSYM(0x70000020)
    DT_MIPS_DELTA_CLASSSYM_NO: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_DELTA_CLASSSYM_NO(0x70000021)
    DT_MIPS_DELTA_CLASS_NO: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_DELTA_CLASS_NO(0x70000018)
    DT_MIPS_DELTA_INSTANCE: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_DELTA_INSTANCE(0x70000019)
    DT_MIPS_DELTA_INSTANCE_NO: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_DELTA_INSTANCE_NO(0x7000001a)
    DT_MIPS_DELTA_RELOC: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_DELTA_RELOC(0x7000001b)
    DT_MIPS_DELTA_RELOC_NO: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_DELTA_RELOC_NO(0x7000001c)
    DT_MIPS_DELTA_SYM: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_DELTA_SYM(0x7000001d)
    DT_MIPS_DELTA_SYM_NO: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_DELTA_SYM_NO(0x7000001e)
    DT_MIPS_DYNSTR_ALIGN: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_DYNSTR_ALIGN(0x7000002b)
    DT_MIPS_FLAGS: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_FLAGS(0x70000005)
    DT_MIPS_GOTSYM: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_GOTSYM(0x70000013)
    DT_MIPS_GP_VALUE: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_GP_VALUE(0x70000030)
    DT_MIPS_HIDDEN_GOTIDX: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_HIDDEN_GOTIDX(0x70000027)
    DT_MIPS_HIPAGENO: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_HIPAGENO(0x70000014)
    DT_MIPS_ICHECKSUM: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_ICHECKSUM(0x70000003)
    DT_MIPS_INTERFACE: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_INTERFACE(0x7000002a)
    DT_MIPS_INTERFACE_SIZE: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_INTERFACE_SIZE(0x7000002c)
    DT_MIPS_IVERSION: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_IVERSION(0x70000004)
    DT_MIPS_LIBLIST: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_LIBLIST(0x70000009)
    DT_MIPS_LIBLISTNO: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_LIBLISTNO(0x70000010)
    DT_MIPS_LOCALPAGE_GOTIDX: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_LOCALPAGE_GOTIDX(0x70000025)
    DT_MIPS_LOCAL_GOTIDX: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_LOCAL_GOTIDX(0x70000026)
    DT_MIPS_LOCAL_GOTNO: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_LOCAL_GOTNO(0x7000000a)
    DT_MIPS_MSYM: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_MSYM(0x70000007)
    DT_MIPS_OPTIONS: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_OPTIONS(0x70000029)
    DT_MIPS_PERF_SUFFIX: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_PERF_SUFFIX(0x7000002e)
    DT_MIPS_PIXIE_INIT: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_PIXIE_INIT(0x70000023)
    DT_MIPS_PLTGOT: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_PLTGOT(0x70000032)
    DT_MIPS_PROTECTED_GOTIDX: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_PROTECTED_GOTIDX(0x70000028)
    DT_MIPS_RLD_MAP: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_RLD_MAP(0x70000016)
    DT_MIPS_RLD_MAP_REL: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_RLD_MAP_REL(0x70000035)
    DT_MIPS_RLD_TEXT_RESOLVE_ADDR: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_RLD_TEXT_RESOLVE_ADDR(0x7000002d)
    DT_MIPS_RLD_VERSION: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_RLD_VERSION(0x70000001)
    DT_MIPS_RWPLT: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_RWPLT(0x70000034)
    DT_MIPS_SYMBOL_LIB: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_SYMBOL_LIB(0x70000024)
    DT_MIPS_SYMTABNO: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_SYMTABNO(0x70000011)
    DT_MIPS_TIME_STAMP: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_TIME_STAMP(0x70000002)
    DT_MIPS_UNREFEXTNO: ghidra.app.util.bin.format.elf.ElfDynamicType = DT_MIPS_UNREFEXTNO(0x70000012)
    MIPS_GP0_VALUE_SYMBOL: unicode = u'_mips_gp0_value'
    MIPS_GP_DISP_SYMBOL_NAME: unicode = u'_gp_disp'
    MIPS_GP_GNU_LOCAL_SYMBOL_NAME: unicode = u'__gnu_local_gp'
    MIPS_GP_VALUE_SYMBOL: unicode = u'_mips_gp_value'
    ODK_EXCEPTIONS: int = 2
    ODK_FILL: int = 5
    ODK_GP_GROUP: int = 9
    ODK_HWAND: int = 7
    ODK_HWOR: int = 8
    ODK_HWPATCH: int = 4
    ODK_IDENT: int = 10
    ODK_NULL: int = 0
    ODK_PAD: int = 3
    ODK_PAGESIZE: int = 11
    ODK_REGINFO: int = 1
    ODK_TAGS: int = 6
    PT_MIPS_ABIFLAGS: ghidra.app.util.bin.format.elf.ElfProgramHeaderType = PT_MIPS_ABIFLAGS(0x70000003)
    PT_MIPS_OPTIONS: ghidra.app.util.bin.format.elf.ElfProgramHeaderType = PT_MIPS_OPTIONS(0x70000002)
    PT_MIPS_REGINFO: ghidra.app.util.bin.format.elf.ElfProgramHeaderType = PT_MIPS_REGINFO(0x70000000)
    PT_MIPS_RTPROC: ghidra.app.util.bin.format.elf.ElfProgramHeaderType = PT_MIPS_RTPROC(0x70000001)
    SHT_MIPS_ABIFLAGS: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_ABIFLAGS(0x7000002a)
    SHT_MIPS_AUXSYM: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_AUXSYM(0x70000016)
    SHT_MIPS_CONFLICT: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_CONFLICT(0x70000002)
    SHT_MIPS_CONTENT: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_CONTENT(0x7000000c)
    SHT_MIPS_DEBUG: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_DEBUG(0x70000005)
    SHT_MIPS_DELTACLASS: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_DELTACLASS(0x7000001d)
    SHT_MIPS_DELTADECL: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_DELTADECL(0x7000001f)
    SHT_MIPS_DELTAINST: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_DELTAINST(0x7000001c)
    SHT_MIPS_DELTASYM: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_DELTASYM(0x7000001b)
    SHT_MIPS_DENSE: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_DENSE(0x70000013)
    SHT_MIPS_DWARF: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_DWARF(0x7000001e)
    SHT_MIPS_EH_REGION: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_EH_REGION(0x70000027)
    SHT_MIPS_EVENTS: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_EVENTS(0x70000021)
    SHT_MIPS_EXTSYM: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_EXTSYM(0x70000012)
    SHT_MIPS_FDESC: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_FDESC(0x70000011)
    SHT_MIPS_GPTAB: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_GPTAB(0x70000003)
    SHT_MIPS_IFACE: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = (0x7000000b)
    SHT_MIPS_LIBLIST: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_LIBLIST(0x70000000)
    SHT_MIPS_LINE: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_LINE(0x70000019)
    SHT_MIPS_LOCSTR: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_LOCSTR(0x70000018)
    SHT_MIPS_LOCSYM: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_LOCSYM(0x70000015)
    SHT_MIPS_MSYM: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_MSYM(0x70000001)
    SHT_MIPS_OPTIONS: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_OPTIONS(0x7000000d)
    SHT_MIPS_OPTSYM: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_OPTSYM(0x70000017)
    SHT_MIPS_PACKAGE: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_PACKAGE(0x70000007)
    SHT_MIPS_PACKSYM: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_PACKSYM(0x70000008)
    SHT_MIPS_PDESC: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_PDESC(0x70000014)
    SHT_MIPS_PDR_EXCEPTION: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_PDR_EXCEPTION(0x70000029)
    SHT_MIPS_PIXIE: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_PIXIE(0x70000023)
    SHT_MIPS_REGINFO: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_REGINFO(0x70000006)
    SHT_MIPS_RELD: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_RELD(0x70000009)
    SHT_MIPS_RFDESC: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_RFDESC(0x7000001a)
    SHT_MIPS_SHDR: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_SHDR(0x70000010)
    SHT_MIPS_SYMBOL_LIB: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_SYMBOL_LIB(0x70000020)
    SHT_MIPS_TRANSLATE: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_TRANSLATE(0x70000022)
    SHT_MIPS_UCODE: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_UCODE(0x70000004)
    SHT_MIPS_WHIRL: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_WHIRL(0x70000026)
    SHT_MIPS_XLATE: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_XLATE(0x70000024)
    SHT_MIPS_XLATE_DEBUG: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_XLATE_DEBUG(0x70000025)
    SHT_MIPS_XLATE_OLD: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_MIPS_XLATE_OLD(0x70000028)
    STO_MIPS_MICROMIPS: int = 128
    STO_MIPS_MIPS16: int = 240
    STO_MIPS_OPTIONAL: int = 4
    STO_MIPS_PIC: int = 32
    STO_MIPS_PLT: int = 8



    def __init__(self): ...



    def addDynamicTypes(self, __a0: java.util.Map) -> None: ...

    def addProgramHeaderTypes(self, __a0: java.util.Map) -> None: ...

    def addSectionHeaderTypes(self, __a0: java.util.HashMap) -> None: ...

    @overload
    def canHandle(self, __a0: ghidra.app.util.bin.format.elf.ElfHeader) -> bool: ...

    @overload
    def canHandle(self, __a0: ghidra.app.util.bin.format.elf.ElfLoadHelper) -> bool: ...

    def creatingFunction(self, __a0: ghidra.app.util.bin.format.elf.ElfLoadHelper, __a1: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address: ...

    def equals(self, __a0: object) -> bool: ...

    def evaluateElfSymbol(self, __a0: ghidra.app.util.bin.format.elf.ElfLoadHelper, __a1: ghidra.app.util.bin.format.elf.ElfSymbol, __a2: ghidra.program.model.address.Address, __a3: bool) -> ghidra.program.model.address.Address: ...

    def getAdjustedLoadSize(self, __a0: ghidra.app.util.bin.format.elf.ElfProgramHeader) -> long: ...

    def getAdjustedMemoryOffset(self, __a0: long, __a1: ghidra.program.model.address.AddressSpace) -> long: ...

    def getAdjustedMemorySize(self, __a0: ghidra.app.util.bin.format.elf.ElfProgramHeader) -> long: ...

    def getAdjustedSize(self, __a0: ghidra.app.util.bin.format.elf.ElfSectionHeader) -> long: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataTypeSuffix(self) -> unicode: ...

    def getDefaultAlignment(self, __a0: ghidra.app.util.bin.format.elf.ElfLoadHelper) -> int: ...

    def getExternalBlockReserveSize(self) -> int: ...

    def getFilteredLoadInputStream(self, __a0: ghidra.app.util.bin.format.elf.ElfLoadHelper, __a1: ghidra.app.util.bin.format.MemoryLoadable, __a2: ghidra.program.model.address.Address, __a3: long, __a4: java.io.InputStream) -> java.io.InputStream: ...

    def getLinkageBlockAlignment(self) -> int: ...

    def getPreferredExternalBlockSize(self) -> int: ...

    def getPreferredSectionAddress(self, __a0: ghidra.app.util.bin.format.elf.ElfLoadHelper, __a1: ghidra.app.util.bin.format.elf.ElfSectionHeader) -> ghidra.program.model.address.Address: ...

    def getPreferredSectionAddressSpace(self, __a0: ghidra.app.util.bin.format.elf.ElfLoadHelper, __a1: ghidra.app.util.bin.format.elf.ElfSectionHeader) -> ghidra.program.model.address.AddressSpace: ...

    def getPreferredSegmentAddress(self, __a0: ghidra.app.util.bin.format.elf.ElfLoadHelper, __a1: ghidra.app.util.bin.format.elf.ElfProgramHeader) -> ghidra.program.model.address.Address: ...

    def getPreferredSegmentAddressSpace(self, __a0: ghidra.app.util.bin.format.elf.ElfLoadHelper, __a1: ghidra.app.util.bin.format.elf.ElfProgramHeader) -> ghidra.program.model.address.AddressSpace: ...

    def getRelocationClass(self, __a0: ghidra.app.util.bin.format.elf.ElfHeader) -> java.lang.Class: ...

    def hasFilteredLoadInputStream(self, __a0: ghidra.app.util.bin.format.elf.ElfLoadHelper, __a1: ghidra.app.util.bin.format.MemoryLoadable, __a2: ghidra.program.model.address.Address) -> bool: ...

    def hashCode(self) -> int: ...

    def isSectionAllocated(self, __a0: ghidra.app.util.bin.format.elf.ElfSectionHeader) -> bool: ...

    def isSectionExecutable(self, __a0: ghidra.app.util.bin.format.elf.ElfSectionHeader) -> bool: ...

    def isSectionWritable(self, __a0: ghidra.app.util.bin.format.elf.ElfSectionHeader) -> bool: ...

    def isSegmentExecutable(self, __a0: ghidra.app.util.bin.format.elf.ElfProgramHeader) -> bool: ...

    def isSegmentReadable(self, __a0: ghidra.app.util.bin.format.elf.ElfProgramHeader) -> bool: ...

    def isSegmentWritable(self, __a0: ghidra.app.util.bin.format.elf.ElfProgramHeader) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def processElf(self, __a0: ghidra.app.util.bin.format.elf.ElfLoadHelper, __a1: ghidra.util.task.TaskMonitor) -> None: ...

    def processGotPlt(self, __a0: ghidra.app.util.bin.format.elf.ElfLoadHelper, __a1: ghidra.util.task.TaskMonitor) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def dataTypeSuffix(self) -> unicode: ...
