import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class CompoundCmd(object, ghidra.framework.cmd.Command):
    """
    Implementation for multiple commands that are done as a unit.

     Multiple commands may be added to this one so that multiple changes can be
     applied to the domain object as unit.
    """





    def __init__(self, name: unicode):
        """
        Constructor for CompoundCmd.
        @param name the name of the command
        """
        ...



    def add(self, cmd: ghidra.framework.cmd.Command) -> None:
        """
        Add the given command to this command.
        @param cmd command to add to this command
        """
        ...

    def applyTo(self, obj: ghidra.framework.model.DomainObject) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode: ...

    def getStatusMsg(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def size(self) -> int:
        """
        Return the number of commands that are part of this compound command.
        @return the number of commands that have been added to this one.
        """
        ...

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
