import java.lang


class ExtensionPoint(object):
    """
    NOTE: ExtensionPoint logistics have changed! It is no longer sufficient to
     implement ExtensionPoint in order for the ClassSearcher to dynamically pick
     up your class. Your class also needs to conform to a class name suffix rule.
     The modules included in your application can have a file named
     "{ModuleRoot}/data/ExtensionPoint.manifest". This file contains (one per
     line) the suffixes that should be checked for inclusion into the class
     searching. IF YOUR EXTENSION POINT DOES NOT HAVE A SUFFIX INDICATED IN ONE OF
     THESE FILES, IT WILL NOT BE AUTOMATICALLY DISCOVERED.

     This is a marker interface used to mark classes and interfaces that Ghidra
     will automatically search for and load.
    """









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
