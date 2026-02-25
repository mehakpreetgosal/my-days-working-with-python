#File handling in Python involves using built-in functions to perform operations 
#like creating, opening, reading, writing, and closing files. 
# The most efficient and recommended way is using the with open() statement, 
# which ensures the file is automatically closed, even if errors occur.

f = open("data.txt", "w") #Accesses a file
f.write("Hello Python") #insets new data into the file
f.close() #Releases system resources associated with the file. 
#(Handled automatically by with statement).

f = open("data.txt", "w")
f.write("My name is Monkey D Luffy and I'm gonna be the king of the pirates!")
f.close()

f = open("data.txt", "r")
data = f.read() # retrieves data from the file and stores it in a variable
print(data)
f.close()

f = open("data.txt", "a") #Adds new data to the end of the file (preserves existing content).
f.write("\nWelcome")
f.close()

#with statement
with open("data.txt", "r") as f:
    print(f.read())

#read line by line
with open("data.txt", "r") as f:
    for line in f:
        print(line)

#Error handling in Python is primarily managed 
# using the try...except block to catch and respond to runtime errors,
#  known as exceptions, without crashing the program.

x = int(input("Enter number: "))
print(10 / x)

#try: This block contains the code that might raise an exception.
try:
    x = int(input("Enter number: "))
    print(10 / x)
except:
    print("Error occurred")
#except: This block executes if an exception occurs in the try block.

try:
    x = int(input("Enter number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")

try:
    print(10 / 2)
except:
    print("Error")
else:
    print("No error occurred")
#else: The code in this block is executed only if 
# the code in the try block runs without raising any exceptions.

try:
    f = open("data.txt", "r")
    print(f.read())
except:
    print("File error")
finally:
    print("Program finished")

#finally: This block of code is always executed, regardless of 
#whether an exception occurred or not. It is typically used for essential 
# cleanup actions, such as closing files or network connections    

# one more example of error handling:
try:
    # Code that may raise an exception
    numerator = 10
    denominator = int(input("Enter a number: "))
    result = numerator / denominator
except ZeroDivisionError:
    # Handle specific error: division by zero
    print("Error: Division by zero is not allowed.")
except ValueError:
    # Handle specific error: invalid input type
    print("Error: Please enter a valid integer.")
else:
    # Code to run if no exceptions occurred
    print(f"Result is {result}")
finally:
    # Code that always runs (cleanup)
    print("Execution complete.")
