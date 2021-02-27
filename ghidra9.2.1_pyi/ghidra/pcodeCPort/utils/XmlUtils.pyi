import java.io
import java.lang


class XmlUtils(object):








    @staticmethod
    def a_v(__a0: java.io.PrintStream, __a1: unicode, __a2: unicode) -> None: ...

    @staticmethod
    def a_v_b(__a0: java.io.PrintStream, __a1: unicode, __a2: bool) -> None: ...

    @staticmethod
    def a_v_i(__a0: java.io.PrintStream, __a1: unicode, __a2: long) -> None: ...

    @staticmethod
    def a_v_u(__a0: java.io.PrintStream, __a1: unicode, __a2: long) -> None: ...

    @staticmethod
    def decodeBoolean(__a0: unicode) -> bool: ...

    @staticmethod
    def decodeUnknownInt(__a0: unicode) -> int: ...

    @staticmethod
    def decodeUnknownLong(__a0: unicode) -> long: ...

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

    @staticmethod
    def xml_escape(__a0: java.io.PrintStream, __a1: unicode) -> None: ...
