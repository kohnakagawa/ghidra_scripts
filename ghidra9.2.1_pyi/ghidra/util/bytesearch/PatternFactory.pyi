import ghidra.util.bytesearch
import java.lang


class PatternFactory(object):
    """
    Interface for factories that create Match Pattern classes
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getMatchActionByName(self, nm: unicode) -> ghidra.util.bytesearch.MatchAction:
        """
        Get a named match action
        @param nm name of action to find
        @return match action with the given name, null otherwise
        """
        ...

    def getPostRuleByName(self, nm: unicode) -> ghidra.util.bytesearch.PostRule:
        """
        Get a named post match rule by name
        @param nm name of the post rule
        @return the post rule with the name, null otherwise
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
