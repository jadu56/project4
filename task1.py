try:
    with open("sample2.txt", "r") as file1:
        reading = file1.read()
        print(reading)
except FileNotFoundError:
    print("File not found")


with open("sample.txt","r")as file:
    reading = file.readline()
    print(reading)