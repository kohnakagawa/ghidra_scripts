import ghidra.program.model.data
import java.lang


class DataTypeNamingUtil(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def setMangledAnonymousFunctionName(functionDefinition: ghidra.program.model.data.FunctionDefinitionDataType, namePrefix: unicode) -> unicode:
        """
        Generate a simple mangled function definition name and apply it to the specified functionDefinition.
        @param functionDefinition function definition whose name should be set
        @param namePrefix prefix to be applied to generated name.  An underscore will separate this prefix from the
         remainder of the mangled name.  If null specified a prefix of "_function" will be used.
        @return name applied to functionDefinition
        @throws IllegalArgumentException if generated name contains unsupported characters
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
