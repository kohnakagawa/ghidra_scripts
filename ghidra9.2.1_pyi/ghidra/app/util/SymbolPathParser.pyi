from typing import List
import java.lang


class SymbolPathParser(object):
    """
    A parser for breaking down namespaces in the presence of complicating factors such
      as templates.

     For example, if a SymbolPath is constructed with "fooint, blah::hah::bar::baz",
     then "baz" is the name of a symbol in the "bar" namespace, which is in the
     "fooint, blah::hah" namespace.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    @staticmethod
    def parse(name: unicode) -> List[unicode]:
        """
        Parses a String pathname into its constituent namespace and name components.
         The list does not contain the global namespace, which is implied, but then
         has each more deeply nested namespace contained in order in the list, followed
         by the trailing name.
        @param name The input String to be parsed.
        @return {@literal List<String>} containing the sequence of namespaces and trailing name.
        """
        ...

    @overload
    @staticmethod
    def parse(name: unicode, ignoreLeaderParens: bool) -> List[unicode]:
        """
        Parses a String pathname into its constituent namespace and name components.
         The list does not contain the global namespace, which is implied, but then
         has each more deeply nested namespace contained in order in the list, followed
         by the trailing name.
        @param name The input String to be parsed.
        @param ignoreLeaderParens true signals to ignore any string that starts with a '(' char.
                This is useful to work around some problem characters.
        @return {@literal List<String>} containing the sequence of namespaces and trailing name.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
