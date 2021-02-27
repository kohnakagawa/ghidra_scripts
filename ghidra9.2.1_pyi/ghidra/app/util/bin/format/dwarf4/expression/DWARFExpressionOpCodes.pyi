from typing import List
import ghidra.app.util.bin.format.dwarf4.expression
import java.lang


class DWARFExpressionOpCodes(object):
    """
    DWARF expression opcode consts from www.dwarfstd.org/doc/DWARF4.pdf
    """

    BLOBONLY_OPERANDTYPES: List[ghidra.app.util.bin.format.dwarf4.expression.DWARFExpressionOperandType] = array(ghidra.app.util.bin.format.dwarf4.expression.DWARFExpressionOperandType, [SIZED_BLOB])
    DW_OP_abs: int = 25
    DW_OP_addr: int = 3
    DW_OP_and: int = 26
    DW_OP_bit_piece: int = 157
    DW_OP_bra: int = 40
    DW_OP_breg0: int = 112
    DW_OP_breg1: int = 113
    DW_OP_breg10: int = 122
    DW_OP_breg11: int = 123
    DW_OP_breg12: int = 124
    DW_OP_breg13: int = 125
    DW_OP_breg14: int = 126
    DW_OP_breg15: int = 127
    DW_OP_breg16: int = 128
    DW_OP_breg17: int = 129
    DW_OP_breg18: int = 130
    DW_OP_breg19: int = 131
    DW_OP_breg2: int = 114
    DW_OP_breg20: int = 132
    DW_OP_breg21: int = 133
    DW_OP_breg22: int = 134
    DW_OP_breg23: int = 135
    DW_OP_breg24: int = 136
    DW_OP_breg25: int = 137
    DW_OP_breg26: int = 138
    DW_OP_breg27: int = 139
    DW_OP_breg28: int = 140
    DW_OP_breg29: int = 141
    DW_OP_breg3: int = 115
    DW_OP_breg30: int = 142
    DW_OP_breg31: int = 143
    DW_OP_breg4: int = 116
    DW_OP_breg5: int = 117
    DW_OP_breg6: int = 118
    DW_OP_breg7: int = 119
    DW_OP_breg8: int = 120
    DW_OP_breg9: int = 121
    DW_OP_bregx: int = 146
    DW_OP_call2: int = 152
    DW_OP_call4: int = 153
    DW_OP_call_frame_cfa: int = 156
    DW_OP_call_ref: int = 154
    DW_OP_const1s: int = 9
    DW_OP_const1u: int = 8
    DW_OP_const2s: int = 11
    DW_OP_const2u: int = 10
    DW_OP_const4s: int = 13
    DW_OP_const4u: int = 12
    DW_OP_const8s: int = 15
    DW_OP_const8u: int = 14
    DW_OP_consts: int = 17
    DW_OP_constu: int = 16
    DW_OP_deref: int = 6
    DW_OP_deref_size: int = 148
    DW_OP_div: int = 27
    DW_OP_drop: int = 19
    DW_OP_dup: int = 18
    DW_OP_eq: int = 41
    DW_OP_fbreg: int = 145
    DW_OP_form_tls_address: int = 155
    DW_OP_ge: int = 42
    DW_OP_gt: int = 43
    DW_OP_hi_user: int = 255
    DW_OP_implicit_value: int = 158
    DW_OP_le: int = 44
    DW_OP_lit0: int = 48
    DW_OP_lit1: int = 49
    DW_OP_lit10: int = 58
    DW_OP_lit11: int = 59
    DW_OP_lit12: int = 60
    DW_OP_lit13: int = 61
    DW_OP_lit14: int = 62
    DW_OP_lit15: int = 63
    DW_OP_lit16: int = 64
    DW_OP_lit17: int = 65
    DW_OP_lit18: int = 66
    DW_OP_lit19: int = 67
    DW_OP_lit2: int = 50
    DW_OP_lit20: int = 68
    DW_OP_lit21: int = 69
    DW_OP_lit22: int = 70
    DW_OP_lit23: int = 71
    DW_OP_lit24: int = 72
    DW_OP_lit25: int = 73
    DW_OP_lit26: int = 74
    DW_OP_lit27: int = 75
    DW_OP_lit28: int = 76
    DW_OP_lit29: int = 77
    DW_OP_lit3: int = 51
    DW_OP_lit30: int = 78
    DW_OP_lit31: int = 79
    DW_OP_lit4: int = 52
    DW_OP_lit5: int = 53
    DW_OP_lit6: int = 54
    DW_OP_lit7: int = 55
    DW_OP_lit8: int = 56
    DW_OP_lit9: int = 57
    DW_OP_lo_user: int = 224
    DW_OP_lt: int = 45
    DW_OP_minus: int = 28
    DW_OP_mod: int = 29
    DW_OP_mul: int = 30
    DW_OP_ne: int = 46
    DW_OP_neg: int = 31
    DW_OP_nop: int = 150
    DW_OP_not: int = 32
    DW_OP_or: int = 33
    DW_OP_over: int = 20
    DW_OP_pick: int = 21
    DW_OP_piece: int = 147
    DW_OP_plus: int = 34
    DW_OP_plus_uconst: int = 35
    DW_OP_push_object_address: int = 151
    DW_OP_reg0: int = 80
    DW_OP_reg1: int = 81
    DW_OP_reg10: int = 90
    DW_OP_reg11: int = 91
    DW_OP_reg12: int = 92
    DW_OP_reg13: int = 93
    DW_OP_reg14: int = 94
    DW_OP_reg15: int = 95
    DW_OP_reg16: int = 96
    DW_OP_reg17: int = 97
    DW_OP_reg18: int = 98
    DW_OP_reg19: int = 99
    DW_OP_reg2: int = 82
    DW_OP_reg20: int = 100
    DW_OP_reg21: int = 101
    DW_OP_reg22: int = 102
    DW_OP_reg23: int = 103
    DW_OP_reg24: int = 104
    DW_OP_reg25: int = 105
    DW_OP_reg26: int = 106
    DW_OP_reg27: int = 107
    DW_OP_reg28: int = 108
    DW_OP_reg29: int = 109
    DW_OP_reg3: int = 83
    DW_OP_reg30: int = 110
    DW_OP_reg31: int = 111
    DW_OP_reg4: int = 84
    DW_OP_reg5: int = 85
    DW_OP_reg6: int = 86
    DW_OP_reg7: int = 87
    DW_OP_reg8: int = 88
    DW_OP_reg9: int = 89
    DW_OP_regx: int = 144
    DW_OP_rot: int = 23
    DW_OP_shl: int = 36
    DW_OP_shr: int = 37
    DW_OP_shra: int = 38
    DW_OP_skip: int = 47
    DW_OP_stack_value: int = 159
    DW_OP_swap: int = 22
    DW_OP_xderef: int = 24
    DW_OP_xderef_size: int = 149
    DW_OP_xor: int = 39
    EMPTY_OPERANDTYPES: List[ghidra.app.util.bin.format.dwarf4.expression.DWARFExpressionOperandType] = array(ghidra.app.util.bin.format.dwarf4.expression.DWARFExpressionOperandType)
    UNSUPPORTED_OPCODES: java.util.Set = []
    UNSUPPORTED_OPCODES_LIST: List[int] = array('i', [148, 24, 149, 151, 155, 152, 153, 154, 158])



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getOperandTypesFor(opcode: int) -> List[ghidra.app.util.bin.format.dwarf4.expression.DWARFExpressionOperandType]: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isValidOpcode(opcode: int) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def toString(opcode: int) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
