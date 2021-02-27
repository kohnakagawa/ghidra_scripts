import ghidra.framework.model
import java.lang


class Command(object):
    """
    Interface to define a change made to a domain object.
    """









    def applyTo(self, obj: ghidra.framework.model.DomainObject) -> bool:
        """
        Applies the command to the given domain object.
        @param obj domain object that this command is to be applied.
        @return true if the command applied successfully
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode:
        """
        Returns the name of this command.
        @return the name of this command
        """
        ...

    def getStatusMsg(self) -> unicode:
        """
        Returns the status message indicating the status of the command.
        @return reason for failure, or null if the status of the command
                 was successful
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
    def name(self) -> unicode: ...

    @property
    def statusMsg(self) -> unicode: ...
