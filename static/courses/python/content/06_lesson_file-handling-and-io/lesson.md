### File Handling and I/O

#### File Handling

File handling refers to managing files throughout their lifetime. We can use operations such as reading from or writing data to files.

Access modes specify the type of operation allowed on the file when it is opened. To open a file, you can use the ‘open()’ function, which takes two parameters: the first one specifies the path for the file, and the second one specifies access mode. In Python, there are 6 access modes you can use, these include:

 - Read Only (r)
 - Read and Write (r+)
 - Write Only (w)
 - Write and Read (w+) 
 - Append Only (a)
 - Append and Read (a+)


### Input / Output (I/O)

I/O in Python allows us to handle user input and output data to the console. The ‘input()’ function is used for taking user input. It works by pausing program execution and waiting for the user to type something. Once they’re finished entering their input, they can press Enter to continue program execution. The ‘input()’ function is commonly assigned to a variable (e.g., userInput = input()) so the user input is stored and can be used later in the program. The ‘print()’ function enables us to output data to the console. To print a variable, you write data in the parentheses (e.g., print(”Hello World”). To print a variable, you simply write an existing variable in the parentheses like so: numVar = 5 print(numVar).

You can also typecast an input: wrapping the input function in a type, e.g., int(input()). This is useful when you want to treat an input as a specific data type rather than a plain string.