f = open('myfile.txt','r')    # Gives an error if file doesn't exist. Default mode.
text = f.read()
print(text)
f.close()

# "text(t)":-To handle text files["file",'rt']
# "binary(b)":-To handle binary files["file",'rb']

f = open('myfile.txt','w')   # Creates new file if it doesn't exit.
f.write("Hello world!!")
f.close()

f = open('myfile.txt','a')   # Creates new file if it doesn't exit with the contents safe.
f.write("\nAwesome!!")
f.close()


with open('myfile.txt','a') as f :    # To automatically close file.
    f.write("\nHow are you?")

