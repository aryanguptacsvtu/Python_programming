with open('file.txt', 'r') as f:
    print(type(f))

    f.seek(10)    # Move to 10th byte in file.

    print(f.tell())

    data = f.read(5)
    print(data)


with open('sample.text','w') as g:
    g.write("Hello world!")
    g.truncate(4)



# 'seek()' allows you to move the current position within a file to a specific point.
# 'tell()' returns the current position within file(in bytes).
# 'truncate()' is used to truncate the file to a specific size.
