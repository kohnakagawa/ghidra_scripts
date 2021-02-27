import java.lang


class DWARFTag(object):
    """
    DWARF uses a series of debugging information entries to define a
     low-level representation of a source program. Each debugging
     information entry is described by an identifying tag and
     contains a series of attributes. The tag specifies the class
     to which an entry belongs, and the attributes define the
     specific characteristics of the entry.

     The debugging information entries in DWARF Version 2, 3, and 4 are
     intended to exist in the .debug_info section of an object file.

     The set of required tag names is listed below.
    """

    DW_TAG_access_declaration: int = 35
    DW_TAG_array_type: int = 1
    DW_TAG_base_type: int = 36
    DW_TAG_call_site: int = 72
    DW_TAG_call_site_parameter: int = 73
    DW_TAG_catch_block: int = 37
    DW_TAG_class_type: int = 2
    DW_TAG_common_block: int = 26
    DW_TAG_common_inclusion: int = 27
    DW_TAG_compile_unit: int = 17
    DW_TAG_condition: int = 63
    DW_TAG_const_type: int = 38
    DW_TAG_constant: int = 39
    DW_TAG_dwarf_procedure: int = 54
    DW_TAG_entry_point: int = 3
    DW_TAG_enumeration_type: int = 4
    DW_TAG_enumerator: int = 40
    DW_TAG_file_type: int = 41
    DW_TAG_formal_parameter: int = 5
    DW_TAG_friend: int = 42
    DW_TAG_gnu_call_site: int = 16649
    DW_TAG_gnu_call_site_parameter: int = 16650
    DW_TAG_hi_user: int = 65535
    DW_TAG_imported_declaration: int = 8
    DW_TAG_imported_module: int = 58
    DW_TAG_imported_unit: int = 61
    DW_TAG_inheritance: int = 28
    DW_TAG_inlined_subroutine: int = 29
    DW_TAG_interface_type: int = 56
    DW_TAG_label: int = 10
    DW_TAG_lexical_block: int = 11
    DW_TAG_lo_user: int = 16512
    DW_TAG_member: int = 13
    DW_TAG_module: int = 30
    DW_TAG_mutable_type: int = 62
    DW_TAG_namelist: int = 43
    DW_TAG_namelist_item: int = 44
    DW_TAG_namespace: int = 57
    DW_TAG_packed_type: int = 45
    DW_TAG_partial_unit: int = 60
    DW_TAG_pointer_type: int = 15
    DW_TAG_ptr_to_member_type: int = 31
    DW_TAG_reference_type: int = 16
    DW_TAG_restrict_type: int = 55
    DW_TAG_rvalue_reference_type: int = 66
    DW_TAG_set_type: int = 32
    DW_TAG_shared_type: int = 64
    DW_TAG_string_type: int = 18
    DW_TAG_structure_type: int = 19
    DW_TAG_subprogram: int = 46
    DW_TAG_subrange_type: int = 33
    DW_TAG_subroutine_type: int = 21
    DW_TAG_template_alias: int = 67
    DW_TAG_template_type_param: int = 47
    DW_TAG_template_value_param: int = 48
    DW_TAG_thrown_type: int = 49
    DW_TAG_try_block: int = 50
    DW_TAG_type_unit: int = 65
    DW_TAG_typedef: int = 22
    DW_TAG_union_type: int = 23
    DW_TAG_unspecified_parameters: int = 24
    DW_TAG_unspecified_type: int = 59
    DW_TAG_variable: int = 52
    DW_TAG_variant: int = 25
    DW_TAG_variant_part: int = 51
    DW_TAG_volatile_type: int = 53
    DW_TAG_with_stmt: int = 34



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
