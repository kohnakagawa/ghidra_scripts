import java.lang


class DemanglerOptions(object):
    """
    A simple class to contain the various settings for demangling.
    """





    @overload
    def __init__(self): ...

    @overload
    def __init__(self, copy: ghidra.app.util.demangler.DemanglerOptions): ...



    def applySignature(self) -> bool:
        """
        Checks if the apply signature option is currently set.
        @return true if set to apply function signatures that are demangled.
        """
        ...

    def demangleOnlyKnownPatterns(self) -> bool:
        """
        Checks if the option to only demangle known mangled patterns is set.
        @return true if only known mangled patterns will be demangled.
        """
        ...

    def doDisassembly(self) -> bool:
        """
        Checks if the option to perform disassembly for known data structures (like functions) when
         demangling is set.
        @return true if the option is set.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setApplySignature(self, applySignature: bool) -> None:
        """
        Set the option to apply function signatures that are demangled.
        @param applySignature true to apply function signatures that are demangled.
        """
        ...

    def setDemangleOnlyKnownPatterns(self, demangleOnlyKnownPatterns: bool) -> None:
        """
        Sets the option to only demangle known mangled patterns. Setting this to false causes
         all symbols to be demangled, which may result in some symbols getting demangled that were not
         actually mangled symbols.
        @param demangleOnlyKnownPatterns true to only demangle known mangled patterns.
        """
        ...

    def setDoDisassembly(self, doDisassembly: bool) -> None:
        """
        Sets the option to perform disassembly for known data structures (like functions) when
         demangling.
        @param doDisassembly true to perform disassembly when demangling.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
