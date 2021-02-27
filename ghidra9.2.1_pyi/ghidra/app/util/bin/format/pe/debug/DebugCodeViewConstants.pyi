import java.lang


class DebugCodeViewConstants(object):
    """
    Constants defined in Code View Debug information.
    """

    SIGNATURE_DOT_NET: int = 21075
    SIGNATURE_N1: int = 20017
    SIGNATURE_NB: int = 20034
    S_ALIGN: int = 1026
    S_BLOCK16: int = 263
    S_BLOCK32: int = 519
    S_BPREL16: int = 256
    S_BPREL32: int = 512
    S_BPREL32_NEW: int = 4102
    S_CEXMODEL16: int = 266
    S_CEXMODEL32: int = 522
    S_COBOLUDT: int = 11
    S_COBOLUDT32: int = 4100
    S_COMPILE: int = 1
    S_CONSTANT: int = 3
    S_CONSTANT32: int = 4098
    S_CVRESERVE: int = 8
    S_DATAREF: int = 1025
    S_END: int = 6
    S_ENDARG: int = 10
    S_ENTRYTHIS: int = 14
    S_GDATA16: int = 258
    S_GDATA32: int = 514
    S_GDATA32_NEW: int = 4104
    S_GPROC16: int = 261
    S_GPROC32: int = 517
    S_GPROC32_NEW: int = 4107
    S_GPROCMIPS: int = 769
    S_GTHREAD32: int = 526
    S_GTHREAD32_NEW: int = 4111
    S_LABEL16: int = 265
    S_LABEL32: int = 521
    S_LDATA16: int = 257
    S_LDATA32: int = 513
    S_LDATA32_NEW: int = 4103
    S_LPROC16: int = 260
    S_LPROC32: int = 516
    S_LPROC32_NEW: int = 4106
    S_LPROCMIPS: int = 768
    S_LPROCREF: int = 1027
    S_LTHREAD32: int = 525
    S_LTHREAD32_NEW: int = 4110
    S_MANYREG: int = 12
    S_MANYREG32: int = 4101
    S_OBJNAME: int = 9
    S_PROCREF: int = 1024
    S_PUB16: int = 259
    S_PUB32: int = 515
    S_PUBSYM32_NEW: int = 4105
    S_REGISTER: int = 2
    S_REGISTER32: int = 4097
    S_REGREL16: int = 268
    S_REGREL32: int = 524
    S_REGREL32_NEW: int = 4109
    S_RETURN: int = 13
    S_SKIP: int = 7
    S_SLINK32: int = 527
    S_SSEARCH: int = 5
    S_THUNK16: int = 262
    S_THUNK32: int = 518
    S_UDT: int = 4
    S_UDT32: int = 4099
    S_VFTABLE16: int = 267
    S_VFTABLE32: int = 523
    S_VFTABLE32_NEW: int = 4108
    S_WITH16: int = 264
    S_WITH32: int = 520
    VERSION_09: int = 12345
    VERSION_10: int = 12592
    VERSION_11: int = 12593
    VERSION_12: int = 12608
    VERSION_13: int = 12528
    VERSION_DOT_NET: int = 17491
    sstAlignSym: int = 293
    sstFileIndex: int = 307
    sstGlobalPub: int = 298
    sstGlobalSym: int = 297
    sstGlobalTypes: int = 299
    sstLibraries: int = 296
    sstMPC: int = 300
    sstModule: int = 288
    sstOffsetMap16: int = 305
    sstOffsetMap32: int = 306
    sstPreComp: int = 303
    sstPreCompMap: int = 304
    sstPublic: int = 290
    sstPublicSym: int = 291
    sstSegMap: int = 301
    sstSegName: int = 302
    sstSrcLnSeg: int = 294
    sstSrcModule: int = 295
    sstStaticSym: int = 308
    sstSymbols: int = 292
    sstTypes: int = 289







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
