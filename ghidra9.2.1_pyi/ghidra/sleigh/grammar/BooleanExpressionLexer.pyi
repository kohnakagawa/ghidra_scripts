from typing import List
import java.lang
import org.antlr.runtime


class BooleanExpressionLexer(org.antlr.runtime.Lexer):
    ALPHA: int = 4
    DIGIT: int = 5
    EOF: int = -1
    ESCAPE: int = 6
    HEXDIGIT: int = 7
    IDENTIFIER: int = 8
    KEY_DEFINED: int = 9
    OCTAL_ESCAPE: int = 10
    OP_AND: int = 11
    OP_EQ: int = 12
    OP_NEQ: int = 13
    OP_NOT: int = 14
    OP_OR: int = 15
    OP_XOR: int = 16
    QSTRING: int = 17
    T__20: int = 20
    T__21: int = 21
    UNICODE_ESCAPE: int = 18
    WS: int = 19



    @overload
    def __init__(self): ...

    @overload
    def __init__(self, input: org.antlr.runtime.CharStream): ...

    @overload
    def __init__(self, input: org.antlr.runtime.CharStream, state: org.antlr.runtime.RecognizerSharedState): ...



    def alreadyParsedRule(self, __a0: org.antlr.runtime.IntStream, __a1: int) -> bool: ...

    def beginResync(self) -> None: ...

    @overload
    def consumeUntil(self, __a0: org.antlr.runtime.IntStream, __a1: int) -> None: ...

    @overload
    def consumeUntil(self, __a0: org.antlr.runtime.IntStream, __a1: org.antlr.runtime.BitSet) -> None: ...

    def displayRecognitionError(self, __a0: List[unicode], __a1: org.antlr.runtime.RecognitionException) -> None: ...

    @overload
    def emit(self) -> org.antlr.runtime.Token: ...

    @overload
    def emit(self, __a0: org.antlr.runtime.Token) -> None: ...

    def emitErrorMessage(self, __a0: unicode) -> None: ...

    def endResync(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def failed(self) -> bool: ...

    def getBacktrackingLevel(self) -> int: ...

    def getCharErrorDisplay(self, __a0: int) -> unicode: ...

    def getCharIndex(self) -> int: ...

    def getCharPositionInLine(self) -> int: ...

    def getCharStream(self) -> org.antlr.runtime.CharStream: ...

    def getClass(self) -> java.lang.Class: ...

    def getDelegates(self) -> List[org.antlr.runtime.Lexer]: ...

    def getEOFToken(self) -> org.antlr.runtime.Token: ...

    def getErrorHeader(self, __a0: org.antlr.runtime.RecognitionException) -> unicode: ...

    def getErrorMessage(self, __a0: org.antlr.runtime.RecognitionException, __a1: List[unicode]) -> unicode: ...

    def getGrammarFileName(self) -> unicode: ...

    def getLine(self) -> int: ...

    def getNumberOfSyntaxErrors(self) -> int: ...

    @overload
    def getRuleInvocationStack(self) -> List[object]: ...

    @overload
    @staticmethod
    def getRuleInvocationStack(__a0: java.lang.Throwable, __a1: unicode) -> List[object]: ...

    def getRuleMemoization(self, __a0: int, __a1: int) -> int: ...

    def getRuleMemoizationCacheSize(self) -> int: ...

    def getSourceName(self) -> unicode: ...

    def getText(self) -> unicode: ...

    def getTokenErrorDisplay(self, __a0: org.antlr.runtime.Token) -> unicode: ...

    def getTokenNames(self) -> List[unicode]: ...

    def hashCode(self) -> int: ...

    def mALPHA(self) -> None: ...

    def mDIGIT(self) -> None: ...

    def mESCAPE(self) -> None: ...

    def mHEXDIGIT(self) -> None: ...

    def mIDENTIFIER(self) -> None: ...

    def mKEY_DEFINED(self) -> None: ...

    def mOCTAL_ESCAPE(self) -> None: ...

    def mOP_AND(self) -> None: ...

    def mOP_EQ(self) -> None: ...

    def mOP_NEQ(self) -> None: ...

    def mOP_NOT(self) -> None: ...

    def mOP_OR(self) -> None: ...

    def mOP_XOR(self) -> None: ...

    def mQSTRING(self) -> None: ...

    def mT__20(self) -> None: ...

    def mT__21(self) -> None: ...

    def mTokens(self) -> None: ...

    def mUNICODE_ESCAPE(self) -> None: ...

    def mWS(self) -> None: ...

    @overload
    def match(self, __a0: int) -> None: ...

    @overload
    def match(self, __a0: unicode) -> None: ...

    @overload
    def match(self, __a0: org.antlr.runtime.IntStream, __a1: int, __a2: org.antlr.runtime.BitSet) -> object: ...

    @overload
    def matchAny(self) -> None: ...

    @overload
    def matchAny(self, __a0: org.antlr.runtime.IntStream) -> None: ...

    def matchRange(self, __a0: int, __a1: int) -> None: ...

    def memoize(self, __a0: org.antlr.runtime.IntStream, __a1: int, __a2: int) -> None: ...

    def mismatchIsMissingToken(self, __a0: org.antlr.runtime.IntStream, __a1: org.antlr.runtime.BitSet) -> bool: ...

    def mismatchIsUnwantedToken(self, __a0: org.antlr.runtime.IntStream, __a1: int) -> bool: ...

    def nextToken(self) -> org.antlr.runtime.Token: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def recover(self, __a0: org.antlr.runtime.RecognitionException) -> None: ...

    @overload
    def recover(self, __a0: org.antlr.runtime.IntStream, __a1: org.antlr.runtime.RecognitionException) -> None: ...

    def recoverFromMismatchedSet(self, __a0: org.antlr.runtime.IntStream, __a1: org.antlr.runtime.RecognitionException, __a2: org.antlr.runtime.BitSet) -> object: ...

    def reportError(self, __a0: org.antlr.runtime.RecognitionException) -> None: ...

    def reset(self) -> None: ...

    def setBacktrackingLevel(self, __a0: int) -> None: ...

    def setCharStream(self, __a0: org.antlr.runtime.CharStream) -> None: ...

    def setText(self, __a0: unicode) -> None: ...

    def skip(self) -> None: ...

    def toString(self) -> unicode: ...

    def toStrings(self, __a0: List[object]) -> List[object]: ...

    @overload
    def traceIn(self, __a0: unicode, __a1: int) -> None: ...

    @overload
    def traceIn(self, __a0: unicode, __a1: int, __a2: object) -> None: ...

    @overload
    def traceOut(self, __a0: unicode, __a1: int) -> None: ...

    @overload
    def traceOut(self, __a0: unicode, __a1: int, __a2: object) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def delegates(self) -> List[org.antlr.runtime.Lexer]: ...

    @property
    def grammarFileName(self) -> unicode: ...