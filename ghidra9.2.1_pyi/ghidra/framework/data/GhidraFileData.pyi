import java.lang


class GhidraFileData(object):
    CHECKED_OUT_EXCLUSIVE_ICON: javax.swing.Icon = jar:file:/Applications/ghidra_9.2.1_PUBLIC/Ghidra/Framework/Project/lib/Project.jar!/images/checkex.png
    CHECKED_OUT_ICON: javax.swing.Icon = jar:file:/Applications/ghidra_9.2.1_PUBLIC/Ghidra/Framework/Project/lib/Project.jar!/images/check.png
    HIJACKED_ICON: javax.swing.Icon = jar:file:/Applications/ghidra_9.2.1_PUBLIC/Ghidra/Framework/Project/lib/Project.jar!/images/small_hijack.gif
    NOT_LATEST_CHECKED_OUT_ICON: javax.swing.Icon = jar:file:/Applications/ghidra_9.2.1_PUBLIC/Ghidra/Framework/Project/lib/Project.jar!/images/checkNotLatest.gif
    READ_ONLY_ICON: javax.swing.Icon = jar:file:/Applications/ghidra_9.2.1_PUBLIC/Ghidra/Framework/Project/lib/Project.jar!/images/user-busy.png
    UNSUPPORTED_FILE_ICON: javax.swing.Icon = jar:file:/Applications/ghidra_9.2.1_PUBLIC/Ghidra/Framework/Project/lib/Project.jar!/images/unknownFile.gif
    VERSION_ICON: javax.swing.Icon = ghidra.framework.data.VersionIcon@7d37ef03







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
