import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class ChangeFunctionTagCmd(object, ghidra.framework.cmd.Command):
    """
    Updates the name or comment field for a given function tag.
    """

    TAG_COMMENT_CHANGED: int = 1
    TAG_NAME_CHANGED: int = 0



    def __init__(self, tagName: unicode, newVal: unicode, field: int):
        """
        Constructor.
        @param tagName the name of the tag to change
        @param newVal the new value to set
        @param field the field to set
        """
        ...



    def applyTo(self, obj: ghidra.framework.model.DomainObject) -> bool:
        """
        PUBLIC METHODS
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode: ...

    def getStatusMsg(self) -> unicode: ...

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

    @property
    def name(self) -> unicode: ...

    @property
    def statusMsg(self) -> unicode: ...
