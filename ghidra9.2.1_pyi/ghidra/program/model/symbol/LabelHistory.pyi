import ghidra.program.model.address
import java.lang
import java.util


class LabelHistory(object):
    """
    Container for history information about what happened to a label.
    """

    ADD: int = 0
    REMOVE: int = 1
    RENAME: int = 2



    def __init__(self, addr: ghidra.program.model.address.Address, userName: unicode, actionID: int, labelStr: unicode, modificationDate: java.util.Date):
        """
        Construct a new LabelHistory object.
        @param addr address of the label change
        @param userName name of user who made the change
        @param actionID either ADD, REMOVE, or RENAME
        @param labelStr label string
        @param modificationDate date of the change
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getActionID(self) -> int:
        """
        Get the action ID for this label history object.
        @return ADD, REMOVE, or RENAME
        """
        ...

    def getAddress(self) -> ghidra.program.model.address.Address:
        """
        Get address for this label history object.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getLabelString(self) -> unicode:
        """
        Get the label string for this label history object.
        """
        ...

    def getModificationDate(self) -> java.util.Date:
        """
        Get the modification date
        """
        ...

    def getUserName(self) -> unicode:
        """
        Get the user that made the change.
        """
        ...

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
    def actionID(self) -> int: ...

    @property
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def labelString(self) -> unicode: ...

    @property
    def modificationDate(self) -> java.util.Date: ...

    @property
    def userName(self) -> unicode: ...
