import ghidra.file.formats.ext4
import java.lang


class Ext4File(object):




    @overload
    def __init__(self): ...

    @overload
    def __init__(self, __a0: unicode): ...

    @overload
    def __init__(self, __a0: ghidra.file.formats.ext4.Ext4Inode): ...

    @overload
    def __init__(self, __a0: unicode, __a1: ghidra.file.formats.ext4.Ext4Inode): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getInode(self) -> ghidra.file.formats.ext4.Ext4Inode: ...

    def getName(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setInode(self, __a0: ghidra.file.formats.ext4.Ext4Inode) -> None: ...

    def setName(self, __a0: unicode) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def inode(self) -> ghidra.file.formats.ext4.Ext4Inode: ...

    @inode.setter
    def inode(self, value: ghidra.file.formats.ext4.Ext4Inode) -> None: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...
