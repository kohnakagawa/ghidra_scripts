from typing import List
import ghidra.sleigh.grammar
import ghidra.sleigh.grammar.SleighParser_SemanticParser
import java.lang
import org.antlr.runtime
import org.antlr.runtime.tree


class SleighParser_SemanticParser(ghidra.sleigh.grammar.AbstractSleighParser):
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
    FOLLOW_AMPERSAND_in_expr_and_op1432: org.antlr.runtime.BitSet = {1}
    FOLLOW_AMPERSAND_in_outererror428: org.antlr.runtime.BitSet = {1}
    FOLLOW_AMPERSAND_in_varnode2249: org.antlr.runtime.BitSet = {15}
    FOLLOW_AMPERSAND_in_varnode2280: org.antlr.runtime.BitSet = {6,10,18,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72}
    FOLLOW_ASSIGN_in_assignment548: org.antlr.runtime.BitSet = {6,8,10,18,25,32,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,79,80,233}
    FOLLOW_ASSIGN_in_assignment573: org.antlr.runtime.BitSet = {6,8,10,18,25,32,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,79,80,233}
    FOLLOW_ASSIGN_in_outererror365: org.antlr.runtime.BitSet = {1}
    FOLLOW_ASTERISK_in_mult_op1903: org.antlr.runtime.BitSet = {1}
    FOLLOW_ASTERISK_in_sizedstar737: org.antlr.runtime.BitSet = {74}
    FOLLOW_ASTERISK_in_sizedstar765: org.antlr.runtime.BitSet = {74}
    FOLLOW_ASTERISK_in_sizedstar802: org.antlr.runtime.BitSet = {15}
    FOLLOW_ASTERISK_in_sizedstar851: org.antlr.runtime.BitSet = {1}
    FOLLOW_BOOL_AND_in_booland_op1295: org.antlr.runtime.BitSet = {1}
    FOLLOW_BOOL_AND_in_outererror407: org.antlr.runtime.BitSet = {1}
    FOLLOW_BOOL_OR_in_expr_boolor_op1254: org.antlr.runtime.BitSet = {1}
    FOLLOW_BOOL_OR_in_outererror393: org.antlr.runtime.BitSet = {1}
    FOLLOW_BOOL_XOR_in_booland_op1309: org.antlr.runtime.BitSet = {1}
    FOLLOW_BOOL_XOR_in_outererror400: org.antlr.runtime.BitSet = {1}
    FOLLOW_CARET_in_expr_xor_op1391: org.antlr.runtime.BitSet = {1}
    FOLLOW_CARET_in_outererror421: org.antlr.runtime.BitSet = {1}
    FOLLOW_COLON_in_declaration605: org.antlr.runtime.BitSet = {10,18,39}
    FOLLOW_COLON_in_lvalue656: org.antlr.runtime.BitSet = {10,18,39}
    FOLLOW_COLON_in_outererror372: org.antlr.runtime.BitSet = {1}
    FOLLOW_COLON_in_sizedstar745: org.antlr.runtime.BitSet = {10,18,39}
    FOLLOW_COLON_in_sizedstar833: org.antlr.runtime.BitSet = {10,18,39}
    FOLLOW_COLON_in_varnode2207: org.antlr.runtime.BitSet = {10,18,39}
    FOLLOW_COLON_in_varnode2229: org.antlr.runtime.BitSet = {10,18,39}
    FOLLOW_COLON_in_varnode2253: org.antlr.runtime.BitSet = {10,18,39}
    FOLLOW_COMMA_in_crossbuild_stmt954: org.antlr.runtime.BitSet = {40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72}
    FOLLOW_COMMA_in_expr_operands2135: org.antlr.runtime.BitSet = {6,8,10,18,25,32,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,79,80,233}
    FOLLOW_COMMA_in_outererror379: org.antlr.runtime.BitSet = {1}
    FOLLOW_COMMA_in_sembitrange703: org.antlr.runtime.BitSet = {10,18,39}
    FOLLOW_EQUAL_in_eq_op1473: org.antlr.runtime.BitSet = {1}
    FOLLOW_EQUAL_in_outererror267: org.antlr.runtime.BitSet = {1}
    FOLLOW_EXCLAIM_in_unary_op2023: org.antlr.runtime.BitSet = {1}
    FOLLOW_FDIV_in_mult_op1987: org.antlr.runtime.BitSet = {1}
    FOLLOW_FDIV_in_outererror505: org.antlr.runtime.BitSet = {1}
    FOLLOW_FEQUAL_in_eq_op1501: org.antlr.runtime.BitSet = {1}
    FOLLOW_FEQUAL_in_outererror281: org.antlr.runtime.BitSet = {1}
    FOLLOW_FGREATEQUAL_in_compare_op1682: org.antlr.runtime.BitSet = {1}
    FOLLOW_FGREATEQUAL_in_outererror358: org.antlr.runtime.BitSet = {1}
    FOLLOW_FGREAT_in_compare_op1710: org.antlr.runtime.BitSet = {1}
    FOLLOW_FGREAT_in_outererror344: org.antlr.runtime.BitSet = {1}
    FOLLOW_FLESSEQUAL_in_compare_op1696: org.antlr.runtime.BitSet = {1}
    FOLLOW_FLESSEQUAL_in_outererror351: org.antlr.runtime.BitSet = {1}
    FOLLOW_FLESS_in_compare_op1668: org.antlr.runtime.BitSet = {1}
    FOLLOW_FLESS_in_outererror337: org.antlr.runtime.BitSet = {1}
    FOLLOW_FMINUS_in_add_op1862: org.antlr.runtime.BitSet = {1}
    FOLLOW_FMINUS_in_outererror463: org.antlr.runtime.BitSet = {1}
    FOLLOW_FMINUS_in_unary_op2065: org.antlr.runtime.BitSet = {1}
    FOLLOW_FMULT_in_mult_op1973: org.antlr.runtime.BitSet = {1}
    FOLLOW_FMULT_in_outererror498: org.antlr.runtime.BitSet = {1}
    FOLLOW_FNOTEQUAL_in_eq_op1515: org.antlr.runtime.BitSet = {1}
    FOLLOW_FNOTEQUAL_in_outererror288: org.antlr.runtime.BitSet = {1}
    FOLLOW_FPLUS_in_add_op1848: org.antlr.runtime.BitSet = {1}
    FOLLOW_FPLUS_in_outererror456: org.antlr.runtime.BitSet = {1}
    FOLLOW_GREATEQUAL_in_compare_op1570: org.antlr.runtime.BitSet = {1}
    FOLLOW_GREATEQUAL_in_outererror302: org.antlr.runtime.BitSet = {1}
    FOLLOW_GREAT_in_compare_op1598: org.antlr.runtime.BitSet = {1}
    FOLLOW_GREAT_in_label113: org.antlr.runtime.BitSet = {1}
    FOLLOW_KEY_BUILD_in_build_stmt926: org.antlr.runtime.BitSet = {40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72}
    FOLLOW_KEY_CALL_in_call_stmt1114: org.antlr.runtime.BitSet = {10,18,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,76}
    FOLLOW_KEY_CROSSBUILD_in_crossbuild_stmt950: org.antlr.runtime.BitSet = {6,10,18,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72}
    FOLLOW_KEY_EXPORT_in_export1180: org.antlr.runtime.BitSet = {8}
    FOLLOW_KEY_EXPORT_in_export1198: org.antlr.runtime.BitSet = {6,10,18,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72}
    FOLLOW_KEY_GOTO_in_goto_stmt979: org.antlr.runtime.BitSet = {10,18,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,76}
    FOLLOW_KEY_LOCAL_in_assignment542: org.antlr.runtime.BitSet = {8,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72}
    FOLLOW_KEY_LOCAL_in_declaration599: org.antlr.runtime.BitSet = {40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72}
    FOLLOW_KEY_LOCAL_in_declaration625: org.antlr.runtime.BitSet = {40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72}
    FOLLOW_KEY_RETURN_in_return_stmt1138: org.antlr.runtime.BitSet = {74}
    FOLLOW_LBRACE_in_semanticbody30: org.antlr.runtime.BitSet = {6,7,8,11,12,13,14,15,16,23,26,27,28,29,30,31,32,33,34,35,37,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,75,76,77,79,80,81,208,209,210,215,216,220,221,222,223,224,225,226,227,231,232,233}
    FOLLOW_LBRACKET_in_jumpdest1014: org.antlr.runtime.BitSet = {6,8,10,18,25,32,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,79,80,233}
    FOLLOW_LBRACKET_in_jumpdest1046: org.antlr.runtime.BitSet = {40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72}
    FOLLOW_LBRACKET_in_return_stmt1140: org.antlr.runtime.BitSet = {6,8,10,18,25,32,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,79,80,233}
    FOLLOW_LBRACKET_in_sembitrange697: org.antlr.runtime.BitSet = {10,18,39}
    FOLLOW_LBRACKET_in_sizedstar739: org.antlr.runtime.BitSet = {40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72}
    FOLLOW_LBRACKET_in_sizedstar767: org.antlr.runtime.BitSet = {40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72}
    FOLLOW_LEFT_in_section_def135: org.antlr.runtime.BitSet = {40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72}
    FOLLOW_LEFT_in_shift_op1751: org.antlr.runtime.BitSet = {1}
    FOLLOW_LESSEQUAL_in_compare_op1584: org.antlr.runtime.BitSet = {1}
    FOLLOW_LESSEQUAL_in_outererror295: org.antlr.runtime.BitSet = {1}
    FOLLOW_LESS_in_compare_op1556: org.antlr.runtime.BitSet = {1}
    FOLLOW_LESS_in_label109: org.antlr.runtime.BitSet = {40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72}
    FOLLOW_LPAREN_in_expr_operands2128: org.antlr.runtime.BitSet = {6,8,10,18,25,32,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,79,80,220,233}
    FOLLOW_LPAREN_in_expr_term2169: org.antlr.runtime.BitSet = {6,8,10,18,25,32,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,79,80,233}
    FOLLOW_LPAREN_in_outererror519: org.antlr.runtime.BitSet = {1}
    FOLLOW_MINUS_in_add_op1834: org.antlr.runtime.BitSet = {1}
    FOLLOW_MINUS_in_outererror449: org.antlr.runtime.BitSet = {1}
    FOLLOW_MINUS_in_unary_op2051: org.antlr.runtime.BitSet = {1}
    FOLLOW_NOTEQUAL_in_eq_op1487: org.antlr.runtime.BitSet = {1}
    FOLLOW_NOTEQUAL_in_outererror274: org.antlr.runtime.BitSet = {1}
    FOLLOW_PERCENT_in_mult_op1931: org.antlr.runtime.BitSet = {1}
    FOLLOW_PERCENT_in_outererror477: org.antlr.runtime.BitSet = {1}
    FOLLOW_PIPE_in_expr_or_op1350: org.antlr.runtime.BitSet = {1}
    FOLLOW_PIPE_in_outererror414: org.antlr.runtime.BitSet = {1}
    FOLLOW_PLUS_in_add_op1820: org.antlr.runtime.BitSet = {1}
    FOLLOW_PLUS_in_outererror442: org.antlr.runtime.BitSet = {1}
    FOLLOW_RBRACE_in_semanticbody36: org.antlr.runtime.BitSet = {1}
    FOLLOW_RBRACKET_in_jumpdest1018: org.antlr.runtime.BitSet = {1}
    FOLLOW_RBRACKET_in_jumpdest1050: org.antlr.runtime.BitSet = {1}
    FOLLOW_RBRACKET_in_outererror386: org.antlr.runtime.BitSet = {1}
    FOLLOW_RBRACKET_in_return_stmt1144: org.antlr.runtime.BitSet = {1}
    FOLLOW_RBRACKET_in_sembitrange709: org.antlr.runtime.BitSet = {1}
    FOLLOW_RBRACKET_in_sizedstar743: org.antlr.runtime.BitSet = {15}
    FOLLOW_RBRACKET_in_sizedstar771: org.antlr.runtime.BitSet = {1}
    FOLLOW_RES_IF_in_cond_stmt1086: org.antlr.runtime.BitSet = {6,8,10,18,25,32,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,79,80,233}
    FOLLOW_RIGHT_in_section_def139: org.antlr.runtime.BitSet = {1}
    FOLLOW_RIGHT_in_shift_op1765: org.antlr.runtime.BitSet = {1}
    FOLLOW_RPAREN_in_expr_operands2145: org.antlr.runtime.BitSet = {1}
    FOLLOW_RPAREN_in_expr_term2173: org.antlr.runtime.BitSet = {1}
    FOLLOW_RPAREN_in_outererror526: org.antlr.runtime.BitSet = {1}
    FOLLOW_SDIV_in_mult_op1945: org.antlr.runtime.BitSet = {1}
    FOLLOW_SDIV_in_outererror484: org.antlr.runtime.BitSet = {1}
    FOLLOW_SEMI_in_statement235: org.antlr.runtime.BitSet = {1}
    FOLLOW_SGREATEQUAL_in_compare_op1626: org.antlr.runtime.BitSet = {1}
    FOLLOW_SGREATEQUAL_in_outererror330: org.antlr.runtime.BitSet = {1}
    FOLLOW_SGREAT_in_compare_op1654: org.antlr.runtime.BitSet = {1}
    FOLLOW_SGREAT_in_outererror316: org.antlr.runtime.BitSet = {1}
    FOLLOW_SLASH_in_mult_op1917: org.antlr.runtime.BitSet = {1}
    FOLLOW_SLASH_in_outererror470: org.antlr.runtime.BitSet = {1}
    FOLLOW_SLESSEQUAL_in_compare_op1640: org.antlr.runtime.BitSet = {1}
    FOLLOW_SLESSEQUAL_in_outererror323: org.antlr.runtime.BitSet = {1}
    FOLLOW_SLESS_in_compare_op1612: org.antlr.runtime.BitSet = {1}
    FOLLOW_SLESS_in_outererror309: org.antlr.runtime.BitSet = {1}
    FOLLOW_SREM_in_mult_op1959: org.antlr.runtime.BitSet = {1}
    FOLLOW_SREM_in_outererror491: org.antlr.runtime.BitSet = {1}
    FOLLOW_SRIGHT_in_outererror435: org.antlr.runtime.BitSet = {1}
    FOLLOW_SRIGHT_in_shift_op1779: org.antlr.runtime.BitSet = {1}
    FOLLOW_TILDE_in_outererror512: org.antlr.runtime.BitSet = {1}
    FOLLOW_TILDE_in_unary_op2037: org.antlr.runtime.BitSet = {1}
    FOLLOW_add_op_in_expr_add1801: org.antlr.runtime.BitSet = {6,8,10,18,25,32,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,79,80,233}
    FOLLOW_assignment_in_statement167: org.antlr.runtime.BitSet = {222}
    FOLLOW_booland_op_in_expr_booland1276: org.antlr.runtime.BitSet = {6,8,10,18,25,32,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,79,80,233}
    FOLLOW_build_stmt_in_statement185: org.antlr.runtime.BitSet = {222}
    FOLLOW_call_stmt_in_statement209: org.antlr.runtime.BitSet = {222}
    FOLLOW_code_block_in_semantic53: org.antlr.runtime.BitSet = {1}
    FOLLOW_compare_op_in_expr_comp1537: org.antlr.runtime.BitSet = {6,8,10,18,25,32,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,79,80,233}
    FOLLOW_cond_stmt_in_statement203: org.antlr.runtime.BitSet = {222}
    FOLLOW_constant_in_declaration607: org.antlr.runtime.BitSet = {1}
    FOLLOW_constant_in_jumpdest1044: org.antlr.runtime.BitSet = {74}
    FOLLOW_constant_in_lvalue658: org.antlr.runtime.BitSet = {1}
    FOLLOW_constant_in_sembitrange701: org.antlr.runtime.BitSet = {16}
    FOLLOW_constant_in_sembitrange707: org.antlr.runtime.BitSet = {215}
    FOLLOW_constant_in_sizedstar747: org.antlr.runtime.BitSet = {1}
    FOLLOW_constant_in_sizedstar835: org.antlr.runtime.BitSet = {1}
    FOLLOW_constant_in_varnode2209: org.antlr.runtime.BitSet = {1}
    FOLLOW_constant_in_varnode2231: org.antlr.runtime.BitSet = {1}
    FOLLOW_constant_in_varnode2255: org.antlr.runtime.BitSet = {6,10,18,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72}
    FOLLOW_crossbuild_stmt_in_statement191: org.antlr.runtime.BitSet = {222}
    FOLLOW_declaration_in_statement173: org.antlr.runtime.BitSet = {222}
    FOLLOW_eq_op_in_expr_eq1454: org.antlr.runtime.BitSet = {6,8,10,18,25,32,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,79,80,233}
    FOLLOW_export_in_statement215: org.antlr.runtime.BitSet = {222}
    FOLLOW_expr_add_in_expr_shift1728: org.antlr.runtime.BitSet = {1,75,219,232}
    FOLLOW_expr_add_in_expr_shift1735: org.antlr.runtime.BitSet = {1,75,219,232}
    FOLLOW_expr_and_in_expr_xor1368: org.antlr.runtime.BitSet = {1,14}
    FOLLOW_expr_and_in_expr_xor1375: org.antlr.runtime.BitSet = {1,14}
    FOLLOW_expr_and_op_in_expr_and1413: org.antlr.runtime.BitSet = {6,8,10,18,25,32,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,79,80,233}
    FOLLOW_expr_apply_in_expr_func2088: org.antlr.runtime.BitSet = {1}
    FOLLOW_expr_apply_in_funcall913: org.antlr.runtime.BitSet = {1}
    FOLLOW_expr_booland_in_expr_boolor1231: org.antlr.runtime.BitSet = {1,12}
    FOLLOW_expr_booland_in_expr_boolor1238: org.antlr.runtime.BitSet = {1,12}
    FOLLOW_expr_boolor_in_expr1220: org.antlr.runtime.BitSet = {1}
    FOLLOW_expr_boolor_op_in_expr_boolor1235: org.antlr.runtime.BitSet = {6,8,10,18,25,32,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,79,80,233}
    FOLLOW_expr_comp_in_expr_eq1450: org.antlr.runtime.BitSet = {1,23,27,34,81}
    FOLLOW_expr_comp_in_expr_eq1457: org.antlr.runtime.BitSet = {1,23,27,34,81}
    FOLLOW_expr_eq_in_expr_and1409: org.antlr.runtime.BitSet = {1,6}
    FOLLOW_expr_eq_in_expr_and1416: org.antlr.runtime.BitSet = {1,6}
    FOLLOW_expr_func_in_expr_unary2010: org.antlr.runtime.BitSet = {1}
    FOLLOW_expr_in_assignment550: org.antlr.runtime.BitSet = {1}
    FOLLOW_expr_in_assignment575: org.antlr.runtime.BitSet = {1}
    FOLLOW_expr_in_cond_stmt1088: org.antlr.runtime.BitSet = {54}
    FOLLOW_expr_in_expr_operands2132: org.antlr.runtime.BitSet = {16,220}
    FOLLOW_expr_in_expr_operands2138: org.antlr.runtime.BitSet = {16,220}
    FOLLOW_expr_in_expr_term2171: org.antlr.runtime.BitSet = {220}
    FOLLOW_expr_in_jumpdest1016: org.antlr.runtime.BitSet = {215}
    FOLLOW_expr_in_lvalue682: org.antlr.runtime.BitSet = {1}
    FOLLOW_expr_in_return_stmt1142: org.antlr.runtime.BitSet = {215}
    FOLLOW_expr_mult_in_expr_add1797: org.antlr.runtime.BitSet = {1,32,35,80,210}
    FOLLOW_expr_mult_in_expr_add1804: org.antlr.runtime.BitSet = {1,32,35,80,210}
    FOLLOW_expr_operands_in_expr_apply2106: org.antlr.runtime.BitSet = {1}
    FOLLOW_expr_or_in_expr_booland1272: org.antlr.runtime.BitSet = {1,11,13}
    FOLLOW_expr_or_in_expr_booland1279: org.antlr.runtime.BitSet = {1,11,13}
    FOLLOW_expr_or_op_in_expr_or1331: org.antlr.runtime.BitSet = {6,8,10,18,25,32,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,79,80,233}
    FOLLOW_expr_shift_in_expr_comp1533: org.antlr.runtime.BitSet = {1,28,29,30,31,36,37,76,77,223,224,226,227}
    FOLLOW_expr_shift_in_expr_comp1540: org.antlr.runtime.BitSet = {1,28,29,30,31,36,37,76,77,223,224,226,227}
    FOLLOW_expr_term_in_expr_func2093: org.antlr.runtime.BitSet = {1}
    FOLLOW_expr_unary_in_expr_mult1880: org.antlr.runtime.BitSet = {1,8,26,33,208,221,225,231}
    FOLLOW_expr_unary_in_expr_mult1887: org.antlr.runtime.BitSet = {1,8,26,33,208,221,225,231}
    FOLLOW_expr_xor_in_expr_or1327: org.antlr.runtime.BitSet = {1,209}
    FOLLOW_expr_xor_in_expr_or1334: org.antlr.runtime.BitSet = {1,209}
    FOLLOW_expr_xor_op_in_expr_xor1372: org.antlr.runtime.BitSet = {6,8,10,18,25,32,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,79,80,233}
    FOLLOW_funcall_in_statement179: org.antlr.runtime.BitSet = {222}
    FOLLOW_goto_stmt_in_cond_stmt1090: org.antlr.runtime.BitSet = {1}
    FOLLOW_goto_stmt_in_statement197: org.antlr.runtime.BitSet = {222}
    FOLLOW_identifier_in_build_stmt928: org.antlr.runtime.BitSet = {1}
    FOLLOW_identifier_in_crossbuild_stmt956: org.antlr.runtime.BitSet = {1}
    FOLLOW_identifier_in_declaration601: org.antlr.runtime.BitSet = {15}
    FOLLOW_identifier_in_declaration627: org.antlr.runtime.BitSet = {1}
    FOLLOW_identifier_in_expr_apply2104: org.antlr.runtime.BitSet = {79}
    FOLLOW_identifier_in_jumpdest1001: org.antlr.runtime.BitSet = {1}
    FOLLOW_identifier_in_jumpdest1048: org.antlr.runtime.BitSet = {215}
    FOLLOW_identifier_in_label111: org.antlr.runtime.BitSet = {36}
    FOLLOW_identifier_in_lvalue652: org.antlr.runtime.BitSet = {15}
    FOLLOW_identifier_in_lvalue674: org.antlr.runtime.BitSet = {1}
    FOLLOW_identifier_in_section_def137: org.antlr.runtime.BitSet = {219}
    FOLLOW_identifier_in_sembitrange693: org.antlr.runtime.BitSet = {74}
    FOLLOW_identifier_in_sizedexport1167: org.antlr.runtime.BitSet = {1}
    FOLLOW_identifier_in_sizedstar741: org.antlr.runtime.BitSet = {215}
    FOLLOW_identifier_in_sizedstar769: org.antlr.runtime.BitSet = {215}
    FOLLOW_identifier_in_varnode2198: org.antlr.runtime.BitSet = {1}
    FOLLOW_identifier_in_varnode2225: org.antlr.runtime.BitSet = {15}
    FOLLOW_integer_in_constant2302: org.antlr.runtime.BitSet = {1}
    FOLLOW_integer_in_jumpdest1031: org.antlr.runtime.BitSet = {1}
    FOLLOW_integer_in_varnode2193: org.antlr.runtime.BitSet = {1}
    FOLLOW_integer_in_varnode2203: org.antlr.runtime.BitSet = {15}
    FOLLOW_jumpdest_in_call_stmt1116: org.antlr.runtime.BitSet = {1}
    FOLLOW_jumpdest_in_goto_stmt981: org.antlr.runtime.BitSet = {1}
    FOLLOW_label_in_jumpdest1065: org.antlr.runtime.BitSet = {1}
    FOLLOW_label_in_statement243: org.antlr.runtime.BitSet = {1}
    FOLLOW_lvalue_in_assignment544: org.antlr.runtime.BitSet = {7}
    FOLLOW_lvalue_in_assignment569: org.antlr.runtime.BitSet = {7}
    FOLLOW_mult_op_in_expr_mult1884: org.antlr.runtime.BitSet = {6,8,10,18,25,32,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,79,80,233}
    FOLLOW_outererror_in_statement253: org.antlr.runtime.BitSet = {1}
    FOLLOW_return_stmt_in_statement221: org.antlr.runtime.BitSet = {222}
    FOLLOW_section_def_in_statement248: org.antlr.runtime.BitSet = {1}
    FOLLOW_semantic_in_semanticbody34: org.antlr.runtime.BitSet = {214}
    FOLLOW_sembitrange_in_expr_term2162: org.antlr.runtime.BitSet = {1}
    FOLLOW_sembitrange_in_lvalue647: org.antlr.runtime.BitSet = {1}
    FOLLOW_shift_op_in_expr_shift1732: org.antlr.runtime.BitSet = {6,8,10,18,25,32,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,79,80,233}
    FOLLOW_sizedexport_in_export1182: org.antlr.runtime.BitSet = {1}
    FOLLOW_sizedstar_in_lvalue679: org.antlr.runtime.BitSet = {6,8,10,18,25,32,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,79,80,233}
    FOLLOW_sizedstar_in_sizedexport1164: org.antlr.runtime.BitSet = {40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72}
    FOLLOW_sizedstar_in_unary_op2077: org.antlr.runtime.BitSet = {1}
    FOLLOW_statement_in_statements95: org.antlr.runtime.BitSet = {1,6,7,8,11,12,13,14,15,16,23,26,27,28,29,30,31,32,33,34,35,37,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,75,76,77,79,80,81,208,209,210,215,216,220,221,222,223,224,225,226,227,231,232,233}
    FOLLOW_statements_in_code_block72: org.antlr.runtime.BitSet = {1}
    FOLLOW_unary_op_in_expr_unary2005: org.antlr.runtime.BitSet = {6,10,18,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,79}
    FOLLOW_varnode_in_crossbuild_stmt952: org.antlr.runtime.BitSet = {16}
    FOLLOW_varnode_in_export1200: org.antlr.runtime.BitSet = {1}
    FOLLOW_varnode_in_expr_term2157: org.antlr.runtime.BitSet = {1}
    FOLLOW_varnode_in_varnode2257: org.antlr.runtime.BitSet = {1}
    FOLLOW_varnode_in_varnode2282: org.antlr.runtime.BitSet = {1}
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
    gParent: ghidra.sleigh.grammar.SleighParser
    gSleighParser: ghidra.sleigh.grammar.SleighParser
    input: org.antlr.runtime.TokenStream




    class expr_add_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class expr_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class expr_or_op_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class expr_shift_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class code_block_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class expr_func_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class sizedexport_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class expr_comp_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class expr_apply_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class expr_boolor_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class expr_mult_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class return_stmt_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class add_op_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class shift_op_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class expr_boolor_op_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class expr_and_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class statements_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class expr_xor_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class call_stmt_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class booland_op_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class build_stmt_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class expr_eq_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class label_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class semanticbody_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class expr_xor_op_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class expr_operands_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class assignment_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class mult_op_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class compare_op_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class cond_stmt_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class declaration_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class eq_op_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class semantic_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class goto_stmt_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class expr_term_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class expr_and_op_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class unary_op_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class crossbuild_stmt_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class section_def_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class constant_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class statement_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class expr_unary_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class export_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class sizedstar_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class funcall_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class sembitrange_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class expr_or_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class lvalue_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class outererror_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class varnode_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class jumpdest_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...




    class expr_booland_return(org.antlr.runtime.ParserRuleReturnScope):
        start: org.antlr.runtime.Token
        stop: org.antlr.runtime.Token



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

        @property
        def tree(self) -> org.antlr.runtime.tree.CommonTree: ...

    @overload
    def __init__(self, input: org.antlr.runtime.TokenStream, gSleighParser: ghidra.sleigh.grammar.SleighParser): ...

    @overload
    def __init__(self, input: org.antlr.runtime.TokenStream, state: org.antlr.runtime.RecognizerSharedState, gSleighParser: ghidra.sleigh.grammar.SleighParser): ...



    def add_op(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.add_op_return: ...

    def alreadyParsedRule(self, __a0: org.antlr.runtime.IntStream, __a1: int) -> bool: ...

    def assignment(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.assignment_return: ...

    def beginResync(self) -> None: ...

    def booland_op(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.booland_op_return: ...

    def build_stmt(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.build_stmt_return: ...

    def call_stmt(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.call_stmt_return: ...

    def code_block(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.code_block_return: ...

    def compare_op(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.compare_op_return: ...

    def cond_stmt(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.cond_stmt_return: ...

    def constant(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.constant_return: ...

    @overload
    def consumeUntil(self, __a0: org.antlr.runtime.IntStream, __a1: int) -> None: ...

    @overload
    def consumeUntil(self, __a0: org.antlr.runtime.IntStream, __a1: org.antlr.runtime.BitSet) -> None: ...

    def crossbuild_stmt(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.crossbuild_stmt_return: ...

    def declaration(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.declaration_return: ...

    def displayRecognitionError(self, __a0: List[unicode], __a1: org.antlr.runtime.RecognitionException) -> None: ...

    def emitErrorMessage(self, msg: unicode) -> None: ...

    def endResync(self) -> None: ...

    def eq_op(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.eq_op_return: ...

    def equals(self, __a0: object) -> bool: ...

    def export(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.export_return: ...

    def expr(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.expr_return: ...

    def expr_add(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.expr_add_return: ...

    def expr_and(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.expr_and_return: ...

    def expr_and_op(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.expr_and_op_return: ...

    def expr_apply(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.expr_apply_return: ...

    def expr_booland(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.expr_booland_return: ...

    def expr_boolor(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.expr_boolor_return: ...

    def expr_boolor_op(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.expr_boolor_op_return: ...

    def expr_comp(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.expr_comp_return: ...

    def expr_eq(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.expr_eq_return: ...

    def expr_func(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.expr_func_return: ...

    def expr_mult(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.expr_mult_return: ...

    def expr_operands(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.expr_operands_return: ...

    def expr_or(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.expr_or_return: ...

    def expr_or_op(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.expr_or_op_return: ...

    def expr_shift(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.expr_shift_return: ...

    def expr_term(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.expr_term_return: ...

    def expr_unary(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.expr_unary_return: ...

    def expr_xor(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.expr_xor_return: ...

    def expr_xor_op(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.expr_xor_op_return: ...

    def failed(self) -> bool: ...

    def funcall(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.funcall_return: ...

    def getBacktrackingLevel(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getDelegates(self) -> List[ghidra.sleigh.grammar.AbstractSleighParser]: ...

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

    def getTokenStream(self) -> org.antlr.runtime.TokenStream: ...

    def getTreeAdaptor(self) -> org.antlr.runtime.tree.TreeAdaptor: ...

    def goto_stmt(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.goto_stmt_return: ...

    def hashCode(self) -> int: ...

    def jumpdest(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.jumpdest_return: ...

    def label(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.label_return: ...

    def lvalue(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.lvalue_return: ...

    def match(self, __a0: org.antlr.runtime.IntStream, __a1: int, __a2: org.antlr.runtime.BitSet) -> object: ...

    def matchAny(self, __a0: org.antlr.runtime.IntStream) -> None: ...

    def memoize(self, __a0: org.antlr.runtime.IntStream, __a1: int, __a2: int) -> None: ...

    def mismatchIsMissingToken(self, __a0: org.antlr.runtime.IntStream, __a1: org.antlr.runtime.BitSet) -> bool: ...

    def mismatchIsUnwantedToken(self, __a0: org.antlr.runtime.IntStream, __a1: int) -> bool: ...

    def mult_op(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.mult_op_return: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def outererror(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.outererror_return: ...

    def recover(self, __a0: org.antlr.runtime.IntStream, __a1: org.antlr.runtime.RecognitionException) -> None: ...

    def recoverFromMismatchedSet(self, __a0: org.antlr.runtime.IntStream, __a1: org.antlr.runtime.RecognitionException, __a2: org.antlr.runtime.BitSet) -> object: ...

    def reportError(self, __a0: org.antlr.runtime.RecognitionException) -> None: ...

    def reset(self) -> None: ...

    def return_stmt(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.return_stmt_return: ...

    def section_def(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.section_def_return: ...

    def semantic(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.semantic_return: ...

    def semanticbody(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.semanticbody_return: ...

    def sembitrange(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.sembitrange_return: ...

    def setBacktrackingLevel(self, __a0: int) -> None: ...

    def setEnv(self, env: ghidra.sleigh.grammar.ParsingEnvironment) -> None: ...

    def setLexer(self, lexer: ghidra.sleigh.grammar.SleighLexer) -> None: ...

    def setTokenStream(self, __a0: org.antlr.runtime.TokenStream) -> None: ...

    def setTreeAdaptor(self, adaptor: org.antlr.runtime.tree.TreeAdaptor) -> None: ...

    def shift_op(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.shift_op_return: ...

    def sizedexport(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.sizedexport_return: ...

    def sizedstar(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.sizedstar_return: ...

    def statement(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.statement_return: ...

    def statements(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.statements_return: ...

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

    def unary_op(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.unary_op_return: ...

    def varnode(self) -> ghidra.sleigh.grammar.SleighParser_SemanticParser.varnode_return: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def delegates(self) -> List[ghidra.sleigh.grammar.AbstractSleighParser]: ...

    @property
    def grammarFileName(self) -> unicode: ...

    @property
    def tokenNames(self) -> List[unicode]: ...

    @property
    def treeAdaptor(self) -> org.antlr.runtime.tree.TreeAdaptor: ...

    @treeAdaptor.setter
    def treeAdaptor(self, value: org.antlr.runtime.tree.TreeAdaptor) -> None: ...
