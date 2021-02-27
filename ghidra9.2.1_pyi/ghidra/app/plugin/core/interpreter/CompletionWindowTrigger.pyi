from typing import List
import ghidra.app.plugin.core.interpreter
import java.awt.event
import java.lang
import javax.swing


class CompletionWindowTrigger(java.lang.Enum):
    CONTROL_SPACE: ghidra.app.plugin.core.interpreter.CompletionWindowTrigger = CONTROL_SPACE
    TAB: ghidra.app.plugin.core.interpreter.CompletionWindowTrigger = TAB







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def getKeyStroke(self) -> javax.swing.KeyStroke: ...

    def hashCode(self) -> int: ...

    def isTrigger(self, __a0: java.awt.event.KeyEvent) -> bool: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.app.plugin.core.interpreter.CompletionWindowTrigger: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.plugin.core.interpreter.CompletionWindowTrigger]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def keyStroke(self) -> javax.swing.KeyStroke: ...
