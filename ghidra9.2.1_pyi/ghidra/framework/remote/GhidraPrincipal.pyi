import ghidra.framework.remote
import java.io
import java.lang
import java.security
import javax.security.auth


class GhidraPrincipal(object, java.security.Principal, java.io.Serializable):
    """
    GhidraPrincipal specifies a Ghidra user as a Principal
     for use with server login/authentication.
    """

    serialVersionUID: long = 0x1L



    def __init__(self, username: unicode):
        """
        Constructor.
        @param username user id/name
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getGhidraPrincipal(subj: javax.security.auth.Subject) -> ghidra.framework.remote.GhidraPrincipal:
        """
        Returns the GhidraPrincipal object contained within a Subject, or null if
         not found.
        @param subj user subject
        @return GhidraPrincipal or null
        """
        ...

    def getName(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def implies(self, __a0: javax.security.auth.Subject) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def name(self) -> unicode: ...
