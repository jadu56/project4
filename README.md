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

