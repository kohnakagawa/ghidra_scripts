import ghidra.program.model.data
import ghidra.program.model.listing
import java.lang


class FunctionSignatureParser(object):
    """
    Class for parsing function signatures. This class attempts to be much more
     flexible than a full parser that requires correct C or C++ syntax. To achieve
     this, it scans the original function signature (if present) for names that
     would cause parse problems (parens, brackets, asterisk, commas, and spaces).
     If it finds any problem names, it looks for those strings in the text to be
     parsed and if it finds them, it replaces them with substitutes that parse
     easily. Then, after parsing, those replacement strings are then restored to
     their original values.

     Some examples of valid c++ that would fail due to the current limitations:


     int operator()(int x) - fails due to parens in function name unsigned int
     bar(float y) - fails due to space in return type name

     Note: you can edit signatures that already have these features as long as
     your modifications don't affect the pieces containing parens, commas or
     spaces in their name.
    """





    def __init__(self, destDataTypeManager: ghidra.program.model.data.DataTypeManager, service: ghidra.app.services.DataTypeQueryService):
        """
        Constructs a SignatureParser for a program.  The destDataTypeManager and/or
         service must be specified.
        @param destDataTypeManager the destination datatype maanger.
        @param service the DataTypeManagerService to use for resolving datatypes that
                        can't be found in the given program. Can be null to utilize
                        program based types only.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def parse(self, originalSignature: ghidra.program.model.listing.FunctionSignature, signatureText: unicode) -> ghidra.program.model.data.FunctionDefinitionDataType:
        """
        Parse the given function signature text into a FunctionDefinitionDataType.
        @param originalSignature the function signature before editing. This may be
                                  null if the user is entering a new signature instead
                                  of editing an existing one.
        @param signatureText the text to be parsed into a function signature.
        @return the FunctionDefinitionDataType resulting from parsing.
        @throws ParseException if the text could not be parsed.
        @throws CancelledException if parse cancelled by user
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
