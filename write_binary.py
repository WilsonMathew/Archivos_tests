list_strings = ["python\n", "java\n", "c++\n", "ruby\n", "basic\n"]

print("Opening file...")

#opening file to write

file_name = r"binarytext.bin"
file_object = open(file_name,"wb")

#write contento to the file

for item in list_strings:
        list_bytes = item.encode("utf-8")
        file_object.write(list_bytes)

#close file

file_object.close()
print("closing file..")