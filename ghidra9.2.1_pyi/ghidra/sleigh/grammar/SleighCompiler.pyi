from typing import List
import generic.stl
import ghidra.pcodeCPort.semantics
import ghidra.pcodeCPort.slgh_compile
import ghidra.pcodeCPort.slghpatexpress
import ghidra.pcodeCPort.slghsymbol
import ghidra.sleigh.grammar
import ghidra.sleigh.grammar.SleighCompiler
import java.lang
import org.antlr.runtime
import org.antlr.runtime.tree


class SleighCompiler(org.antlr.runtime.tree.TreeParser):
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
    FOLLOW_OP_ADDRESS_OF_in_varnode5104: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_ADDRESS_OF_in_varnode5125: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_ADD_in_expr4622: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_ADD_in_pexpression22536: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_ADD_in_pexpression2290: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_ALIGNMENT_in_aligndef215: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_AND_in_expr4238: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_AND_in_pexpression2233: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_AND_in_pexpression22479: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_APPLY_in_cstatement2821: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_APPLY_in_expr_apply4989: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_APPLY_in_expr_apply5014: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_ARGUMENTS_in_arguments1420: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_ASSIGN_in_assignment3305: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_ASSIGN_in_assignment3337: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_ASSIGN_in_assignment3367: org.antlr.runtime.BitSet = {108}
    FOLLOW_OP_ASSIGN_in_assignment3397: org.antlr.runtime.BitSet = {139,204}
    FOLLOW_OP_ASSIGN_in_assignment3417: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_ASSIGN_in_assignment3438: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_ASSIGN_in_assignment3457: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_ASSIGN_in_cstatement2800: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_BIG_in_endian131: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_BIN_CONSTANT_in_integer5229: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_BITRANGE2_in_expr4953: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_BITRANGES_in_bitrangedef1022: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_BITRANGE_in_assignment3308: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_BITRANGE_in_bitrange3486: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_BITRANGE_in_sbitrange1038: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_BIT_PATTERN_in_bitpattern1637: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_BOOL_AND_in_expr4180: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_BOOL_AND_in_pequation1923: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_BOOL_OR_in_expr4142: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_BOOL_OR_in_pequation1885: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_BOOL_XOR_in_expr4161: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_BUILD_in_build_stmt3755: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_CALL_in_call_stmt4044: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_CONCATENATE_in_printpiece1793: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_CONSTRUCTOR_in_constructor1563: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_CONTEXT_BLOCK_in_contextblock2751: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_CONTEXT_in_contextdef710: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_CROSSBUILD_in_crossbuild_stmt3787: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_CTLIST_in_constructorlikelist1538: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_DECLARATIVE_SIZE_in_assignment3340: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_DECLARATIVE_SIZE_in_assignment3370: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_DEC_CONSTANT_in_integer5216: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_DEC_in_fieldmod418: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_DEFAULT_in_spacemod799: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_DEREFERENCE_in_sizedstar3532: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_DEREFERENCE_in_sizedstar3556: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_DEREFERENCE_in_sizedstar3576: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_DEREFERENCE_in_sizedstar3595: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_DEREFERENCE_in_sizedstarv3632: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_DEREFERENCE_in_sizedstarv3657: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_DEREFERENCE_in_sizedstarv3678: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_DEREFERENCE_in_sizedstarv3698: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_DISPLAY_in_display1733: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_DIV_in_expr4718: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_DIV_in_pexpression22593: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_DIV_in_pexpression2347: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_ELLIPSIS_RIGHT_in_pequation1958: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_ELLIPSIS_in_pequation1943: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_EMPTY_LIST_in_arguments1439: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_ENDIAN_in_endiandef109: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_EQUAL_in_expr4258: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_EQUAL_in_pequation1974: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_EXPORT_in_export4102: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_EXPORT_in_export4117: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_FADD_in_expr4660: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_FDIV_in_expr4813: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_FEQUAL_in_expr4296: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_FGREATEQUAL_in_expr4506: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_FGREAT_in_expr4544: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_FIELDDEFS_in_fielddefs297: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_FIELDDEF_in_fielddef325: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_FIELD_MODS_in_fieldmods357: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_FLESSEQUAL_in_expr4525: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_FLESS_in_expr4487: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_FMULT_in_expr4794: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_FNEGATE_in_expr4878: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_FNOTEQUAL_in_expr4315: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_FSUB_in_expr4679: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_GOTO_in_cond_stmt3999: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_GOTO_in_goto_stmt3835: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_GREATEQUAL_in_expr4354: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_GREATEQUAL_in_pequation2074: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_GREAT_in_expr4392: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_GREAT_in_pequation2054: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_HEX_CONSTANT_in_integer5203: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_HEX_in_fieldmod406: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_IDENTIFIER_LIST_in_identifierlist919: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_LIST_in_valuelist1275: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_LIST_in_varlist1311: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_arguments1424: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_assignment3420: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_cstatement2803: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_cstatement2824: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_cstatement2832: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_cstatement2840: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_ctorstart1677: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_expr_apply4994: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_family_or_operand_symbol2128: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_family_symbol671: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_identifier5171: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_identifierlist927: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_jump_symbol3860: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_label3188: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_operand_symbol572: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_pattern_symbol22719: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_pattern_symbol2686: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_pequation_symbol2161: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_printpiece1772: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_sbitrange1041: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_section_label3228: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_section_symbol3265: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_space_symbol605: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_specific_identifier440: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_specific_symbol638: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_unbound_identifier473: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_value_symbol539: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IDENTIFIER_in_varnode_symbol506: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_IF_in_cond_stmt3992: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_INTBLIST_in_intblist1133: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_INVERT_in_expr4848: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_INVERT_in_pexpression22628: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_INVERT_in_pexpression2382: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_JUMPDEST_ABSOLUTE_in_jumpdest3926: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_JUMPDEST_DYNAMIC_in_jumpdest3911: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_JUMPDEST_LABEL_in_jumpdest3961: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_JUMPDEST_RELATIVE_in_jumpdest3941: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_JUMPDEST_SYMBOL_in_jumpdest3895: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_LABEL_in_label3184: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_LEFT_in_expr4564: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_LEFT_in_pexpression22498: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_LEFT_in_pexpression2252: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_LESSEQUAL_in_expr4373: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_LESSEQUAL_in_pequation2034: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_LESS_in_expr4335: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_LESS_in_pequation2014: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_LITTLE_in_endian141: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_LOCAL_in_assignment3363: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_LOCAL_in_assignment3393: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_LOCAL_in_declaration3142: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_LOCAL_in_declaration3160: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_MACRO_in_macrodef1373: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_MULT_in_expr4699: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_MULT_in_pexpression22574: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_MULT_in_pexpression2328: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_NAMES_in_nameattach1203: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_NEGATE_in_expr4863: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_NEGATE_in_intbpart1169: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_NEGATE_in_pexpression22613: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_NEGATE_in_pexpression2367: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_NIL_in_bitpat_or_nil1524: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_NIL_in_id_or_nil1498: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_NOFLOW_in_fieldmod394: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_NOP_in_code_block2944: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_NOTEQUAL_in_expr4277: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_NOTEQUAL_in_pequation1994: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_NOT_in_expr4833: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_NO_CONTEXT_BLOCK_in_contextblock2763: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_NO_FIELD_MOD_in_fieldmods366: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_OR_in_expr4200: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_OR_in_pexpression2195: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_OR_in_pexpression22441: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_PARENTHESIZED_in_expr4937: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_PARENTHESIZED_in_pequation2103: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_PARENTHESIZED_in_pexpression22662: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_PARENTHESIZED_in_pexpression2416: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_PCODEOP_in_pcodeopdef1074: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_PCODE_in_ctorsemantic1602: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_PCODE_in_ctorsemantic1616: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_QSTRING_in_qstring5148: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_QSTRING_in_string1854: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_REM_in_expr4737: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_RETURN_in_return_stmt4076: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_RIGHT_in_expr4583: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_RIGHT_in_pexpression22517: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_RIGHT_in_pexpression2271: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_SDIV_in_expr4756: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_SECTION_LABEL_in_section_label3224: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_SEMANTIC_in_semantic2884: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_SEQUENCE_in_pequation1904: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_SGREATEQUAL_in_expr4430: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_SGREAT_in_expr4468: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_SIGNED_in_fieldmod382: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_SIZE_in_sizemod833: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_SIZING_SIZE_in_varnode5107: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_SLESSEQUAL_in_expr4449: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_SLESS_in_expr4411: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_SPACEMODS_in_spacemods769: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_SPACE_in_spacedef743: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_SREM_in_expr4775: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_SRIGHT_in_expr4602: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_STRING_OR_IDENT_LIST_in_stringoridentlist971: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_STRING_in_string1841: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_SUBTABLE_in_ctorstart1673: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_SUB_in_expr4641: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_SUB_in_pexpression22555: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_SUB_in_pexpression2309: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_TABLE_in_ctorstart1710: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_TOKEN_ENDIAN_in_tokendef267: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_TOKEN_in_tokendef245: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_TRUNCATION_SIZE_in_varnode5087: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_TYPE_in_typemod813: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_UNIMPL_in_ctorsemantic1618: org.antlr.runtime.BitSet = {3}
    FOLLOW_OP_VALUES_in_valueattach1099: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_VARIABLES_in_varattach1233: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_VARNODE_in_varnodedef871: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_WHITESPACE_in_whitespace1818: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_WILDCARD_in_assignment3442: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_OP_WILDCARD_in_ctorstart1691: org.antlr.runtime.BitSet = {112}
    FOLLOW_OP_WILDCARD_in_expr_apply5018: org.antlr.runtime.BitSet = {3,83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_OP_WILDCARD_in_family_or_operand_symbol2142: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_WILDCARD_in_family_symbol685: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_WILDCARD_in_identifier5185: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_WILDCARD_in_identifierlist943: org.antlr.runtime.BitSet = {3,139,204}
    FOLLOW_OP_WILDCARD_in_intbpart1161: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_WILDCARD_in_jump_symbol3874: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_WILDCARD_in_label3204: org.antlr.runtime.BitSet = {3}
    FOLLOW_OP_WILDCARD_in_operand_symbol586: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_WILDCARD_in_pattern_symbol22733: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_WILDCARD_in_pattern_symbol2700: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_WILDCARD_in_pequation_symbol2175: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_WILDCARD_in_section_label3244: org.antlr.runtime.BitSet = {3}
    FOLLOW_OP_WILDCARD_in_section_symbol3279: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_WILDCARD_in_space_symbol619: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_WILDCARD_in_specific_identifier454: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_WILDCARD_in_specific_symbol652: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_WILDCARD_in_unbound_identifier487: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_WILDCARD_in_value_symbol553: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_WILDCARD_in_varnode_symbol520: org.antlr.runtime.BitSet = {1}
    FOLLOW_OP_WITH_in_withblock1451: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_WORDSIZE_in_wordsizemod852: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_XOR_in_expr4219: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_XOR_in_pexpression2214: org.antlr.runtime.BitSet = {2}
    FOLLOW_OP_XOR_in_pexpression22460: org.antlr.runtime.BitSet = {2}
    FOLLOW_aligndef_in_definition155: org.antlr.runtime.BitSet = {1}
    FOLLOW_arguments_in_macrodef1382: org.antlr.runtime.BitSet = {177}
    FOLLOW_assignment_in_statement2987: org.antlr.runtime.BitSet = {1}
    FOLLOW_bitpat_or_nil_in_withblock1459: org.antlr.runtime.BitSet = {104,165}
    FOLLOW_bitpattern_in_bitpat_or_nil1517: org.antlr.runtime.BitSet = {1}
    FOLLOW_bitpattern_in_constructor1571: org.antlr.runtime.BitSet = {104,165}
    FOLLOW_bitrange_in_expr4920: org.antlr.runtime.BitSet = {1}
    FOLLOW_bitrangedef_in_definition180: org.antlr.runtime.BitSet = {1}
    FOLLOW_build_stmt_in_statement3028: org.antlr.runtime.BitSet = {1}
    FOLLOW_call_stmt_in_statement3081: org.antlr.runtime.BitSet = {1}
    FOLLOW_code_block_in_semantic2888: org.antlr.runtime.BitSet = {3}
    FOLLOW_cond_stmt_in_statement3066: org.antlr.runtime.BitSet = {1}
    FOLLOW_constructor_in_constructorlike1348: org.antlr.runtime.BitSet = {1}
    FOLLOW_constructorlike_in_constructorlikelist1546: org.antlr.runtime.BitSet = {3,85,94,102,103,155,157,170,186,195,196,200,201,202,205}
    FOLLOW_constructorlike_in_root92: org.antlr.runtime.BitSet = {1,85,94,102,103,155,157,170,186,195,196,200,201,202,205}
    FOLLOW_constructorlikelist_in_withblock1469: org.antlr.runtime.BitSet = {3}
    FOLLOW_contextblock_in_constructor1575: org.antlr.runtime.BitSet = {169}
    FOLLOW_contextblock_in_withblock1463: org.antlr.runtime.BitSet = {106}
    FOLLOW_contextdef_in_definition165: org.antlr.runtime.BitSet = {1}
    FOLLOW_crossbuild_stmt_in_statement3042: org.antlr.runtime.BitSet = {1}
    FOLLOW_cstatement_in_cstatements2785: org.antlr.runtime.BitSet = {1,87,89}
    FOLLOW_cstatements_in_contextblock2755: org.antlr.runtime.BitSet = {3}
    FOLLOW_ctorsemantic_in_constructor1579: org.antlr.runtime.BitSet = {3}
    FOLLOW_ctorstart_in_constructor1567: org.antlr.runtime.BitSet = {95}
    FOLLOW_declaration_in_statement2999: org.antlr.runtime.BitSet = {1}
    FOLLOW_definition_in_constructorlikelist1542: org.antlr.runtime.BitSet = {3,85,94,102,103,155,157,170,186,195,196,200,201,202,205}
    FOLLOW_definition_in_root86: org.antlr.runtime.BitSet = {1,85,94,102,103,155,157,170,186,195,196,200,201,202,205}
    FOLLOW_display_in_ctorstart1698: org.antlr.runtime.BitSet = {3}
    FOLLOW_display_in_ctorstart1716: org.antlr.runtime.BitSet = {3}
    FOLLOW_endian_in_endiandef113: org.antlr.runtime.BitSet = {3}
    FOLLOW_endian_in_tokendef280: org.antlr.runtime.BitSet = {126}
    FOLLOW_endiandef_in_root80: org.antlr.runtime.BitSet = {1,85,94,102,103,155,157,170,186,195,196,200,201,202,205}
    FOLLOW_export_in_statement3118: org.antlr.runtime.BitSet = {1}
    FOLLOW_expr_apply_in_expr4902: org.antlr.runtime.BitSet = {1}
    FOLLOW_expr_apply_in_funcall3729: org.antlr.runtime.BitSet = {1}
    FOLLOW_expr_in_assignment3326: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_assignment3354: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_assignment3384: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_assignment3406: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_assignment3429: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_assignment3446: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_assignment3465: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_cond_stmt3996: org.antlr.runtime.BitSet = {134}
    FOLLOW_expr_in_expr4146: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4150: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4165: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4169: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4184: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4188: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4204: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4208: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4223: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4227: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4242: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4246: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4262: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4266: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4281: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4285: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4300: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4304: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4319: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4323: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4339: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4343: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4358: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4362: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4377: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4381: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4396: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4400: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4415: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4419: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4434: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4438: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4453: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4457: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4472: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4476: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4491: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4495: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4510: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4514: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4529: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4533: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4548: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4552: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4568: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4572: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4587: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4591: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4606: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4610: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4626: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4630: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4645: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4649: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4664: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4668: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4683: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4687: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4703: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4707: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4722: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4726: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4741: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4745: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4760: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4764: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4779: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4783: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4798: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4802: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4817: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_expr4821: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4837: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4852: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4867: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4882: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr4941: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_expr_operands5055: org.antlr.runtime.BitSet = {1,83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_expr_in_jumpdest3915: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_return_stmt4080: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_sizedstar3545: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_sizedstar3565: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_sizedstar3584: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_in_sizedstar3599: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_operands_in_expr_apply5003: org.antlr.runtime.BitSet = {3}
    FOLLOW_expr_operands_in_expr_apply5022: org.antlr.runtime.BitSet = {3}
    FOLLOW_family_or_operand_symbol_in_pequation1978: org.antlr.runtime.BitSet = {83,86,91,109,113,138,139,143,150,156,158,167,168,174,192,204,207}
    FOLLOW_family_symbol_in_pequation1998: org.antlr.runtime.BitSet = {83,86,91,109,113,138,139,143,150,156,158,167,168,174,192,204,207}
    FOLLOW_family_symbol_in_pequation2018: org.antlr.runtime.BitSet = {83,86,91,109,113,138,139,143,150,156,158,167,168,174,192,204,207}
    FOLLOW_family_symbol_in_pequation2038: org.antlr.runtime.BitSet = {83,86,91,109,113,138,139,143,150,156,158,167,168,174,192,204,207}
    FOLLOW_family_symbol_in_pequation2058: org.antlr.runtime.BitSet = {83,86,91,109,113,138,139,143,150,156,158,167,168,174,192,204,207}
    FOLLOW_family_symbol_in_pequation2078: org.antlr.runtime.BitSet = {83,86,91,109,113,138,139,143,150,156,158,167,168,174,192,204,207}
    FOLLOW_fielddef_in_fielddefs299: org.antlr.runtime.BitSet = {3,125}
    FOLLOW_fielddefs_in_contextdef719: org.antlr.runtime.BitSet = {3}
    FOLLOW_fielddefs_in_tokendef258: org.antlr.runtime.BitSet = {3}
    FOLLOW_fielddefs_in_tokendef284: org.antlr.runtime.BitSet = {3}
    FOLLOW_fieldmod_in_fieldmods359: org.antlr.runtime.BitSet = {3,107,137,160,181}
    FOLLOW_fieldmods_in_fielddef342: org.antlr.runtime.BitSet = {3}
    FOLLOW_funcall_in_statement3011: org.antlr.runtime.BitSet = {1}
    FOLLOW_goto_stmt_in_statement3051: org.antlr.runtime.BitSet = {1}
    FOLLOW_id_or_nil_in_withblock1455: org.antlr.runtime.BitSet = {95,159}
    FOLLOW_identifier_in_id_or_nil1491: org.antlr.runtime.BitSet = {1}
    FOLLOW_identifier_in_stringorident999: org.antlr.runtime.BitSet = {1}
    FOLLOW_identifierlist_in_pcodeopdef1078: org.antlr.runtime.BitSet = {3}
    FOLLOW_identifierlist_in_varnodedef888: org.antlr.runtime.BitSet = {3}
    FOLLOW_intblist_in_valueattach1108: org.antlr.runtime.BitSet = {3}
    FOLLOW_intbpart_in_intblist1138: org.antlr.runtime.BitSet = {3,91,109,138,158,204}
    FOLLOW_integer_in_aligndef219: org.antlr.runtime.BitSet = {3}
    FOLLOW_integer_in_assignment3317: org.antlr.runtime.BitSet = {91,109,138}
    FOLLOW_integer_in_assignment3321: org.antlr.runtime.BitSet = {3}
    FOLLOW_integer_in_assignment3349: org.antlr.runtime.BitSet = {3}
    FOLLOW_integer_in_assignment3379: org.antlr.runtime.BitSet = {3}
    FOLLOW_integer_in_bitrange3495: org.antlr.runtime.BitSet = {91,109,138}
    FOLLOW_integer_in_bitrange3499: org.antlr.runtime.BitSet = {3}
    FOLLOW_integer_in_declaration3151: org.antlr.runtime.BitSet = {3}
    FOLLOW_integer_in_expr4929: org.antlr.runtime.BitSet = {1}
    FOLLOW_integer_in_expr4962: org.antlr.runtime.BitSet = {3}
    FOLLOW_integer_in_fielddef334: org.antlr.runtime.BitSet = {91,109,138}
    FOLLOW_integer_in_fielddef338: org.antlr.runtime.BitSet = {127,166}
    FOLLOW_integer_in_intbpart1173: org.antlr.runtime.BitSet = {3}
    FOLLOW_integer_in_intbpart1183: org.antlr.runtime.BitSet = {1}
    FOLLOW_integer_in_jumpdest3930: org.antlr.runtime.BitSet = {3}
    FOLLOW_integer_in_jumpdest3945: org.antlr.runtime.BitSet = {139,204}
    FOLLOW_integer_in_pexpression22654: org.antlr.runtime.BitSet = {1}
    FOLLOW_integer_in_pexpression2408: org.antlr.runtime.BitSet = {1}
    FOLLOW_integer_in_sbitrange1055: org.antlr.runtime.BitSet = {91,109,138}
    FOLLOW_integer_in_sbitrange1059: org.antlr.runtime.BitSet = {3}
    FOLLOW_integer_in_sizedstar3541: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_integer_in_sizedstar3580: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_integer_in_sizedstarv3641: org.antlr.runtime.BitSet = {139,204}
    FOLLOW_integer_in_sizedstarv3682: org.antlr.runtime.BitSet = {139,204}
    FOLLOW_integer_in_sizemod837: org.antlr.runtime.BitSet = {3}
    FOLLOW_integer_in_tokendef254: org.antlr.runtime.BitSet = {126}
    FOLLOW_integer_in_tokendef276: org.antlr.runtime.BitSet = {90,153}
    FOLLOW_integer_in_varnode5091: org.antlr.runtime.BitSet = {91,109,138}
    FOLLOW_integer_in_varnode5095: org.antlr.runtime.BitSet = {3}
    FOLLOW_integer_in_varnode5111: org.antlr.runtime.BitSet = {3}
    FOLLOW_integer_in_varnodedef880: org.antlr.runtime.BitSet = {91,109,138}
    FOLLOW_integer_in_varnodedef884: org.antlr.runtime.BitSet = {140}
    FOLLOW_integer_in_wordsizemod856: org.antlr.runtime.BitSet = {3}
    FOLLOW_jump_symbol_in_jumpdest3899: org.antlr.runtime.BitSet = {3}
    FOLLOW_jumpdest_in_call_stmt4048: org.antlr.runtime.BitSet = {3}
    FOLLOW_jumpdest_in_cond_stmt4003: org.antlr.runtime.BitSet = {3}
    FOLLOW_jumpdest_in_goto_stmt3839: org.antlr.runtime.BitSet = {3}
    FOLLOW_label_in_jumpdest3965: org.antlr.runtime.BitSet = {3}
    FOLLOW_label_in_statement3109: org.antlr.runtime.BitSet = {1}
    FOLLOW_macrodef_in_constructorlike1334: org.antlr.runtime.BitSet = {1}
    FOLLOW_nameattach_in_definition195: org.antlr.runtime.BitSet = {1}
    FOLLOW_operand_symbol_in_build_stmt3759: org.antlr.runtime.BitSet = {3}
    FOLLOW_pattern_symbol2_in_pexpression22644: org.antlr.runtime.BitSet = {1}
    FOLLOW_pattern_symbol_in_pexpression2398: org.antlr.runtime.BitSet = {1}
    FOLLOW_pcodeopdef_in_definition185: org.antlr.runtime.BitSet = {1}
    FOLLOW_pequation_in_bitpattern1641: org.antlr.runtime.BitSet = {3}
    FOLLOW_pequation_in_pequation1889: org.antlr.runtime.BitSet = {96,97,114,115,118,135,136,139,151,152,163,168,178,204}
    FOLLOW_pequation_in_pequation1893: org.antlr.runtime.BitSet = {3}
    FOLLOW_pequation_in_pequation1908: org.antlr.runtime.BitSet = {96,97,114,115,118,135,136,139,151,152,163,168,178,204}
    FOLLOW_pequation_in_pequation1912: org.antlr.runtime.BitSet = {3}
    FOLLOW_pequation_in_pequation1927: org.antlr.runtime.BitSet = {96,97,114,115,118,135,136,139,151,152,163,168,178,204}
    FOLLOW_pequation_in_pequation1931: org.antlr.runtime.BitSet = {3}
    FOLLOW_pequation_in_pequation1947: org.antlr.runtime.BitSet = {3}
    FOLLOW_pequation_in_pequation1962: org.antlr.runtime.BitSet = {3}
    FOLLOW_pequation_in_pequation2107: org.antlr.runtime.BitSet = {3}
    FOLLOW_pequation_symbol_in_pequation2094: org.antlr.runtime.BitSet = {1}
    FOLLOW_pexpression2_in_pequation1983: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression2_in_pequation2003: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression2_in_pequation2023: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression2_in_pequation2043: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression2_in_pequation2063: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression2_in_pequation2083: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression2_in_pexpression22445: org.antlr.runtime.BitSet = {83,86,91,109,113,138,139,143,150,156,158,167,168,174,192,204,207}
    FOLLOW_pexpression2_in_pexpression22449: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression2_in_pexpression22464: org.antlr.runtime.BitSet = {83,86,91,109,113,138,139,143,150,156,158,167,168,174,192,204,207}
    FOLLOW_pexpression2_in_pexpression22468: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression2_in_pexpression22483: org.antlr.runtime.BitSet = {83,86,91,109,113,138,139,143,150,156,158,167,168,174,192,204,207}
    FOLLOW_pexpression2_in_pexpression22487: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression2_in_pexpression22502: org.antlr.runtime.BitSet = {83,86,91,109,113,138,139,143,150,156,158,167,168,174,192,204,207}
    FOLLOW_pexpression2_in_pexpression22506: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression2_in_pexpression22521: org.antlr.runtime.BitSet = {83,86,91,109,113,138,139,143,150,156,158,167,168,174,192,204,207}
    FOLLOW_pexpression2_in_pexpression22525: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression2_in_pexpression22540: org.antlr.runtime.BitSet = {83,86,91,109,113,138,139,143,150,156,158,167,168,174,192,204,207}
    FOLLOW_pexpression2_in_pexpression22544: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression2_in_pexpression22559: org.antlr.runtime.BitSet = {83,86,91,109,113,138,139,143,150,156,158,167,168,174,192,204,207}
    FOLLOW_pexpression2_in_pexpression22563: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression2_in_pexpression22578: org.antlr.runtime.BitSet = {83,86,91,109,113,138,139,143,150,156,158,167,168,174,192,204,207}
    FOLLOW_pexpression2_in_pexpression22582: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression2_in_pexpression22597: org.antlr.runtime.BitSet = {83,86,91,109,113,138,139,143,150,156,158,167,168,174,192,204,207}
    FOLLOW_pexpression2_in_pexpression22601: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression2_in_pexpression22617: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression2_in_pexpression22632: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression2_in_pexpression22666: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression_in_cstatement2812: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression_in_pexpression2199: org.antlr.runtime.BitSet = {83,86,91,109,113,138,139,143,150,156,158,167,168,174,192,204,207}
    FOLLOW_pexpression_in_pexpression2203: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression_in_pexpression2218: org.antlr.runtime.BitSet = {83,86,91,109,113,138,139,143,150,156,158,167,168,174,192,204,207}
    FOLLOW_pexpression_in_pexpression2222: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression_in_pexpression2237: org.antlr.runtime.BitSet = {83,86,91,109,113,138,139,143,150,156,158,167,168,174,192,204,207}
    FOLLOW_pexpression_in_pexpression2241: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression_in_pexpression2256: org.antlr.runtime.BitSet = {83,86,91,109,113,138,139,143,150,156,158,167,168,174,192,204,207}
    FOLLOW_pexpression_in_pexpression2260: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression_in_pexpression2275: org.antlr.runtime.BitSet = {83,86,91,109,113,138,139,143,150,156,158,167,168,174,192,204,207}
    FOLLOW_pexpression_in_pexpression2279: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression_in_pexpression2294: org.antlr.runtime.BitSet = {83,86,91,109,113,138,139,143,150,156,158,167,168,174,192,204,207}
    FOLLOW_pexpression_in_pexpression2298: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression_in_pexpression2313: org.antlr.runtime.BitSet = {83,86,91,109,113,138,139,143,150,156,158,167,168,174,192,204,207}
    FOLLOW_pexpression_in_pexpression2317: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression_in_pexpression2332: org.antlr.runtime.BitSet = {83,86,91,109,113,138,139,143,150,156,158,167,168,174,192,204,207}
    FOLLOW_pexpression_in_pexpression2336: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression_in_pexpression2351: org.antlr.runtime.BitSet = {83,86,91,109,113,138,139,143,150,156,158,167,168,174,192,204,207}
    FOLLOW_pexpression_in_pexpression2355: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression_in_pexpression2371: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression_in_pexpression2386: org.antlr.runtime.BitSet = {3}
    FOLLOW_pexpression_in_pexpression2420: org.antlr.runtime.BitSet = {3}
    FOLLOW_pieces_in_display1737: org.antlr.runtime.BitSet = {3}
    FOLLOW_printpiece_in_pieces1751: org.antlr.runtime.BitSet = {1,101,139,171,190,203}
    FOLLOW_qstring_in_stringorident1008: org.antlr.runtime.BitSet = {1}
    FOLLOW_return_stmt_in_statement3096: org.antlr.runtime.BitSet = {1}
    FOLLOW_sbitrange_in_bitrangedef1024: org.antlr.runtime.BitSet = {3,92}
    FOLLOW_section_label_in_statement3128: org.antlr.runtime.BitSet = {1}
    FOLLOW_section_symbol_in_crossbuild_stmt3795: org.antlr.runtime.BitSet = {3}
    FOLLOW_semantic_in_ctorsemantic1606: org.antlr.runtime.BitSet = {3}
    FOLLOW_semantic_in_macrodef1388: org.antlr.runtime.BitSet = {3}
    FOLLOW_sizedstar_in_assignment3461: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_sizedstar_in_expr4892: org.antlr.runtime.BitSet = {1}
    FOLLOW_sizedstarv_in_export4106: org.antlr.runtime.BitSet = {3}
    FOLLOW_sizemod_in_spacemod789: org.antlr.runtime.BitSet = {1}
    FOLLOW_space_symbol_in_jumpdest3949: org.antlr.runtime.BitSet = {3}
    FOLLOW_space_symbol_in_sizedstar3536: org.antlr.runtime.BitSet = {91,109,138}
    FOLLOW_space_symbol_in_sizedstar3560: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_space_symbol_in_sizedstarv3636: org.antlr.runtime.BitSet = {91,109,138}
    FOLLOW_space_symbol_in_sizedstarv3661: org.antlr.runtime.BitSet = {139,204}
    FOLLOW_space_symbol_in_varnodedef875: org.antlr.runtime.BitSet = {91,109,138}
    FOLLOW_spacedef_in_definition170: org.antlr.runtime.BitSet = {1}
    FOLLOW_spacemod_in_spacemods771: org.antlr.runtime.BitSet = {3,110,182,198,206}
    FOLLOW_spacemods_in_spacedef754: org.antlr.runtime.BitSet = {3}
    FOLLOW_specific_identifier_in_tokendef249: org.antlr.runtime.BitSet = {91,109,138}
    FOLLOW_specific_identifier_in_tokendef271: org.antlr.runtime.BitSet = {91,109,138}
    FOLLOW_specific_identifier_in_typemod817: org.antlr.runtime.BitSet = {3}
    FOLLOW_specific_symbol_in_assignment3312: org.antlr.runtime.BitSet = {91,109,138}
    FOLLOW_specific_symbol_in_bitrange3490: org.antlr.runtime.BitSet = {91,109,138}
    FOLLOW_specific_symbol_in_expr4957: org.antlr.runtime.BitSet = {91,109,138}
    FOLLOW_specific_symbol_in_sizedstarv3645: org.antlr.runtime.BitSet = {3}
    FOLLOW_specific_symbol_in_sizedstarv3666: org.antlr.runtime.BitSet = {3}
    FOLLOW_specific_symbol_in_sizedstarv3686: org.antlr.runtime.BitSet = {3}
    FOLLOW_specific_symbol_in_sizedstarv3702: org.antlr.runtime.BitSet = {3}
    FOLLOW_specific_symbol_in_varnode5076: org.antlr.runtime.BitSet = {1}
    FOLLOW_statement_in_statements2955: org.antlr.runtime.BitSet = {1,87,89,99,100,105,119,134,141,149,154,173,176}
    FOLLOW_statements_in_code_block2939: org.antlr.runtime.BitSet = {1}
    FOLLOW_string_in_printpiece1800: org.antlr.runtime.BitSet = {1}
    FOLLOW_stringorident_in_stringoridentlist976: org.antlr.runtime.BitSet = {3,139,171,204}
    FOLLOW_stringoridentlist_in_nameattach1212: org.antlr.runtime.BitSet = {3}
    FOLLOW_tokendef_in_definition160: org.antlr.runtime.BitSet = {1}
    FOLLOW_typemod_in_spacemod784: org.antlr.runtime.BitSet = {1}
    FOLLOW_unbound_identifier_in_assignment3344: org.antlr.runtime.BitSet = {91,109,138}
    FOLLOW_unbound_identifier_in_assignment3374: org.antlr.runtime.BitSet = {91,109,138}
    FOLLOW_unbound_identifier_in_assignment3401: org.antlr.runtime.BitSet = {83,84,86,87,91,92,93,96,97,98,109,111,113,118,120,121,122,123,124,128,129,130,131,132,133,135,136,138,139,143,150,151,152,156,158,162,163,167,168,172,174,175,179,180,184,185,188,189,192,197,204,207}
    FOLLOW_unbound_identifier_in_declaration3146: org.antlr.runtime.BitSet = {91,109,138}
    FOLLOW_unbound_identifier_in_declaration3164: org.antlr.runtime.BitSet = {3}
    FOLLOW_unbound_identifier_in_fielddef329: org.antlr.runtime.BitSet = {91,109,138}
    FOLLOW_unbound_identifier_in_macrodef1377: org.antlr.runtime.BitSet = {88,116}
    FOLLOW_unbound_identifier_in_spacedef747: org.antlr.runtime.BitSet = {187}
    FOLLOW_value_symbol_in_valuelist1280: org.antlr.runtime.BitSet = {3,139,204}
    FOLLOW_valueattach_in_definition190: org.antlr.runtime.BitSet = {1}
    FOLLOW_valuelist_in_nameattach1207: org.antlr.runtime.BitSet = {191}
    FOLLOW_valuelist_in_valueattach1103: org.antlr.runtime.BitSet = {142}
    FOLLOW_valuelist_in_varattach1237: org.antlr.runtime.BitSet = {140}
    FOLLOW_varattach_in_definition200: org.antlr.runtime.BitSet = {1}
    FOLLOW_varlist_in_varattach1242: org.antlr.runtime.BitSet = {3}
    FOLLOW_varnode_in_crossbuild_stmt3791: org.antlr.runtime.BitSet = {139,204}
    FOLLOW_varnode_in_export4121: org.antlr.runtime.BitSet = {3}
    FOLLOW_varnode_in_expr4911: org.antlr.runtime.BitSet = {1}
    FOLLOW_varnode_in_varnode5116: org.antlr.runtime.BitSet = {3}
    FOLLOW_varnode_in_varnode5129: org.antlr.runtime.BitSet = {3}
    FOLLOW_varnode_symbol_in_contextdef714: org.antlr.runtime.BitSet = {126}
    FOLLOW_varnode_symbol_in_sbitrange1050: org.antlr.runtime.BitSet = {91,109,138}
    FOLLOW_varnode_symbol_in_varlist1316: org.antlr.runtime.BitSet = {3,139,204}
    FOLLOW_varnodedef_in_definition175: org.antlr.runtime.BitSet = {1}
    FOLLOW_whitespace_in_printpiece1786: org.antlr.runtime.BitSet = {1}
    FOLLOW_withblock_in_constructorlike1341: org.antlr.runtime.BitSet = {1}
    FOLLOW_wordsizemod_in_spacemod794: org.antlr.runtime.BitSet = {1}
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




    class identifier_return(org.antlr.runtime.tree.TreeRuleReturnScope):
        start: object
        tree: org.antlr.runtime.tree.Tree
        value: unicode



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






    class id_or_nil_return(org.antlr.runtime.tree.TreeRuleReturnScope):
        start: object
        tree: org.antlr.runtime.tree.Tree
        value: unicode



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



    @overload
    def __init__(self, input: org.antlr.runtime.tree.TreeNodeStream): ...

    @overload
    def __init__(self, input: org.antlr.runtime.tree.TreeNodeStream, state: org.antlr.runtime.RecognizerSharedState): ...



    def aligndef(self) -> None: ...

    def alreadyParsedRule(self, __a0: org.antlr.runtime.IntStream, __a1: int) -> bool: ...

    def arguments(self) -> generic.stl.Pair: ...

    def assignment(self) -> generic.stl.VectorSTL: ...

    def beginResync(self) -> None: ...

    def bitpat_or_nil(self) -> ghidra.pcodeCPort.slghpatexpress.PatternEquation: ...

    def bitpattern(self) -> ghidra.pcodeCPort.slghpatexpress.PatternEquation: ...

    def bitrange(self) -> ghidra.pcodeCPort.slgh_compile.ExprTree: ...

    def bitrangedef(self) -> None: ...

    def build_stmt(self) -> generic.stl.VectorSTL: ...

    def call_stmt(self) -> generic.stl.VectorSTL: ...

    def code_block(self, startingPoint: ghidra.sleigh.grammar.Location) -> ghidra.pcodeCPort.semantics.ConstructTpl: ...

    def cond_stmt(self) -> generic.stl.VectorSTL: ...

    def constructor(self) -> None: ...

    def constructorlike(self) -> None: ...

    def constructorlikelist(self) -> None: ...

    @overload
    def consumeUntil(self, __a0: org.antlr.runtime.IntStream, __a1: int) -> None: ...

    @overload
    def consumeUntil(self, __a0: org.antlr.runtime.IntStream, __a1: org.antlr.runtime.BitSet) -> None: ...

    def contextblock(self) -> generic.stl.VectorSTL: ...

    def contextdef(self) -> None: ...

    def crossbuild_stmt(self) -> generic.stl.VectorSTL: ...

    def cstatement(self, r: generic.stl.VectorSTL) -> None: ...

    def cstatements(self) -> generic.stl.VectorSTL: ...

    def ctorsemantic(self, ctor: ghidra.pcodeCPort.slghsymbol.Constructor) -> ghidra.pcodeCPort.slgh_compile.SectionVector: ...

    def ctorstart(self) -> ghidra.pcodeCPort.slghsymbol.Constructor: ...

    def declaration(self) -> None: ...

    def definition(self) -> None: ...

    def display(self, ct: ghidra.pcodeCPort.slghsymbol.Constructor) -> None: ...

    def displayRecognitionError(self, __a0: List[unicode], __a1: org.antlr.runtime.RecognitionException) -> None: ...

    def emitErrorMessage(self, __a0: unicode) -> None: ...

    def endResync(self) -> None: ...

    def endian(self) -> int: ...

    def endiandef(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def export(self, rtl: ghidra.pcodeCPort.semantics.ConstructTpl) -> ghidra.pcodeCPort.semantics.ConstructTpl: ...

    def expr(self) -> ghidra.pcodeCPort.slgh_compile.ExprTree: ...

    def expr_apply(self) -> object: ...

    def expr_operands(self) -> generic.stl.VectorSTL: ...

    def failed(self) -> bool: ...

    def family_or_operand_symbol(self, purpose: unicode) -> org.antlr.runtime.tree.Tree: ...

    def family_symbol(self, purpose: unicode) -> ghidra.pcodeCPort.slghsymbol.FamilySymbol: ...

    def fielddef(self) -> None: ...

    def fielddefs(self) -> None: ...

    def fieldmod(self) -> None: ...

    def fieldmods(self) -> None: ...

    def funcall(self) -> generic.stl.VectorSTL: ...

    def getBacktrackingLevel(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getDelegates(self) -> List[org.antlr.runtime.tree.TreeParser]: ...

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

    def getTreeNodeStream(self) -> org.antlr.runtime.tree.TreeNodeStream: ...

    def goto_stmt(self) -> generic.stl.VectorSTL: ...

    def hashCode(self) -> int: ...

    def id_or_nil(self) -> ghidra.sleigh.grammar.SleighCompiler.id_or_nil_return: ...

    def identifier(self) -> ghidra.sleigh.grammar.SleighCompiler.identifier_return: ...

    def identifierlist(self) -> generic.stl.Pair: ...

    @overload
    def inContext(self, __a0: unicode) -> bool: ...

    @overload
    @staticmethod
    def inContext(__a0: org.antlr.runtime.tree.TreeAdaptor, __a1: List[unicode], __a2: object, __a3: unicode) -> bool: ...

    def intblist(self) -> generic.stl.VectorSTL: ...

    def intbpart(self) -> long: ...

    def integer(self) -> ghidra.sleigh.grammar.RadixBigInteger: ...

    def jump_symbol(self, purpose: unicode) -> ghidra.pcodeCPort.semantics.VarnodeTpl: ...

    def jumpdest(self, purpose: unicode) -> ghidra.pcodeCPort.slgh_compile.ExprTree: ...

    def label(self) -> generic.stl.Pair: ...

    def macrodef(self) -> None: ...

    def match(self, __a0: org.antlr.runtime.IntStream, __a1: int, __a2: org.antlr.runtime.BitSet) -> object: ...

    def matchAny(self, __a0: org.antlr.runtime.IntStream) -> None: ...

    def memoize(self, __a0: org.antlr.runtime.IntStream, __a1: int, __a2: int) -> None: ...

    def mismatchIsMissingToken(self, __a0: org.antlr.runtime.IntStream, __a1: org.antlr.runtime.BitSet) -> bool: ...

    def mismatchIsUnwantedToken(self, __a0: org.antlr.runtime.IntStream, __a1: int) -> bool: ...

    def nameattach(self) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def operand_symbol(self, purpose: unicode) -> ghidra.pcodeCPort.slghsymbol.OperandSymbol: ...

    def pattern_symbol(self, purpose: unicode) -> ghidra.pcodeCPort.slghpatexpress.PatternExpression: ...

    def pattern_symbol2(self, purpose: unicode) -> ghidra.pcodeCPort.slghpatexpress.PatternExpression: ...

    def pcodeopdef(self) -> None: ...

    def pequation(self) -> ghidra.pcodeCPort.slghpatexpress.PatternEquation: ...

    def pequation_symbol(self, purpose: unicode) -> ghidra.pcodeCPort.slghpatexpress.PatternEquation: ...

    def pexpression(self) -> ghidra.pcodeCPort.slghpatexpress.PatternExpression: ...

    def pexpression2(self) -> ghidra.pcodeCPort.slghpatexpress.PatternExpression: ...

    def pieces(self, ct: ghidra.pcodeCPort.slghsymbol.Constructor) -> None: ...

    def printpiece(self, ct: ghidra.pcodeCPort.slghsymbol.Constructor) -> None: ...

    def qstring(self) -> unicode: ...

    def recover(self, __a0: org.antlr.runtime.IntStream, __a1: org.antlr.runtime.RecognitionException) -> None: ...

    def recoverFromMismatchedSet(self, __a0: org.antlr.runtime.IntStream, __a1: org.antlr.runtime.RecognitionException, __a2: org.antlr.runtime.BitSet) -> object: ...

    def reportError(self, __a0: org.antlr.runtime.RecognitionException) -> None: ...

    def reset(self) -> None: ...

    def return_stmt(self) -> generic.stl.VectorSTL: ...

    def root(self, pe: ghidra.sleigh.grammar.ParsingEnvironment, sc: ghidra.pcodeCPort.slgh_compile.SleighCompile) -> int: ...

    def sbitrange(self) -> None: ...

    def section_label(self) -> generic.stl.Pair: ...

    def section_symbol(self, purpose: unicode) -> ghidra.pcodeCPort.slghsymbol.SectionSymbol: ...

    def semantic(self, pe: ghidra.sleigh.grammar.ParsingEnvironment, containerLoc: ghidra.sleigh.grammar.Location, pcode: ghidra.pcodeCPort.slgh_compile.PcodeCompile, where: org.antlr.runtime.tree.Tree, sectionsAllowed: bool, isMacroParse: bool) -> ghidra.pcodeCPort.slgh_compile.SectionVector: ...

    def setBacktrackingLevel(self, __a0: int) -> None: ...

    def setTreeNodeStream(self, __a0: org.antlr.runtime.tree.TreeNodeStream) -> None: ...

    def sizedstar(self) -> generic.stl.Pair: ...

    def sizedstarv(self) -> generic.stl.Pair: ...

    def sizemod(self) -> None: ...

    def space_symbol(self, purpose: unicode) -> ghidra.pcodeCPort.slghsymbol.SpaceSymbol: ...

    def spacedef(self) -> None: ...

    def spacemod(self) -> None: ...

    def spacemods(self) -> None: ...

    def specific_identifier(self, purpose: unicode) -> org.antlr.runtime.tree.Tree: ...

    def specific_symbol(self, purpose: unicode) -> ghidra.pcodeCPort.slghsymbol.SpecificSymbol: ...

    def statement(self) -> None: ...

    def statements(self) -> None: ...

    def string(self) -> unicode: ...

    def stringorident(self) -> unicode: ...

    def stringoridentlist(self) -> generic.stl.VectorSTL: ...

    def toString(self) -> unicode: ...

    def toStrings(self, __a0: List[object]) -> List[object]: ...

    def tokendef(self) -> None: ...

    @overload
    def traceIn(self, __a0: unicode, __a1: int) -> None: ...

    @overload
    def traceIn(self, __a0: unicode, __a1: int, __a2: object) -> None: ...

    @overload
    def traceOut(self, __a0: unicode, __a1: int) -> None: ...

    @overload
    def traceOut(self, __a0: unicode, __a1: int, __a2: object) -> None: ...

    def typemod(self) -> None: ...

    def unbound_identifier(self, purpose: unicode) -> org.antlr.runtime.tree.Tree: ...

    def value_symbol(self, purpose: unicode) -> generic.stl.Pair: ...

    def valueattach(self) -> None: ...

    def valuelist(self, purpose: unicode) -> generic.stl.Pair: ...

    def varattach(self) -> None: ...

    def varlist(self, purpose: unicode) -> generic.stl.VectorSTL: ...

    def varnode(self) -> ghidra.pcodeCPort.semantics.VarnodeTpl: ...

    def varnode_symbol(self, purpose: unicode, noWildcards: bool) -> ghidra.pcodeCPort.slghsymbol.VarnodeSymbol: ...

    def varnodedef(self) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def whitespace(self) -> unicode: ...

    def withblock(self) -> None: ...

    def wordsizemod(self) -> None: ...

    @property
    def delegates(self) -> List[org.antlr.runtime.tree.TreeParser]: ...

    @property
    def grammarFileName(self) -> unicode: ...

    @property
    def tokenNames(self) -> List[unicode]: ...
