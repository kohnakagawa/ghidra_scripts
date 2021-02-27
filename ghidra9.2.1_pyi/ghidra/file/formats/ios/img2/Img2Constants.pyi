import java.lang


class Img2Constants(object):
    IMAGE_TYPE_batC: unicode = u'batC'
    IMAGE_TYPE_batL: unicode = u'batL'
    IMAGE_TYPE_batl: unicode = u'batl'
    IMAGE_TYPE_dtre: unicode = u'dtre'
    IMAGE_TYPE_ibot: unicode = u'ibot'
    IMAGE_TYPE_llbz: unicode = u'llbz'
    IMAGE_TYPE_logo: unicode = u'logo'
    IMAGE_TYPE_nsvr: unicode = u'nsrv'
    IMAGE_TYPE_recm: unicode = u'recm'
    IMG2_LENGTH: int = 1024
    IMG2_SIGNATURE: unicode = u'Img2'
    IMG2_SIGNATURE_BYTES: List[int] = array('b', [50, 103, 109, 73])



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
