import java.lang


class GenericPluginCategoryNames(object):
    COMMON: unicode = u'Common'
    EXAMPLES: unicode = u'Examples'
    MISC: unicode = u'Miscellaneous'
    SUPPORT: unicode = u'Support'
    TESTING: unicode = u'Testing'



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
