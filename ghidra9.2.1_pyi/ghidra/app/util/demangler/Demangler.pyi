import ghidra.app.util.demangler
import ghidra.program.model.listing
import ghidra.util.classfinder
import java.lang


class Demangler(ghidra.util.classfinder.ExtensionPoint, object):
    """
    NOTE:  ALL DEMANGLER CLASSES MUST END IN "Demangler".  If not,
     the ClassSearcher will not find them.
    """









    def canDemangle(self, program: ghidra.program.model.listing.Program) -> bool: ...

    def createDefaultOptions(self) -> ghidra.app.util.demangler.DemanglerOptions:
        """
        Creates default options for this particular demangler
        @return the options
        """
        ...

    @overload
    def demangle(self, mangled: unicode) -> ghidra.app.util.demangler.DemangledObject:
        """
        Attempts to demangle the given string using the default options
         ({@link #createDefaultOptions()}
        @param mangled the mangled string
        @return the result
        @throws DemangledException if the string cannot be demangled
        """
        ...

    @overload
    def demangle(self, mangled: unicode, demangleOnlyKnownPatterns: bool) -> ghidra.app.util.demangler.DemangledObject:
        """
        Deprecated.  Use {@link #demangle(String)} or
          {@link #demangle(String, DemanglerOptions)}.
        @param mangled the mangled string
        @param demangleOnlyKnownPatterns true signals to avoid demangling strings that do
                not fit known demangled patterns for this demangler
        @return the result
        @throws DemangledException if the string cannot be demangled
        @deprecated see above
        """
        ...

    @overload
    def demangle(self, mangled: unicode, options: ghidra.app.util.demangler.DemanglerOptions) -> ghidra.app.util.demangler.DemangledObject:
        """
        Attempts to demangle the given string using the given options
        @param mangled the mangled string
        @param options the options
        @return the result
        @throws DemangledException if the string cannot be demangled
        """
        ...

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
