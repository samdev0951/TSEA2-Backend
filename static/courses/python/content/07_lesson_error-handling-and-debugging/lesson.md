### Error Handling

When writing code in any programming language, you will come across errors. Syntax errors occur when there is a grammar mistake in the code, causing the compiler or interpreter to stop execution. In this case, “grammar” refers to the rules of the programming language. Exceptions are another type of error - they occur during the execution of the program. For example, an int casted input only handles numbers, but if the user enters a letter, the program will throw an exception error if it’s not handled.

There are specialised keywords in Python to help you handle unexpected errors. The “try” keyword is used for testing a block of code for errors. The “except” keyword is used to handle errors in a program. It’s especially useful when you update part of an application and want to make sure it works with the rest of the existing code. Lastly, the “finally” keyword is used to define a block that will execute no matter the outcome, whether an error is caught by “try” or not. 

### Debugging

The debugging process consists of three steps to successfully tackle it. 1. Figure out the source of the problem. Use print statements to print a simple message to the console to verify which parts of the code are being executed. 2. Understand WHY it’s happening. Without a clear understanding of the reason behind the error, it will be difficult to come up with a solution. 3. Fix the error and verify the solution. Once you have found the error, you can work on a solution. Make sure to test the solution to ensure errorless execution.