import ghidra.app.util.bin
import ghidra.file.crypto
import ghidra.util.classfinder
import ghidra.util.task
import java.lang


class Decryptor(ghidra.util.classfinder.ExtensionPoint, object):








    def decrypt(self, __a0: unicode, __a1: unicode, __a2: ghidra.app.util.bin.ByteProvider, __a3: ghidra.util.task.TaskMonitor) -> ghidra.file.crypto.DecryptedPacket: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isValid(self, __a0: ghidra.app.util.bin.ByteProvider) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
