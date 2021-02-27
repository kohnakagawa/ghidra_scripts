from typing import List
import ghidra.app.util.bin.format.dwarf4.encoding
import java.lang


class DWARFForm(java.lang.Enum):
    DW_FORM_addr: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm = DW_FORM_addr
    DW_FORM_block: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm = DW_FORM_block
    DW_FORM_block1: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm = DW_FORM_block1
    DW_FORM_block2: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm = DW_FORM_block2
    DW_FORM_block4: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm = DW_FORM_block4
    DW_FORM_data1: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm = DW_FORM_data1
    DW_FORM_data2: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm = DW_FORM_data2
    DW_FORM_data4: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm = DW_FORM_data4
    DW_FORM_data8: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm = DW_FORM_data8
    DW_FORM_exprloc: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm = DW_FORM_exprloc
    DW_FORM_flag: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm = DW_FORM_flag
    DW_FORM_flag_present: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm = DW_FORM_flag_present
    DW_FORM_indirect: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm = DW_FORM_indirect
    DW_FORM_ref1: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm = DW_FORM_ref1
    DW_FORM_ref2: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm = DW_FORM_ref2
    DW_FORM_ref4: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm = DW_FORM_ref4
    DW_FORM_ref8: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm = DW_FORM_ref8
    DW_FORM_ref_addr: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm = DW_FORM_ref_addr
    DW_FORM_ref_sig8: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm = DW_FORM_ref_sig8
    DW_FORM_ref_udata: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm = DW_FORM_ref_udata
    DW_FORM_sdata: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm = DW_FORM_sdata
    DW_FORM_sec_offset: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm = DW_FORM_sec_offset
    DW_FORM_string: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm = DW_FORM_string
    DW_FORM_strp: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm = DW_FORM_strp
    DW_FORM_udata: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm = DW_FORM_udata
    NULL: ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm = NULL







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def find(__a0: int) -> ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def getValue(self) -> int: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.dwarf4.encoding.DWARFForm]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def value(self) -> int: ...
