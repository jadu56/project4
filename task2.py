text_1=input("Enter a text to write to the file: ")
with open("text1.txt","w") as file1:
    write1=file1.write(text_1 +"\n")

with open("text1.txt","a") as file1:
    text_2=input("Enter additional text to append: ")
    write2=file1.write(text_2 +"\n")

with open("text1.txt","r") as file1:
    read1=file1.read()
    print(read1)