import java.lang


class OperandType(object):
    """
    Helper class for testing operand related flags in an integer.
    """

    ADDRESS: int = 8192
    BIT: int = 32768
    BYTE: int = 65536
    CODE: int = 64
    COP: int = 2097152
    DATA: int = 128
    DYNAMIC: int = 4194304
    FLAG: int = 2048
    FLOAT: int = 1048576
    IMMEDIATE: int = 8
    IMPLICIT: int = 32
    INDIRECT: int = 4
    LIST: int = 1024
    PORT: int = 256
    QUADWORD: int = 262144
    READ: int = 1
    REGISTER: int = 512
    RELATIVE: int = 16
    SCALAR: int = 16384
    SIGNED: int = 524288
    TEXT: int = 4096
    WORD: int = 131072
    WRITE: int = 2



    def __init__(self): ...



    @staticmethod
    def doesRead(operandType: int) -> bool:
        """
        check the READ flag.
        @param operandType the bit field to examine.
        @return true if the READ flag is set.
        """
        ...

    @staticmethod
    def doesWrite(operandType: int) -> bool:
        """
        check the WRITE flag.
        @param operandType the bit field to examine.
        @return true if the WRITE flag is set.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isAddress(operandType: int) -> bool:
        """
        check ADDRESS flag.
        @param operandType the bit field to examine.
        @return true if the ADDRESS flag is set
        """
        ...

    @staticmethod
    def isBit(operandType: int) -> bool:
        """
        check the BIT flag.
        @param operandType the bit field to examine.
        @return true if the BIT flag is set.
        """
        ...

    @staticmethod
    def isByte(operandType: int) -> bool:
        """
        check the BYTE flag.
        @param operandType the bit field to examine.
        @return true if the BYTE flag is set.
        """
        ...

    @staticmethod
    def isCoProcessor(operandType: int) -> bool:
        """
        check the COPROCESSOR flag.
        @param operandType the bit field to examine.
        @return true if the COPROCESSOR flag is set.
        """
        ...

    @staticmethod
    def isCodeReference(operandType: int) -> bool:
        """
        check the CODE flag.
        @param operandType the bit field to examine.
        @return true if the CODE flag is set.
        """
        ...

    @staticmethod
    def isDataReference(operandType: int) -> bool:
        """
        check the DATA flag.
        @param operandType the bit field to examine.
        @return true if the DATA flag is set.
        """
        ...

    @staticmethod
    def isFlag(operandType: int) -> bool:
        """
        check the CONDITION FLAG flag.
        @param operandType the bit field to examine.
        @return true if the CONDITION flag is set.
        """
        ...

    @staticmethod
    def isFloat(operandType: int) -> bool:
        """
        check the FLOAT flag.
        @param operandType the bit field to examine.
        @return true if the FLOAT flag is set.
        """
        ...

    @staticmethod
    def isImmediate(operandType: int) -> bool:
        """
        check the IMMEDIATE flag.
        @param operandType the bit field to examine.
        @return true if the IMMEDIATE flag is set.
        """
        ...

    @staticmethod
    def isImplicit(operandType: int) -> bool:
        """
        check the IMPLICIT flag.
        @param operandType the bit field to examine.
        @return true if the IMPLICIT flag is set.
        """
        ...

    @staticmethod
    def isIndirect(operandType: int) -> bool:
        """
        check the INDIRECT flag.
        @param operandType the bit field to examine.
        @return true if the INDIRECT flag is set.
        """
        ...

    @staticmethod
    def isList(operandType: int) -> bool:
        """
        check the LIST flag.
        @param operandType the bit field to examine.
        @return true if the LIST flag is set.
        """
        ...

    @staticmethod
    def isPort(operandType: int) -> bool:
        """
        check the PORT flag.
        @param operandType the bit field to examine.
        @return true if the PORT flag is set.
        """
        ...

    @staticmethod
    def isQuadWord(operandType: int) -> bool:
        """
        check the QUADWORD flag.
        @param operandType the bit field to examine.
        @return true if the QUADWORD flag is set.
        """
        ...

    @staticmethod
    def isRegister(operandType: int) -> bool:
        """
        check the REGISTER flag.
        @param operandType the bit field to examine.
        @return true if the REGISTER flag is set.
        """
        ...

    @staticmethod
    def isRelative(operandType: int) -> bool:
        """
        check the RELATIVE flag.
        @param operandType the bit field to examine.
        @return true if the RELATIVE flag is set.
        """
        ...

    @staticmethod
    def isScalar(operandType: int) -> bool:
        """
        check SCALAR flag.
        @param operandType the bit field to examine.
        @return true if the SCALAR flag is set
        """
        ...

    @staticmethod
    def isScalarAsAddress(operandType: int) -> bool:
        """
        check if both a scalar and an address
        @param operandType the bit field to examine.
        @return true if it is both a scalar and an address
        """
        ...

    @staticmethod
    def isSigned(operandType: int) -> bool:
        """
        check the SIGNED flag.
        @param operandType the bit field to examine.
        @return true if the SIGNED flag is set.
        """
        ...

    @staticmethod
    def isText(operandType: int) -> bool:
        """
        check the TEXT flag.
        @param operandType the bit field to examine.
        @return true if the TEXT flag is set.
        """
        ...

    @staticmethod
    def isWord(operandType: int) -> bool:
        """
        check the WORD flag.
        @param operandType the bit field to examine.
        @return true if the WORD flag is set.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def toString(operandType: int) -> unicode:
        """
        returns a string representation of the given operandType
        @param operandType the operandType bits
        @return the string rep
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
