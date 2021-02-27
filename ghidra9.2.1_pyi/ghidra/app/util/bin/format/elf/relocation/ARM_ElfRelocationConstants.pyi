import java.lang


class ARM_ElfRelocationConstants(object):
    R_ARM_ABS12: int = 6
    R_ARM_ABS16: int = 5
    R_ARM_ABS32: int = 2
    R_ARM_ABS32_NOI: int = 55
    R_ARM_ABS_8: int = 8
    R_ARM_ALU_PCREL_15_8: int = 33
    R_ARM_ALU_PCREL_23_15: int = 34
    R_ARM_ALU_PCREL_7_0: int = 32
    R_ARM_ALU_PC_G0: int = 58
    R_ARM_ALU_PC_G0_NC: int = 57
    R_ARM_ALU_PC_G1: int = 60
    R_ARM_ALU_PC_G1_NC: int = 59
    R_ARM_ALU_PC_G2: int = 61
    R_ARM_ALU_SBREL_19_12_NC: int = 36
    R_ARM_ALU_SBREL_27_20_CK: int = 37
    R_ARM_ALU_SB_G0: int = 71
    R_ARM_ALU_SB_G0_NC: int = 70
    R_ARM_ALU_SB_G1: int = 73
    R_ARM_ALU_SB_G1_NC: int = 72
    R_ARM_ALU_SB_G2: int = 74
    R_ARM_BASE_ABS: int = 31
    R_ARM_BASE_PREL: int = 25
    R_ARM_BREL_ADJ: int = 12
    R_ARM_CALL: int = 28
    R_ARM_COPY: int = 20
    R_ARM_GLOB_DAT: int = 21
    R_ARM_GNU_VTENTRY: int = 100
    R_ARM_GNU_VTINHERIT: int = 101
    R_ARM_GOTOFF12: int = 98
    R_ARM_GOTOFF32: int = 24
    R_ARM_GOTRELAX: int = 99
    R_ARM_GOT_ABS: int = 95
    R_ARM_GOT_BREL: int = 26
    R_ARM_GOT_BREL12: int = 97
    R_ARM_GOT_PLT32: int = 27
    R_ARM_GOT_PREL: int = 96
    R_ARM_JUMP24: int = 29
    R_ARM_JUMP_SLOT: int = 22
    R_ARM_LDC_PC_G0: int = 67
    R_ARM_LDC_PC_G1: int = 68
    R_ARM_LDC_PC_G2: int = 69
    R_ARM_LDC_SB_G0: int = 81
    R_ARM_LDC_SB_G1: int = 82
    R_ARM_LDC_SB_G2: int = 83
    R_ARM_LDRS_PC_G0: int = 64
    R_ARM_LDRS_PC_G1: int = 65
    R_ARM_LDRS_PC_G2: int = 66
    R_ARM_LDRS_SB_G0: int = 78
    R_ARM_LDRS_SB_G1: int = 79
    R_ARM_LDRS_SB_G2: int = 80
    R_ARM_LDR_PC_G0: int = 4
    R_ARM_LDR_PC_G1: int = 62
    R_ARM_LDR_PC_G2: int = 63
    R_ARM_LDR_SBREL_11_0_NC: int = 35
    R_ARM_LDR_SB_G0: int = 75
    R_ARM_LDR_SB_G1: int = 76
    R_ARM_LDR_SB_G2: int = 77
    R_ARM_ME_TOO: int = 128
    R_ARM_MOVT_ABS: int = 44
    R_ARM_MOVT_BREL: int = 85
    R_ARM_MOVT_PREL: int = 46
    R_ARM_MOVW_ABS_NC: int = 43
    R_ARM_MOVW_BREL: int = 86
    R_ARM_MOVW_BREL_NC: int = 84
    R_ARM_MOVW_PREL_NC: int = 45
    R_ARM_NONE: int = 0
    R_ARM_PC24: int = 1
    R_ARM_PLT32_ABS: int = 94
    R_ARM_PREL31: int = 42
    R_ARM_PRIVATE_0: int = 112
    R_ARM_PRIVATE_1: int = 113
    R_ARM_PRIVATE_10: int = 122
    R_ARM_PRIVATE_11: int = 123
    R_ARM_PRIVATE_12: int = 124
    R_ARM_PRIVATE_13: int = 125
    R_ARM_PRIVATE_14: int = 126
    R_ARM_PRIVATE_15: int = 127
    R_ARM_PRIVATE_2: int = 114
    R_ARM_PRIVATE_3: int = 115
    R_ARM_PRIVATE_4: int = 116
    R_ARM_PRIVATE_5: int = 117
    R_ARM_PRIVATE_6: int = 118
    R_ARM_PRIVATE_7: int = 119
    R_ARM_PRIVATE_8: int = 120
    R_ARM_PRIVATE_9: int = 121
    R_ARM_REL32: int = 3
    R_ARM_REL32_NOI: int = 56
    R_ARM_RELATIVE: int = 23
    R_ARM_SBREL31: int = 39
    R_ARM_SBREL32: int = 9
    R_ARM_TARGET1: int = 38
    R_ARM_TARGET2: int = 41
    R_ARM_THM_ABS5: int = 7
    R_ARM_THM_ALU_PREL_11_0: int = 53
    R_ARM_THM_CALL: int = 10
    R_ARM_THM_JUMP11: int = 102
    R_ARM_THM_JUMP19: int = 51
    R_ARM_THM_JUMP24: int = 30
    R_ARM_THM_JUMP6: int = 52
    R_ARM_THM_JUMP8: int = 103
    R_ARM_THM_MOVT_ABS: int = 48
    R_ARM_THM_MOVT_BREL: int = 88
    R_ARM_THM_MOVT_PREL: int = 50
    R_ARM_THM_MOVW_ABS_NC: int = 47
    R_ARM_THM_MOVW_BREL: int = 89
    R_ARM_THM_MOVW_BREL_NC: int = 87
    R_ARM_THM_MOVW_PREL_NC: int = 49
    R_ARM_THM_PC12: int = 54
    R_ARM_THM_PC8: int = 11
    R_ARM_THM_SWI8: int = 14
    R_ARM_THM_TLS_CALL: int = 93
    R_ARM_THM_TLS_DESCSEQ16: int = 129
    R_ARM_THM_TLS_DESCSEQ32: int = 130
    R_ARM_THM_XPC22: int = 16
    R_ARM_TLS_CALL: int = 91
    R_ARM_TLS_DESC: int = 13
    R_ARM_TLS_DESCSEQ: int = 92
    R_ARM_TLS_DTPMOD32: int = 17
    R_ARM_TLS_DTPOFF32: int = 18
    R_ARM_TLS_GD32: int = 104
    R_ARM_TLS_GOTDESC: int = 90
    R_ARM_TLS_IE12GP: int = 111
    R_ARM_TLS_IE32: int = 107
    R_ARM_TLS_LDM32: int = 105
    R_ARM_TLS_LDO12: int = 109
    R_ARM_TLS_LDO32: int = 106
    R_ARM_TLS_LE12: int = 110
    R_ARM_TLS_LE32: int = 108
    R_ARM_TLS_TPOFF32: int = 19
    R_ARM_V4BX: int = 40
    R_ARM_XPC25: int = 15







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
