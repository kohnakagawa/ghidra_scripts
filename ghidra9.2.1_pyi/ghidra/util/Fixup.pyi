import ghidra.framework.plugintool
import java.lang


class Fixup(object):








    def canFixup(self) -> bool:
        """
        Return true if this Fixup object can automatically perform some action to address the issue. false
         if the fixup() method does nothing.
        @return
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def fixup(self, provider: ghidra.framework.plugintool.ServiceProvider) -> bool:
        """
        Attempts to perform some action or task to "fix" the related issue.
        @param provider a service provider that can provide various services.
        @return true if the fixup performed its intended action.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode:
        """
        Returns a description of what this Fixup.  Typically, it will either be a simple suggestion
         for something the user could do, or it might be a description of whate the fixup() method will
         attempt to do to address some issue.
        @return a description for this Fixup
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
    def description(self) -> unicode: ...
