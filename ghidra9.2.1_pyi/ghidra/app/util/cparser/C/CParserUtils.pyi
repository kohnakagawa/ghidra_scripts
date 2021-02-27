import ghidra.app.services
import ghidra.framework.plugintool
import ghidra.program.model.data
import ghidra.program.model.listing
import java.lang


class CParserUtils(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def handleParseProblem(t: java.lang.Throwable, functionString: unicode) -> unicode:
        """
        Given a throwable, attempt pull out the significant error parts to generate a
         user-friendly error message.
        @param t the throwable to examine, originating from the {@link CParser}.
        @param functionString the full function signature text that was parsed by the parser.
        @return a user-friendly error message, or null if this class did not know how to
                 handle the given exception.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    @staticmethod
    def parseSignature(service: ghidra.app.services.DataTypeManagerService, program: ghidra.program.model.listing.Program, signatureText: unicode) -> ghidra.program.model.data.FunctionDefinitionDataType:
        """
        Parse the given function signature text.  Any exceptions will be handled herein
         by showing an error dialog (null is returned in that case).
        @param service the service used to access DataTypeManagers or null to use only the program's
         data type manager.
        @param program the program against which data types will be resolved
        @param signatureText the signature to parse
        @return the data type that is created as a result of parsing; null if there was a problem
        @see #parseSignature(DataTypeManagerService, Program, String, boolean)
        """
        ...

    @overload
    @staticmethod
    def parseSignature(serviceProvider: ghidra.framework.plugintool.ServiceProvider, program: ghidra.program.model.listing.Program, signatureText: unicode) -> ghidra.program.model.data.FunctionDefinitionDataType:
        """
        Parse the given function signature text.  Any exceptions will be handled herein
         by showing an error dialog (null is returned in that case).
        @param serviceProvider the service provider used to access DataTypeManagers
        @param program the program against which data types will be resolved
        @param signatureText the signature to parse
        @return the data type that is created as a result of parsing; null if there was a problem
        @see #parseSignature(DataTypeManagerService, Program, String)
        @see #parseSignature(DataTypeManagerService, Program, String, boolean)
        """
        ...

    @overload
    @staticmethod
    def parseSignature(service: ghidra.app.services.DataTypeManagerService, program: ghidra.program.model.listing.Program, signatureText: unicode, handleExceptions: bool) -> ghidra.program.model.data.FunctionDefinitionDataType:
        """
        Parse the given function signature text.  Any exceptions will be handled herein
         by showing an error dialog (null is returned in that case).
        @param service the service used to access DataTypeManagers or null to use only the program's
         data type manager.
        @param program the program against which data types will be resolved
        @param signatureText the signature to parse
        @param handleExceptions true signals that this method should deal with exceptions,
                showing error messages as necessary; false signals to throw any encountered
                parsing exceptions.  This allows clients to perform exception handling that
                better matches their workflow.
        @return the data type that is created as a result of parsing; null if there was a problem
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
