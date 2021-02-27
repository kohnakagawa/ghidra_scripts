import java.lang


class SegmentNames(object):
    SEG_DATA: unicode = u'__DATA'
    SEG_ICON: unicode = u'__ICON'
    SEG_IMPORT: unicode = u'__IMPORT'
    SEG_LINKEDIT: unicode = u'__LINKEDIT'
    SEG_OBJC: unicode = u'__OBJC'
    SEG_PAGEZERO: unicode = u'__PAGEZERO'
    SEG_PRELINK_TEXT: unicode = u'__PRELINK_TEXT'
    SEG_TEXT: unicode = u'__TEXT'
    SEG_TEXT_EXEC: unicode = u'__TEXT_EXEC'
    SEG_UNIXSTACK: unicode = u'__UNIXSTACK'



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
