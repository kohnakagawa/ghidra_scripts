import ghidra.framework.model
import java.lang


class DomainFileFilter(object):
    """
    Interface  to indicate whether a domain file should be included in a list or
     set of domain files.
    """









    def accept(self, df: ghidra.framework.model.DomainFile) -> bool:
        """
        Tests whether or not the specified domain file should be
         included in a domain file list.
        @param df The domain file to be tested
        @return <code>true</code> if and only if <code>df</code>
        """
        ...

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
