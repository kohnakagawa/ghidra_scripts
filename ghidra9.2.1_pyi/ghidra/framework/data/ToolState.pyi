import ghidra.framework.model
import java.lang


class ToolState(object):
    """
    Container object for the state of the tool to hold an XML element.
    """





    def __init__(self, tool: ghidra.framework.plugintool.PluginTool, domainObject: ghidra.framework.model.DomainObject):
        """
        Construct a new tool state.
        @param tool tool's state to save
        @param domainObject the object containing the tool state
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getAfterState(self, domainObject: ghidra.framework.model.DomainObject) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreAfterRedo(self, domainObject: ghidra.framework.model.DomainObject) -> None:
        """
        Restore the tool's state after an undo
        """
        ...

    def restoreAfterUndo(self, domainObject: ghidra.framework.model.DomainObject) -> None:
        """
        Restore the tool's state after an undo
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
