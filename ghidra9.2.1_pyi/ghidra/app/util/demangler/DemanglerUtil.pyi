import ghidra.app.util.demangler
import ghidra.program.model.listing
import java.lang


class DemanglerUtil(object):




    def __init__(self): ...



    @overload
    @staticmethod
    def demangle(mangled: unicode) -> ghidra.app.util.demangler.DemangledObject:
        """
        Locates all available demanglers, then it attempts to demangle.  This method will
         query all demanglers regardless of architecture.

         <p>This method will use only the default options for demangling.  If you need to
         specify options, then you will have to call each specific demangler directly, creating
         the options specifically needed for each demangler.   See
         {@link Demangler#createDefaultOptions()}.
        @param mangled the mangled name
        @return the demangled object or null
        """
        ...

    @overload
    @staticmethod
    def demangle(program: ghidra.program.model.listing.Program, mangled: unicode) -> ghidra.app.util.demangler.DemangledObject:
        """
        Locates all available demanglers and checks to see if the supplied program is
         supported, then it attempts to demangle.

         <p>This method will use only the default options for demangling.  If you need to
         specify options, then you will have to call each specific demangler directly, creating
         the options specifically needed for each demangler.   See
         {@link Demangler#createDefaultOptions()}.
        @param program the program containing the mangled name
        @param mangled the mangled name
        @return the demangled object or null
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def stripSuperfluousSignatureSpaces(str: unicode) -> unicode:
        """
        Remove superfluous function signature spaces from specified string
        @param str string
        @return string with unwanted spaces removed
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
