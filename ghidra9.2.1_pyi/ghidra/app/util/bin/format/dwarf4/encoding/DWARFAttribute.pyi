import java.lang


class DWARFAttribute(object):
    DW_AT_GNU_addr_base: int = 8499
    DW_AT_GNU_dwo_id: int = 8497
    DW_AT_GNU_dwo_name: int = 8496
    DW_AT_GNU_pubnames: int = 8500
    DW_AT_GNU_pubtypes: int = 8501
    DW_AT_GNU_ranges_base: int = 8498
    DW_AT_MIPS_linkage_name: int = 8199
    DW_AT_abstract_origin: int = 49
    DW_AT_accessibility: int = 50
    DW_AT_address_class: int = 51
    DW_AT_allocated: int = 78
    DW_AT_artificial: int = 52
    DW_AT_associated: int = 79
    DW_AT_base_types: int = 53
    DW_AT_binary_scale: int = 91
    DW_AT_bit_offset: int = 12
    DW_AT_bit_size: int = 13
    DW_AT_bit_stride: int = 46
    DW_AT_byte_size: int = 11
    DW_AT_byte_stride: int = 81
    DW_AT_call_column: int = 87
    DW_AT_call_file: int = 88
    DW_AT_call_line: int = 89
    DW_AT_calling_convention: int = 54
    DW_AT_common_reference: int = 26
    DW_AT_comp_dir: int = 27
    DW_AT_const_expr: int = 108
    DW_AT_const_value: int = 28
    DW_AT_containing_type: int = 29
    DW_AT_count: int = 55
    DW_AT_data_bit_offset: int = 107
    DW_AT_data_location: int = 80
    DW_AT_data_member_location: int = 56
    DW_AT_decimal_scale: int = 92
    DW_AT_decimal_sign: int = 94
    DW_AT_decl_column: int = 57
    DW_AT_decl_file: int = 58
    DW_AT_decl_line: int = 59
    DW_AT_declaration: int = 60
    DW_AT_default_value: int = 30
    DW_AT_description: int = 90
    DW_AT_digit_count: int = 95
    DW_AT_discr: int = 21
    DW_AT_discr_list: int = 61
    DW_AT_discr_value: int = 22
    DW_AT_elemental: int = 102
    DW_AT_encoding: int = 62
    DW_AT_endianity: int = 101
    DW_AT_entry_pc: int = 82
    DW_AT_enum_class: int = 109
    DW_AT_explicit: int = 99
    DW_AT_extension: int = 84
    DW_AT_external: int = 63
    DW_AT_frame_base: int = 64
    DW_AT_friend: int = 65
    DW_AT_hi_user: int = 16383
    DW_AT_high_pc: int = 18
    DW_AT_identifier_case: int = 66
    DW_AT_import: int = 24
    DW_AT_inline: int = 32
    DW_AT_is_optional: int = 33
    DW_AT_language: int = 19
    DW_AT_linkage_name: int = 110
    DW_AT_lo_user: int = 8192
    DW_AT_location: int = 2
    DW_AT_low_pc: int = 17
    DW_AT_lower_bound: int = 34
    DW_AT_macro_info: int = 67
    DW_AT_main_subprogram: int = 106
    DW_AT_mutable: int = 97
    DW_AT_name: int = 3
    DW_AT_namelist_item: int = 68
    DW_AT_object_pointer: int = 100
    DW_AT_ordering: int = 9
    DW_AT_picture_string: int = 96
    DW_AT_priority: int = 69
    DW_AT_producer: int = 37
    DW_AT_prototyped: int = 39
    DW_AT_pure: int = 103
    DW_AT_ranges: int = 85
    DW_AT_recursive: int = 104
    DW_AT_return_addr: int = 42
    DW_AT_segment: int = 70
    DW_AT_sibling: int = 1
    DW_AT_signature: int = 105
    DW_AT_small: int = 93
    DW_AT_specification: int = 71
    DW_AT_start_scope: int = 44
    DW_AT_static_link: int = 72
    DW_AT_stmt_list: int = 16
    DW_AT_string_length: int = 25
    DW_AT_threads_scaled: int = 98
    DW_AT_trampoline: int = 86
    DW_AT_type: int = 73
    DW_AT_upper_bound: int = 47
    DW_AT_use_UTF8: int = 83
    DW_AT_use_location: int = 74
    DW_AT_variable_parameter: int = 75
    DW_AT_virtuality: int = 76
    DW_AT_visibility: int = 23
    DW_AT_vtable_elem_location: int = 77



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def toString(value: long) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
