"""Sample HelloWorld Program.

This is a sample HelloWorld program to demonstrate proper
Python coding style, testing, documentation, and more.

Author: Olivia Ford orford@mnu.edu
Version: 0.1
"""


class HelloWorld:
    """Simple HelloWorld Class.

    Prints "Hello World" to the terminal when the main function is executed.
    """
    @staticmethod
    def main(args):
        """Prints a hello message.

        This method prints the standard "Hello World" message to the terminal.

        Args:
            args: The command-line arguments provided to the program.
        """
        if len(args) == 2:
            print("Hello {}".format(args[1]))
        else:
            print("Hello World")
