import java.io
import java.lang


class TestApplicationUtils(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getInstallationDirectory() -> java.io.File:
        """
        Returns the directory containing the installation of this application.   The value returned
         here will either be an actual installation directory or the parent directory of a cloned
         repository.  This method will work in the various modes of operation, including:
         <ul>
         	<li><u>Development Mode</u> - running from a repo clone, from inside of an IDE or the
         command-line.   In this mode a sample directory structure is:
         <pre>
         		/.../git_repos/ghidra_clone/ghidra/Ghidra/Features/Base/src/...

         		which means this method will return 'ghidra_clone'
         </pre>
          </li>
          <li><u>Batch Testing Mode</u> - running from a test server, but not from inside a
          complete build.  This mode uses jar files for the compiled source code, but is running
          from within the structure of a cloned repo.  In this mode a sample directory structure is:
         <pre>
         		/.../git_repos/ghidra_clone/ghidra/Ghidra/Features/Base/src/...

         		which means this method will return 'ghidra_clone'
         </pre>
          </li>
          <li><u>Eclipse Release Development Mode</u> - running from a full application release.
          This mode uses jar files from the installation for dependencies.  The user test files
          are run from within an Eclipse that has been linked with the application installation.
          In this mode a sample directory structure is:
         <pre>
         		/.../Software/ghidra_10.0/Ghidra/Features/Base/lib/Base.jar

         		which means this method will return 'ghidra_10.0'
         </pre>
          </li>
         </ul>
        @return the installation directory
        """
        ...

    @staticmethod
    def getUniqueTempFolder() -> java.io.File:
        """
        Creates a folder that is unique for the current installation. This allows clients to
         have multiple clones (for development mode) or multiple installations (for release mode)
         on their machine, running tests from each repo simultaneously.
        @return a folder that is unique for the current installation
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
