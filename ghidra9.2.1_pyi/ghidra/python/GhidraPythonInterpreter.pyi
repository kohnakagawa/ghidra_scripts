from typing import List
import <reflected field public org.python.core.PyObject org.python.core.PySystemState
import generic.jar
import ghidra.python
import java.io
import java.lang
import java.util
import org.python.core
import org.python.util


class GhidraPythonInterpreter(org.python.util.InteractiveInterpreter):
    """
    A python interpreter meant for Ghidra's use.  Each interpreter you get will have its own
     variable space so they should not interfere with each other.

     There is no longer a way to reset an interpreter...it was too complicated to get right.
     Instead, you should #cleanup() your old interpreter and make a new one.
    """

    buffer: java.lang.StringBuilder
    filename: unicode







    def cleanup(self) -> None: ...

    def close(self) -> None: ...

    @overload
    def compile(self, __a0: unicode) -> code: ...

    @overload
    def compile(self, __a0: java.io.Reader) -> code: ...

    @overload
    def compile(self, __a0: unicode, __a1: unicode) -> code: ...

    @overload
    def compile(self, __a0: java.io.Reader, __a1: unicode) -> code: ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    def eval(self, __a0: unicode) -> object: ...

    @overload
    def eval(self, __a0: object) -> object: ...

    @overload
    def exec(self, __a0: unicode) -> None: ...

    @overload
    def exec(self, __a0: object) -> None: ...

    def execFile(self, file: generic.jar.ResourceFile, script: ghidra.python.PythonScript) -> None:
        """
        Execute a python file using this interpreter.
        @param file The python file to execute.
        @param script A PythonScript from which we load state (or null).
        @throws IllegalStateException if this interpreter has been cleaned up.
        """
        ...

    @overload
    def execfile(self, __a0: unicode) -> None: ...

    @overload
    def execfile(self, __a0: java.io.InputStream) -> None: ...

    @overload
    def execfile(self, __a0: java.io.InputStream, __a1: unicode) -> None: ...

    @overload
    @staticmethod
    def get() -> ghidra.python.GhidraPythonInterpreter:
        """
        Gets a new GhidraPythonInterpreter instance.
        @return A new GhidraPythonInterpreter. Could be null if it failed to be created.
        """
        ...

    @overload
    def get(self, __a0: unicode) -> object: ...

    @overload
    def get(self, __a0: unicode, __a1: java.lang.Class) -> object: ...

    def getClass(self) -> java.lang.Class: ...

    def getLocals(self) -> object: ...

    def getSystemState(self) -> <reflected field public org.python.core.PyObject org.python.core.PySystemState.__name__ at 0x1>: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def initialize(__a0: java.util.Properties, __a1: java.util.Properties, __a2: List[unicode]) -> None: ...

    def interrupt(self, __a0: org.python.core.ThreadState) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def push(self, line: unicode, script: ghidra.python.PythonScript) -> bool:
        """
        Pushes (executes) a line of Python to the interpreter.
        @param line the line of Python to push to the interpreter
        @param script a PythonScript from which we load state (or null)
        @return true if more input is needed before execution can occur
        @throws PyException if an unhandled exception occurred while executing the line of python
        @throws IllegalStateException if this interpreter has been cleaned up.
        """
        ...

    def resetbuffer(self) -> None: ...

    def runcode(self, __a0: object) -> None: ...

    @overload
    def runsource(self, __a0: unicode) -> bool: ...

    @overload
    def runsource(self, __a0: unicode, __a1: unicode) -> bool: ...

    @overload
    def runsource(self, __a0: unicode, __a1: unicode, __a2: org.python.core.CompileMode) -> bool: ...

    @overload
    def set(self, __a0: unicode, __a1: object) -> None: ...

    @overload
    def set(self, __a0: unicode, __a1: object) -> None: ...

    @overload
    def setErr(self, __a0: java.io.OutputStream) -> None: ...

    @overload
    def setErr(self, __a0: java.io.Writer) -> None: ...

    @overload
    def setErr(self, __a0: object) -> None: ...

    @overload
    def setIn(self, __a0: java.io.InputStream) -> None: ...

    @overload
    def setIn(self, __a0: java.io.Reader) -> None: ...

    @overload
    def setIn(self, __a0: object) -> None: ...

    def setLocals(self, __a0: object) -> None: ...

    @overload
    def setOut(self, __a0: java.io.OutputStream) -> None: ...

    @overload
    def setOut(self, __a0: java.io.Writer) -> None: ...

    @overload
    def setOut(self, __a0: object) -> None: ...

    def showexception(self, __a0: exception) -> None: ...

    @staticmethod
    def threadLocalStateInterpreter(__a0: object) -> org.python.util.PythonInterpreter: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def write(self, __a0: unicode) -> None: ...
