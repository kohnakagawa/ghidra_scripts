import ghidra.program.model.lang
import java.lang


class Processor(object, java.lang.Comparable):








    @overload
    def compareTo(self, p: ghidra.program.model.lang.Processor) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool: ...

    @staticmethod
    def findOrPossiblyCreateProcessor(name: unicode) -> ghidra.program.model.lang.Processor:
        """
        Use this method if you want to grab a reference to a Processor given its
         name, but if it doesn't exist go ahead and create it anyway and return
         the new instance.
        @param name the name of the Processor you're looking for/going to create
        @return the Processor
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def toProcessor(name: unicode) -> ghidra.program.model.lang.Processor:
        """
        Use this method to look up a Processor from a String when you want a ProcessorNotFoundException
         thrown if the Processor isn't found.
         <p>
         <b><u>Warning:</u></b> Use of this method depends upon languages being loaded.  See
         {@link DefaultLanguageService}.
        @param name the name of the Processor you're looking for
        @return the Processor
        @throws ProcessorNotFoundException if the processor doesn't exist yet
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
