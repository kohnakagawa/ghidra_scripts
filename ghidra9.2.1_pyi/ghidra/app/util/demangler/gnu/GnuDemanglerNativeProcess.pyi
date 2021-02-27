import ghidra.app.util.demangler.gnu
import java.lang


class GnuDemanglerNativeProcess(object):
    DEMANGLER_GNU: unicode = u'demangler_gnu_v2_33_1'







    def demangle(self, __a0: unicode) -> unicode: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    @staticmethod
    def getDemanglerNativeProcess() -> ghidra.app.util.demangler.gnu.GnuDemanglerNativeProcess: ...

    @overload
    @staticmethod
    def getDemanglerNativeProcess(__a0: unicode) -> ghidra.app.util.demangler.gnu.GnuDemanglerNativeProcess: ...

    @overload
    @staticmethod
    def getDemanglerNativeProcess(__a0: unicode, __a1: unicode) -> ghidra.app.util.demangler.gnu.GnuDemanglerNativeProcess: ...

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
