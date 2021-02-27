import java.lang


class ElfConstants(object):
    """
    A collection of constants used in the ELF header.
    """

    EI_ABIVERSION: int = 8
    EI_CLASS: int = 4
    EI_DATA: int = 5
    EI_MAG0: int = 0
    EI_MAG1: int = 1
    EI_MAG2: int = 2
    EI_MAG3: int = 3
    EI_NIDENT: int = 16
    EI_OSIABI: int = 7
    EI_PAD: int = 9
    EI_VERSION: int = 6
    ELFOSABI_AIX: int = 7
    ELFOSABI_ARM: int = 97
    ELFOSABI_AROS: int = 15
    ELFOSABI_C6000_ELFABI: int = 64
    ELFOSABI_C6000_LINUX: int = 65
    ELFOSABI_CLOUDABI: int = 17
    ELFOSABI_FENIXOS: int = 16
    ELFOSABI_FREEBSD: int = 9
    ELFOSABI_GNU: int = 3
    ELFOSABI_HPUX: int = 1
    ELFOSABI_HURD: int = 4
    ELFOSABI_IRIX: int = 8
    ELFOSABI_LINUX: int = 3
    ELFOSABI_MODESTO: int = 11
    ELFOSABI_NETBSD: int = 2
    ELFOSABI_NONE: int = 0
    ELFOSABI_NSK: int = 14
    ELFOSABI_OPENBSD: int = 12
    ELFOSABI_OPENVMS: int = 13
    ELFOSABI_SOLARIS: int = 6
    ELFOSABI_STANDALONE: int = -1
    ELFOSABI_TRUE64: int = 10
    ELF_CLASS_32: int = 1
    ELF_CLASS_64: int = 2
    ELF_CLASS_NONE: int = 0
    ELF_CLASS_NUM: int = 3
    ELF_DATA_BE: int = 2
    ELF_DATA_LE: int = 1
    ELF_DATA_NONE: int = 0
    EM_386: int = 3
    EM_486: int = 6
    EM_56800EX: int = 200
    EM_68HC05: int = 72
    EM_68HC08: int = 71
    EM_68HC11: int = 70
    EM_68HC12: int = 53
    EM_68HC16: int = 69
    EM_68K: int = 4
    EM_78KOR: int = 199
    EM_8051: int = 165
    EM_860: int = 7
    EM_88K: int = 5
    EM_960: int = 19
    EM_AARCH64: int = 183
    EM_ALTERA_NIOS2: int = 113
    EM_AMDGPU: int = 224
    EM_ARC: int = 45
    EM_ARCA: int = 109
    EM_ARC_A5: int = 93
    EM_ARC_COMPACT2: int = 195
    EM_ARM: int = 40
    EM_AVR: int = 83
    EM_AVR32: int = 185
    EM_AVR32_unofficial: int = 6317
    EM_BA1: int = 201
    EM_BA2: int = 202
    EM_BLACKFIN: int = 106
    EM_BPF: int = 247
    EM_C166: int = 116
    EM_CDP: int = 215
    EM_CE: int = 119
    EM_CLOUDSHIELD: int = 192
    EM_COGE: int = 216
    EM_COLDFIRE: int = 52
    EM_COOL: int = 217
    EM_COREA_1ST: int = 193
    EM_COREA_2ND: int = 194
    EM_CR: int = 103
    EM_CR16: int = 177
    EM_CRAYNV2: int = 172
    EM_CRIS: int = 76
    EM_CRX: int = 114
    EM_CSR_KALIMBA: int = 219
    EM_CUDA: int = 190
    EM_CYPRESS_M8C: int = 161
    EM_D10V: int = 85
    EM_D30V: int = 86
    EM_DSP24: int = 136
    EM_DSPIC30F: int = 118
    EM_DXP: int = 112
    EM_ECOG1: int = 168
    EM_ECOG16: int = 176
    EM_ECOG1X: int = 168
    EM_ECOG2: int = 134
    EM_ETPU: int = 178
    EM_EXCESS: int = 111
    EM_F2MC16: int = 104
    EM_FAKE_ALPHA: int = 41
    EM_FIREPATH: int = 78
    EM_FR20: int = 37
    EM_FR30: int = 84
    EM_FX66: int = 66
    EM_H8S: int = 48
    EM_H8_300: int = 46
    EM_H8_300H: int = 47
    EM_H8_500: int = 49
    EM_HEXAGON: int = 164
    EM_HUANY: int = 81
    EM_IA_64: int = 50
    EM_IP2K: int = 101
    EM_JAVELIN: int = 77
    EM_K10M: int = 181
    EM_KM32: int = 210
    EM_KMX16: int = 212
    EM_KMX32: int = 211
    EM_KMX8: int = 213
    EM_KVARC: int = 214
    EM_L10M: int = 180
    EM_LANAI: int = 244
    EM_LATTICEMICO32: int = 138
    EM_M16C: int = 117
    EM_M32: int = 1
    EM_M32C: int = 120
    EM_M32R: int = 88
    EM_MANIK: int = 171
    EM_MAX: int = 102
    EM_MAXQ30: int = 169
    EM_MCHP_PIC: int = 204
    EM_MCST_ELBRUS: int = 175
    EM_ME16: int = 59
    EM_METAG: int = 174
    EM_MIPS: int = 8
    EM_MIPS_RS3_LE: int = 10
    EM_MIPS_X: int = 51
    EM_MMA: int = 54
    EM_MMDSP_PLUS: int = 160
    EM_MMIX: int = 80
    EM_MN10200: int = 90
    EM_MN10300: int = 89
    EM_MSP430: int = 105
    EM_NCPU: int = 56
    EM_NDR1: int = 57
    EM_NDS32: int = 167
    EM_NONE: int = 0
    EM_NORC: int = 218
    EM_NS32K: int = 97
    EM_OPEN8: int = 196
    EM_OPENRISC: int = 92
    EM_PARISC: int = 15
    EM_PCP: int = 55
    EM_PDP10: int = 64
    EM_PDP11: int = 65
    EM_PDSP: int = 63
    EM_PJ: int = 91
    EM_PPC: int = 20
    EM_PPC64: int = 21
    EM_PRISM: int = 82
    EM_R32C: int = 162
    EM_RCE: int = 39
    EM_RH32: int = 38
    EM_RISCV: int = 243
    EM_RL78: int = 197
    EM_RS08: int = 132
    EM_RX: int = 173
    EM_S370: int = 9
    EM_S390: int = 22
    EM_SCORE7: int = 135
    EM_SEP: int = 108
    EM_SE_C17: int = 139
    EM_SE_C33: int = 107
    EM_SH: int = 42
    EM_SHARC: int = 133
    EM_SLE9X: int = 179
    EM_SNP1K: int = 99
    EM_SPARC: int = 2
    EM_SPARC32PLUS: int = 18
    EM_SPARCV9: int = 43
    EM_SPU: int = 23
    EM_ST100: int = 60
    EM_ST19: int = 74
    EM_ST200: int = 100
    EM_ST7: int = 68
    EM_ST9PLUS: int = 67
    EM_STARCORE: int = 58
    EM_STM8: int = 186
    EM_STXP7X: int = 166
    EM_SVX: int = 73
    EM_TILE64: int = 187
    EM_TILEGX: int = 191
    EM_TILEPRO: int = 188
    EM_TINYJ: int = 61
    EM_TI_C2000: int = 141
    EM_TI_C5500: int = 142
    EM_TI_C6000: int = 140
    EM_TMM_GPP: int = 96
    EM_TPC: int = 98
    EM_TRICORE: int = 44
    EM_TRIMEDIA: int = 163
    EM_TSK3000: int = 131
    EM_UNICORE: int = 110
    EM_V800: int = 36
    EM_V850: int = 87
    EM_VAX: int = 75
    EM_VIDEOCORE: int = 95
    EM_VIDEOCORE3: int = 137
    EM_VIDEOCORE5: int = 198
    EM_VPP500: int = 17
    EM_X86_64: int = 62
    EM_XCORE: int = 203
    EM_XGATE: int = 115
    EM_XIMO16: int = 170
    EM_XTENSA: int = 94
    EM_ZSP: int = 79
    ET_CORE: int = 4
    ET_DYN: int = 3
    ET_EXEC: int = 2
    ET_HIPROC: int = -1
    ET_LOPROC: int = -256
    ET_NONE: int = 0
    ET_REL: int = 1
    EV_CURRENT: int = 1
    EV_NONE: int = 0
    MAGIC_BYTES: List[int] = array('b', [127, 69, 76, 70])
    MAGIC_NUM: int = 127
    MAGIC_STR: unicode = u'ELF'
    MAGIC_STR_LEN: int = 3
    PLT_ENTRY_SIZE: int = 16







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
