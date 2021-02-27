from typing import Iterator
import ghidra.app.util.cparser.CPP.PreProcessor
import ghidra.program.model.data
import java.lang
import java.util


class DefineTable(object):




    def __init__(self): ...



    def containsKey(self, def_: unicode) -> bool:
        """
        See if the define table contains a definition
        @param def
        @return
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def expand(self, image: unicode, join: bool) -> unicode:
        """
        do the final expansion of "##" concats in the define strings that protect normal macro substitution.
        @param image
        @param join
        @return
        """
        ...

    def get(self, string: unicode) -> ghidra.app.util.cparser.CPP.PreProcessor.PPToken:
        """
        @param string
        @return
        """
        ...

    def getArgs(self, currKey: unicode) -> java.util.Vector:
        """
        @param currKey
        @return
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDefineAt(self, buf: java.lang.StringBuffer, pos: int) -> unicode:
        """
        @param buf the buffer containing the define
        @param pos the position of the define
        @return the define
        """
        ...

    def getDefineNames(self) -> Iterator[unicode]:
        """
        @return an iterator over the defined string names
        """
        ...

    def getDefinitionPath(self, defName: unicode) -> unicode: ...

    def getParams(self, buf: java.lang.StringBuffer, start: int, endChar: int) -> unicode:
        """
        @param buf the buffer containing the parameters
        @param start the starting index of the parameters in the buffer
        @param endChar the delimiter for the parameters
        @return the parameters
        """
        ...

    def getValue(self, defName: unicode) -> unicode: ...

    def hashCode(self) -> int: ...

    def isArg(self, string: unicode) -> bool:
        """
        Check if a define has args.
        @param string name of define
        @return
        """
        ...

    def isNumeric(self, defName: unicode) -> bool:
        """
        Check if the token that defined this define was numeric
        @param defName
        @return
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def populateDefineEquates(self, dtMgr: ghidra.program.model.data.DataTypeManager) -> None:
        """
        Given a data type manager, populate defines with constant values as Enums
        """
        ...

    def put(self, string: unicode, val: ghidra.app.util.cparser.CPP.PreProcessor.PPToken) -> None:
        """
        Associate a define "name" with a Preprocessor parser token match.
        @param string - name of define
        @param val - token value from parsing
        """
        ...

    def putArg(self, string: unicode, val: java.util.Vector) -> None:
        """
        Add an args definition for a define with arguments
             #define bubba(a,b)   (a or b)
        @param string name of define
        @param val set of arg token names
        """
        ...

    def remove(self, string: unicode) -> ghidra.app.util.cparser.CPP.PreProcessor.PPToken:
        """
        Remove a definition from the known defines.
        @param string name of define
        @return return the defined token for the named define.
        """
        ...

    def removeArg(self, string: unicode) -> java.util.Vector:
        """
        Get rid of args for a define
        @param string name of define
        @return
        """
        ...

    def size(self) -> int:
        """
        Size of the define table.
        @return
        """
        ...

    @overload
    def toString(self) -> unicode: ...

    @overload
    def toString(self, string: unicode) -> unicode:
        """
        display a string for the named define.
        @param string named define
        @return
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def defineNames(self) -> java.util.Iterator: ...
