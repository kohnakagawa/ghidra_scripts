import java.lang


class GhidraScriptConstants(object):
    """
    A class to hold constants to be shared for clients of this package.

     This class should not depend on any classes in this package in order to prevent static
     loading of data.
    """

    DEFAULT_SCRIPT_NAME: unicode = u'NewScript'
    USER_SCRIPTS_DIR_PROPERTY: unicode = u'ghidra.user.scripts.dir'







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
