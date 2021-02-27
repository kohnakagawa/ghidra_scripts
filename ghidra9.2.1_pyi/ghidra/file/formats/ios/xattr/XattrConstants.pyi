import java.lang


class XattrConstants(object):
    DECMPFS_XATTR_NAME: unicode = u'com.apple.decmpfs'
    KAUTH_FILESEC_XATTR_NAME: unicode = u'com.apple.system.Security'
    KAUTH_SCOPE_PROCESS: unicode = u'com.apple.kauth.process'
    RESOURCE_XATTR_NAME: unicode = u'com.apple.ResourceFork'



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
