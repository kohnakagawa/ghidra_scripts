import ghidra.program.model.data
import java.lang


class PrimitiveTypeListing(object):
    """
    A class to convert from debug data types into Ghidra data types.
    """

    T_32PBOOL08: int = 1072
    T_32PBOOL16: int = 1073
    T_32PBOOL32: int = 1074
    T_32PBOOL64: int = 1075
    T_32PCHAR: int = 1040
    T_32PCPLX32: int = 1104
    T_32PCPLX64: int = 1105
    T_32PFBOOL08: int = 1328
    T_32PFBOOL16: int = 1329
    T_32PFBOOL32: int = 1330
    T_32PFBOOL64: int = 1331
    T_32PFCHAR: int = 1296
    T_32PFCPLX32: int = 1360
    T_32PFCPLX64: int = 1361
    T_32PFINT2: int = 1394
    T_32PFINT4: int = 1396
    T_32PFINT8: int = 1398
    T_32PFQUAD: int = 1299
    T_32PFRCHAR: int = 1392
    T_32PFREAL32: int = 1344
    T_32PFREAL64: int = 1345
    T_32PFSHORT: int = 1297
    T_32PFUCHAR: int = 1312
    T_32PFUINT2: int = 1395
    T_32PFUINT4: int = 1397
    T_32PFUINT8: int = 1399
    T_32PFULONG: int = 1314
    T_32PFUQUAD: int = 1315
    T_32PFUSHORT: int = 1313
    T_32PFVOID: int = 1283
    T_32PFWCHAR: int = 1393
    T_32PINT2: int = 1138
    T_32PINT4: int = 1140
    T_32PINT8: int = 1142
    T_32PLONG: int = 1042
    T_32PQUAD: int = 1043
    T_32PRCHAR: int = 1136
    T_32PREAL32: int = 1088
    T_32PREAL64: int = 1089
    T_32PSHORT: int = 1041
    T_32PUCHAR: int = 1056
    T_32PUINT2: int = 1139
    T_32PUINT4: int = 1141
    T_32PUINT8: int = 1143
    T_32PULONG: int = 1058
    T_32PUQUAD: int = 1059
    T_32PUSHORT: int = 1057
    T_32PVOID: int = 1027
    T_32PWCHAR: int = 1137
    T_ABS: int = 1
    T_BIT: int = 96
    T_BOOL08: int = 48
    T_BOOL16: int = 49
    T_BOOL32: int = 50
    T_BOOL64: int = 51
    T_CHAR: int = 16
    T_CPLX32: int = 80
    T_CPLX64: int = 81
    T_CURRENCY: int = 4
    T_FBASICSTR: int = 6
    T_HINSTANCE: int = 4349
    T_INT2: int = 114
    T_INT4: int = 116
    T_INT8: int = 118
    T_LONG: int = 18
    T_NBASICSTR: int = 5
    T_NOTTRANS: int = 7
    T_NOTYPE: int = 0
    T_P2PFLONG: int = 1298
    T_PASCHAR: int = 97
    T_PBOOL08: int = 304
    T_PBOOL16: int = 305
    T_PBOOL32: int = 306
    T_PBOOL64: int = 307
    T_PCHAR: int = 272
    T_PCPLX32: int = 336
    T_PCPLX64: int = 337
    T_PFBOOL08: int = 560
    T_PFBOOL16: int = 561
    T_PFBOOL32: int = 562
    T_PFBOOL64: int = 563
    T_PFCHAR: int = 528
    T_PFCPLX32: int = 592
    T_PFCPLX64: int = 593
    T_PFINT2: int = 626
    T_PFINT4: int = 628
    T_PFINT8: int = 630
    T_PFLONG: int = 530
    T_PFOID: int = 515
    T_PFQUAD: int = 531
    T_PFRCHAR: int = 624
    T_PFREAL32: int = 576
    T_PFREAL64: int = 577
    T_PFSHORT: int = 529
    T_PFUCHAR: int = 544
    T_PFUINT2: int = 627
    T_PFUINT4: int = 629
    T_PFUINT8: int = 631
    T_PFULONG: int = 546
    T_PFUQUAD: int = 547
    T_PFUSHORT: int = 545
    T_PFWCHAR: int = 625
    T_PHBOOL08: int = 816
    T_PHBOOL16: int = 817
    T_PHBOOL32: int = 818
    T_PHBOOL64: int = 819
    T_PHCHAR: int = 784
    T_PHCPLX32: int = 848
    T_PHCPLX64: int = 849
    T_PHINT2: int = 882
    T_PHINT4: int = 884
    T_PHINT8: int = 886
    T_PHLONG: int = 786
    T_PHQUAD: int = 787
    T_PHRCHAR: int = 880
    T_PHREAL32: int = 832
    T_PHREAL64: int = 833
    T_PHSHORT: int = 785
    T_PHUCHAR: int = 800
    T_PHUINT2: int = 883
    T_PHUINT4: int = 885
    T_PHUINT8: int = 887
    T_PHULONG: int = 802
    T_PHUQUAD: int = 803
    T_PHUSHORT: int = 801
    T_PHVOID: int = 771
    T_PHWCHAR: int = 881
    T_PINT2: int = 370
    T_PINT4: int = 372
    T_PINT8: int = 374
    T_PLONG: int = 274
    T_PQUAD: int = 275
    T_PRCHAR: int = 368
    T_PREAL32: int = 320
    T_PREAL64: int = 321
    T_PSHORT: int = 273
    T_PUCHAR: int = 288
    T_PUINT2: int = 371
    T_PUINT4: int = 373
    T_PUINT8: int = 375
    T_PULONG: int = 290
    T_PUQUAD: int = 291
    T_PUSHORT: int = 289
    T_PVOID: int = 259
    T_PWCHAR: int = 369
    T_QUAD: int = 19
    T_RCHAR: int = 112
    T_REAL32: int = 64
    T_REAL64: int = 65
    T_SEGMENT: int = 2
    T_SHORT: int = 17
    T_UCHAR: int = 32
    T_UINT2: int = 115
    T_UINT4: int = 117
    T_UINT8: int = 119
    T_ULONG: int = 34
    T_UQUAD: int = 35
    T_USHORT: int = 33
    T_VOID: int = 3
    T_WCHAR: int = 113



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getDataType(type: int) -> ghidra.program.model.data.DataType: ...

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
