import java.lang


class Img3Constants(object):
    IMG3_SIGNATURE: unicode = u'Img3'
    IMG3_SIGNATURE_BYTES: List[int] = array('b', [51, 103, 109, 73])
    IMG3_SIGNATURE_LENGTH: int = 4
    IMG3_TAG_BDID_MAGIC: unicode = u'BDID'
    IMG3_TAG_BORD_MAGIC: unicode = u'BORD'
    IMG3_TAG_CERT_MAGIC: unicode = u'CERT'
    IMG3_TAG_CHIP_PROD: unicode = u'CHIP'
    IMG3_TAG_DATA_MAGIC: unicode = u'DATA'
    IMG3_TAG_ECID_MAGIC: unicode = u'ECID'
    IMG3_TAG_KBAG_MAGIC: unicode = u'KBAG'
    IMG3_TAG_PROD_MAGIC: unicode = u'PROD'
    IMG3_TAG_SCEP_MAGIC: unicode = u'SCEP'
    IMG3_TAG_SDOM_MAGIC: unicode = u'SDOM'
    IMG3_TAG_SEPO_MAGIC: unicode = u'SEPO'
    IMG3_TAG_SHSH_MAGIC: unicode = u'SHSH'
    IMG3_TAG_TYPE_MAGIC: unicode = u'TYPE'
    IMG3_TAG_VERS_MAGIC: unicode = u'VERS'
    IMG3_TYPE_APPLE_LOGO: unicode = u'logo'
    IMG3_TYPE_IBEC: unicode = u'ibec'
    IMG3_TYPE_IBOOT: unicode = u'ibot'
    IMG3_TYPE_IBSS: unicode = u'ibss'
    IMG3_TYPE_KERNEL: unicode = u'krnl'
    IMG3_TYPE_LLB: unicode = u'illb'
    IMG3_TYPE_RAMDISK: unicode = u'rdsk'
    IMG3_TYPE_RECOVERY_MODE: unicode = u'recm'



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
