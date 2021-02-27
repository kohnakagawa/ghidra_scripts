import java.lang
import javax.swing


class ReservedKeyBindings(object):
    FOCUS_CYCLE_INFO_KEY: javax.swing.KeyStroke = shift meta alt pressed F3
    FOCUS_INFO_KEY: javax.swing.KeyStroke = shift meta alt pressed F2
    HELP_INFO_KEY: javax.swing.KeyStroke = meta pressed F1
    HELP_KEY1: javax.swing.KeyStroke = pressed HELP
    HELP_KEY2: javax.swing.KeyStroke = pressed F1
    UPDATE_KEY_BINDINGS_KEY: javax.swing.KeyStroke = pressed F4







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isReservedKeystroke(keyStroke: javax.swing.KeyStroke) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
