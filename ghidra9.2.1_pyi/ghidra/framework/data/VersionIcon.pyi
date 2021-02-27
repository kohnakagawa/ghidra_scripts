import java.awt
import java.lang
import javax.swing


class VersionIcon(object, javax.swing.Icon):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getIconHeight(self) -> int: ...

    def getIconWidth(self) -> int: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def paintIcon(self, c: java.awt.Component, g: java.awt.Graphics, x: int, y: int) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
