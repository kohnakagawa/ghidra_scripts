import java.lang


class MIPS_ElfRelocationConstants(object):
    MIPS_LOW26: int = 67108863
    R_MICROMIPS_26_S1: int = 133
    R_MICROMIPS_CALL16: int = 142
    R_MICROMIPS_CALL_HI16: int = 153
    R_MICROMIPS_CALL_LO16: int = 154
    R_MICROMIPS_GOT16: int = 138
    R_MICROMIPS_GOT_DISP: int = 145
    R_MICROMIPS_GOT_HI16: int = 148
    R_MICROMIPS_GOT_LO16: int = 149
    R_MICROMIPS_GOT_OFST: int = 147
    R_MICROMIPS_GOT_PAGE: int = 146
    R_MICROMIPS_GPREL16: int = 136
    R_MICROMIPS_GPREL7_S2: int = 172
    R_MICROMIPS_HI: int = 173
    R_MICROMIPS_HI0_LO16: int = 157
    R_MICROMIPS_HI16: int = 134
    R_MICROMIPS_HIGHER: int = 151
    R_MICROMIPS_HIGHEST: int = 152
    R_MICROMIPS_JALR: int = 156
    R_MICROMIPS_LITERAL: int = 137
    R_MICROMIPS_LO: int = 133
    R_MICROMIPS_LO16: int = 135
    R_MICROMIPS_PC10_S1: int = 140
    R_MICROMIPS_PC16_S1: int = 141
    R_MICROMIPS_PC23_S2: int = 173
    R_MICROMIPS_PC7_S1: int = 139
    R_MICROMIPS_SCN_DISP: int = 155
    R_MICROMIPS_SUB: int = 150
    R_MICROMIPS_TLS_DTPREL_HI16: int = 164
    R_MICROMIPS_TLS_DTPREL_LO16: int = 165
    R_MICROMIPS_TLS_GD: int = 162
    R_MICROMIPS_TLS_GOTTPREL: int = 166
    R_MICROMIPS_TLS_LDM: int = 163
    R_MICROMIPS_TLS_TPREL_HI16: int = 169
    R_MICROMIPS_TLS_TPREL_LO16: int = 170
    R_MIPS16_26: int = 100
    R_MIPS16_CALL16: int = 103
    R_MIPS16_GOT16: int = 102
    R_MIPS16_GPREL: int = 101
    R_MIPS16_HI: int = 112
    R_MIPS16_HI16: int = 104
    R_MIPS16_LO: int = 100
    R_MIPS16_LO16: int = 105
    R_MIPS16_TLS_DTPREL_HI16: int = 108
    R_MIPS16_TLS_DTPREL_LO16: int = 109
    R_MIPS16_TLS_GD: int = 106
    R_MIPS16_TLS_GOTTPREL: int = 110
    R_MIPS16_TLS_LDM: int = 107
    R_MIPS16_TLS_TPREL_HI16: int = 111
    R_MIPS16_TLS_TPREL_LO16: int = 112
    R_MIPS_16: int = 1
    R_MIPS_26: int = 4
    R_MIPS_32: int = 2
    R_MIPS_64: int = 18
    R_MIPS_ADD_IMMEDIATE: int = 34
    R_MIPS_CALL16: int = 11
    R_MIPS_CALL_HI16: int = 30
    R_MIPS_CALL_LO16: int = 31
    R_MIPS_COPY: int = 126
    R_MIPS_DELETE: int = 27
    R_MIPS_GLOB_DAT: int = 51
    R_MIPS_GOT16: int = 9
    R_MIPS_GOT_DISP: int = 19
    R_MIPS_GOT_HI16: int = 22
    R_MIPS_GOT_LO16: int = 23
    R_MIPS_GOT_OFST: int = 21
    R_MIPS_GOT_PAGE: int = 20
    R_MIPS_GPREL16: int = 7
    R_MIPS_GPREL32: int = 12
    R_MIPS_HI16: int = 5
    R_MIPS_HIGHER: int = 28
    R_MIPS_HIGHEST: int = 29
    R_MIPS_INSERT_A: int = 25
    R_MIPS_INSERT_B: int = 26
    R_MIPS_JALR: int = 37
    R_MIPS_JUMP_SLOT: int = 127
    R_MIPS_LITERAL: int = 8
    R_MIPS_LO16: int = 6
    R_MIPS_NONE: int = 0
    R_MIPS_PC16: int = 10
    R_MIPS_PC32: int = 248
    R_MIPS_PJUMP: int = 35
    R_MIPS_REL16: int = 33
    R_MIPS_REL32: int = 3
    R_MIPS_RELGOT: int = 36
    R_MIPS_SCN_DISP: int = 32
    R_MIPS_SHIFT5: int = 16
    R_MIPS_SHIFT6: int = 17
    R_MIPS_SUB: int = 24
    R_MIPS_TLS_DTPMOD32: int = 38
    R_MIPS_TLS_DTPMOD64: int = 40
    R_MIPS_TLS_DTPREL32: int = 39
    R_MIPS_TLS_DTPREL64: int = 41
    R_MIPS_TLS_DTPREL_HI16: int = 44
    R_MIPS_TLS_DTPREL_LO16: int = 45
    R_MIPS_TLS_GD: int = 42
    R_MIPS_TLS_GOTTPREL: int = 46
    R_MIPS_TLS_LDM: int = 43
    R_MIPS_TLS_TPREL32: int = 47
    R_MIPS_TLS_TPREL64: int = 48
    R_MIPS_TLS_TPREL_HI16: int = 49
    R_MIPS_TLS_TPREL_LO16: int = 50
    R_MIPS_UNUSED1: int = 13
    R_MIPS_UNUSED2: int = 14
    R_MIPS_UNUSED3: int = 15







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
