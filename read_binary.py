print("starting file...")
file_name = r"binarytext.bin"
file_object = open(file_name, "rb")
content = file_object.read()
text_content = content.decode("utf-8")

print("Content: \n", text_content)
file_object.close()
print("closing file")