import ghidra.app.util.opinion
import ghidra.program.model.lang
import java.lang


class LoadSpec(object):
    """
    Represents a possible way for a Loader to load something.
    """





    @overload
    def __init__(self, loader: ghidra.app.util.opinion.Loader, imageBase: long, requiresLanguageCompilerSpec: bool):
        """
        Constructs a {@link LoadSpec} with an unknown language/compiler.  Some {@link Loader}'s do
         not require a language/compiler.
        @param loader This {@link LoadSpec}'s {@link Loader}.
        @param imageBase The desired image base address for the load.
        @param requiresLanguageCompilerSpec True if this {@link LoadSpec} requires a
           language/compiler; otherwise, false.  If a language/compiler is required, it will have
           to be supplied to the {@link Loader} by some other means, and this {@link LoadSpec} will
           be considered incomplete.
        @see #isComplete()
        """
        ...

    @overload
    def __init__(self, loader: ghidra.app.util.opinion.Loader, imageBase: long, languageCompilerSpecQueryResult: ghidra.app.util.opinion.QueryResult):
        """
        Constructs a {@link LoadSpec} from a {@link QueryResult}.
        @param loader This {@link LoadSpec}'s {@link Loader}.
        @param imageBase The desired image base address for the load.
        @param languageCompilerSpecQueryResult The language/compiler spec ID.
        """
        ...

    @overload
    def __init__(self, loader: ghidra.app.util.opinion.Loader, imageBase: long, languageCompilerSpec: ghidra.program.model.lang.LanguageCompilerSpecPair, isPreferred: bool):
        """
        Constructs a {@link LoadSpec} from a manually supplied {@link LanguageCompilerSpecPair}.
        @param loader This {@link LoadSpec}'s {@link Loader}.
        @param imageBase The desired image base address for the load.
        @param languageCompilerSpec The language/compiler spec ID.  If this is not needed or not
           known, use {@link #LoadSpec(Loader, long, boolean)}.
        @param isPreferred true if this {@link LoadSpec} is preferred; otherwise, false.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDesiredImageBase(self) -> long:
        """
        Gets the desired image base to use during the load.
        @return The desired image base to use during the load.
        """
        ...

    def getLanguageCompilerSpec(self) -> ghidra.program.model.lang.LanguageCompilerSpecPair:
        """
        Gets this {@link LoadSpec}'s {@link LanguageCompilerSpecPair}.
        @return This {@link LoadSpec}'s {@link LanguageCompilerSpecPair}.  Could be null if this
           {@link LoadSpec} doesn't need or know the language/compiler.
        """
        ...

    def getLoader(self) -> ghidra.app.util.opinion.Loader:
        """
        Gets this {@link LoadSpec}'s {@link Loader}.
        @return This {@link LoadSpec}'s {@link Loader}.
        """
        ...

    def hashCode(self) -> int: ...

    def isComplete(self) -> bool:
        """
        Gets whether or not this {@link LoadSpec} is complete.  A {@link LoadSpec} is not considered
         complete if it requires a language/compiler to load something, but the language/compiler
         is currently unknown.
        @return True if this {@link LoadSpec} is complete; otherwise, false.
        """
        ...

    def isPreferred(self) -> bool:
        """
        Gets whether or not this {@link LoadSpec} is a preferred {@link LoadSpec}.
        @return True if this {@link LoadSpec} is a preferred {@link LoadSpec}; otherwise, false.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def requiresLanguageCompilerSpec(self) -> bool:
        """
        Gets whether or not this {@link LoadSpec} requires a language/compiler to load something.
        @return True if this {@link LoadSpec} requires a language/compiler to load something;
           otherwise, false.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def complete(self) -> bool: ...

    @property
    def desiredImageBase(self) -> long: ...

    @property
    def languageCompilerSpec(self) -> ghidra.program.model.lang.LanguageCompilerSpecPair: ...

    @property
    def loader(self) -> ghidra.app.util.opinion.Loader: ...

    @property
    def preferred(self) -> bool: ...
