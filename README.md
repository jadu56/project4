# File Reading with Error Handling in Python

This Python program demo how to safely **read files** using error handling (`try/except`) and how to read content from files line by line.

##  Features
- Attempts to open and read from `sample2.txt`.
  - If the file does not exist, it prints **"File not found"** instead of crashing.
- Reads the **first line** from another file called `sample.txt`.

##  Code Example
```python
try:
    with open("sample2.txt", "r") as file1:
        reading = file1.read()
        print(reading)
except FileNotFoundError:
    print("File not found")

with open("sample.txt", "r") as file:
    reading = file.readline()
    print(reading) 




















# File Read, Write, and Append Program

This is a simple Python program that demo how to **write**, **append**, and **read** text from a file.

##Features
- Takes user input and **writes** it to a new file (`text1.txt`).
- Allows the user to **append** additional text to the same file.
- Finally, it **reads** the content of the file and displays it on the screen.

## Code Example
```python
text_1 = input("Enter a text to write to the file: ")
with open("text1.txt", "w") as file1:
    write1 = file1.write(text_1 + "\n")

with open("text1.txt", "a") as file1:
    text_2 = input("Enter additional text to append: ")
    write2 = file1.write(text_2 + "\n")

with open("text1.txt", "r") as file1:
    read1 = file1.read()
    print(read1)

