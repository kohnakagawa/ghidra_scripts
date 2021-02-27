import ghidra.program.database.util
import ghidra.program.model.listing
import java.lang


class ProgramTransaction(object, java.lang.AutoCloseable):
    """
    A convenience context for transaction IDs on a Ghidra program database


     This is meant to be used as an idiom in a try-with-resources block:






     This idiom is very useful if there is complex logic in your transaction, it's very easy to forget
     to close the transaction, especially if an error occurs, leaving the database in an open
     transaction indefinitely. The try-with-resources block will ensure that the transaction is closed
     in all circumstances. Note, however, that in order for the transaction to be committed, you must
     call #commit().


     Any exceptions within the block will cause  to be skipped, thus aborting the
     transaction.
    """









    def close(self) -> None:
        """
        Finish the transaction

         <p>
         If this is called before {@link #commit()}, then the transaction is aborted. This is called
         automatically at the close of a try-with-resources block.
        """
        ...

    def commit(self) -> None:
        """
        Finish the transaction, and commit

         <p>
         This MUST be called in order to commit the transaction. The transaction is not committed
         until the close of the try-with-resources block.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def open(program: ghidra.program.model.listing.Program, description: unicode) -> ghidra.program.database.util.ProgramTransaction:
        """
        Start a transaction on the given program with the given description
        @param program the program to modify
        @param description a description of the transaction
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
